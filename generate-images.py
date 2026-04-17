import json, base64, time, os, sys
import urllib.request

API_KEY = "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"
MODEL = "google/gemini-2.5-flash-image"
OUT_DIR = "/home/node/.openclaw/workspace/feel-good-initiative/slides"
os.makedirs(OUT_DIR, exist_ok=True)

STYLE = "Style: Documentary editorial photography. Color palette: deep warm teal (#1A3C3C), off-white (#F7F9F8), burnt orange accent (#D95A10), muted sand tones. Cape Town coastal aesthetic. Golden hour lighting with warm teal color grading. Subtle film grain texture. 16:9 aspect ratio. Generous negative space. Premium NPO feel — confident, hopeful, grounded. No stock photography, no clip art. One clear focal point per image."

PROMPTS = {
    "slide-01-title": f"Generate an image: A dramatic aerial view of Hout Bay beach at golden hour. The Atlantic Ocean stretches endlessly, rugged cliffs frame the coastline, warm light catches the water. A single beam of burnt orange light cuts through teal-toned clouds. Cinematic, wide frame, sense of beginning and ambition. This is a title slide background — leave generous space in the center for text overlay. {STYLE}",

    "slide-02-problem": f"Generate an image: A stark, honest documentary photograph. A neglected community noticeboard on a beautiful but undeveloped Cape Town beach. The board is weathered, faded, barely readable. Behind it, the ocean is stunning — the potential is obvious but the presentation is amateur. The gap between what IS and what COULD BE. Shallow depth of field on the noticeboard, ocean blurred behind. {STYLE}",

    "slide-03-comparison": f"Generate an image: Split composition — left side dark and muted showing an empty, bare digital screen with minimal content (representing poor online presence), right side bright and professional showing a polished screen with rich content and imagery (representing credibility). The contrast between amateur and professional. Corporate office environment, natural lighting. The two halves should feel like night and day. {STYLE}",

    "slide-04-approach": f"Generate an image: Three stepping stones emerging from ocean water, each progressively higher and more solid, leading toward a Cape Town coastline at golden hour. The first stone is rough and small, the second is larger and smoother, the third is substantial and catches the orange sunlight. Metaphor for phased growth. Wide cinematic frame, teal water, orange sky. {STYLE}",

    "slide-05-credibility": f"Generate an image: A professional workspace with brand identity materials laid out — color swatches, typography samples, a laptop showing a clean website mockup, business cards, a printed sponsor deck. Everything coordinated in teal, off-white, and orange tones. Overhead flat-lay shot, natural window light. Clean, organized, professional — this is what credibility looks like when built properly. {STYLE}",

    "slide-06-investment": f"Generate an image: Close-up of hands exchanging a professional document across a wooden table. One hand is placing it down confidently, the other reaching to receive it. On the table: a branded folder in teal, a pen, a cup of coffee. The moment of commitment — professional but warm. Shallow depth of field, warm golden light from the side. {STYLE}",

    "slide-07-authority": f"Generate an image: A community storytelling moment on Hout Bay beach. A diverse group of 4-5 people gathered around, one person speaking passionately with hands gesturing toward the ocean. Documentary style, candid, not posed. Warm golden hour light catches their faces. Behind them, the ocean and Table Mountain silhouette. This is authentic story, real people, real mission. {STYLE}",

    "slide-08-pricing": f"Generate an image: Abstract editorial composition — building blocks or modular pieces stacking upward in teal and orange tones against an off-white background. Each block is a different size, representing incremental growth and add-on pricing. Clean, geometric, architectural feel. Minimalist but not empty. The blocks cast long warm shadows. {STYLE}",

    "slide-09-sponsors": f"Generate an image: A Cape Town beach cleanup scene from a dramatic low angle. Volunteers in branded teal t-shirts working together, picking up debris, organizing. In the background, the ocean sparkles under golden light. The energy is positive, active, impactful. A banner or flag with orange accents flutters in the sea breeze. Documentary photography, motion blur on the edges. {STYLE}",

    "slide-10-fullpicture": f"Generate an image: Aerial drone shot of Hout Bay from above — the full bay visible, the beach, the community, the mountain, the ocean stretching to the horizon. Three distinct zones visible: the developed area, the beach, and the open ocean — representing the three phases. Golden hour, warm teal water, orange-lit clouds. Expansive, ambitious, showing the full picture. {STYLE}",

    "slide-11-accountability": f"Generate an image: A clean, modern dashboard or progress chart rendered physically — think a large wall-mounted board in a bright office with growth metrics, arrow charts pointing upward, and milestone markers. Teal background with orange accent markers at key milestones. Professional, data-driven, transparent. Natural light from a nearby window. {STYLE}",

    "slide-12-urgency": f"Generate an image: A dramatic Cape Town sunset — the sun is just touching the horizon over the Atlantic Ocean seen from Hout Bay. The sky is on fire with orange and amber, reflecting on the wet sand. A clock-like shadow or sundial effect from rocks on the beach. Time is passing. The beauty is undeniable but fleeting. Cinematic, emotional, urgent. {STYLE}",

    "slide-13-begin": f"Generate an image: Two hands reaching toward each other across a table, about to shake — one wearing a community wristband, the other a professional watch. Between them on the table, a branded document with teal and orange accents. The moment before partnership. Warm side lighting, shallow depth of field. Hope, commitment, beginning. {STYLE}"
}

for name, prompt in PROMPTS.items():
    out_path = os.path.join(OUT_DIR, f"{name}.png")
    if os.path.exists(out_path):
        print(f"SKIP {name} (exists)")
        continue

    print(f"Generating {name}...", flush=True)
    
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()
    
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            d = json.loads(resp.read())
        
        images = d.get('choices', [{}])[0].get('message', {}).get('images', [])
        if not images:
            # Try content as list
            content = d.get('choices', [{}])[0].get('message', {}).get('content', '')
            if isinstance(content, list):
                images = [p for p in content if p.get('type') == 'image_url']
        
        if images:
            url = images[0].get('image_url', {}).get('url', '')
            if url.startswith('data:'):
                b64 = url.split(',', 1)[1]
                with open(out_path, 'wb') as f:
                    f.write(base64.b64decode(b64))
                size = os.path.getsize(out_path)
                print(f"  ✅ {name} saved ({size} bytes)")
            else:
                print(f"  ❌ {name} — got URL not base64: {url[:100]}")
        else:
            print(f"  ❌ {name} — no images in response")
            print(f"     Response: {json.dumps(d)[:300]}")
    except Exception as e:
        print(f"  ❌ {name} — error: {e}")
    
    time.sleep(2)  # Rate limit buffer

print("\nDone!")
