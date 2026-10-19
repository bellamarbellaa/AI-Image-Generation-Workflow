---
name: nano-banana
description: Translates user image requests into hyper-realistic, consistent JSON prompt schemas for Nano Banana 2 (gemini-3.1-flash-image) and Nano Banana Pro (gemini-3-pro-image), saves them to prompts/<category>/, and generates images into images/<category>/.
---

# Nano Banana Image Generation Skill

Use this skill whenever the user requests an image generation, visual concept, product shoot, portrait, infographic, or photo redesign.

## Core Objective
Convert vague plain-text requests into precise, structured **JSON Prompts**. JSON prompting eliminates the randomness of AI image generators by providing fine-grained arguments that Gemini models interpret with extreme fidelity.

---

## 📂 Category Mapping
Always route prompts and images into one of the following 5 directories:
1. `people`: Portraits, candid shots, headshots, lifestyle influencers, fashion, street portraits.
2. `products`: Commercial ads, e-commerce studio shots, packaging, cosmetic bottles, tech gadgets.
3. `photography`: Landscape, architecture, interior design, street photography, macro nature.
4. `infographics`: Flowcharts, explanatory diagrams, posters with accurate typography, educational visuals.
5. `miscellaneous`: Game UI, digital art, stylized graphics, hybrid concepts.

File paths must strictly follow:
- Prompt: `prompts/<category>/<snake_case_name>.json`
- Image: `images/<category>/<snake_case_name>.png`

---

## 📐 JSON Prompt Specification Schema

When authoring a JSON prompt, structure the object according to this canonical schema:

```json
{
  "title": "Descriptive title of the scene",
  "category": "people | products | photography | infographics | miscellaneous",
  "model": "gemini-3.1-flash-image",
  "subject": {
    "entity": "Primary subject description",
    "details": "Micro-details (e.g. skin pores, fabric weave, condensation droplets, glass reflections)",
    "expression_or_state": "Facial expression or physical state",
    "wardrobe_or_material": "Clothing, textures, materials"
  },
  "composition": {
    "framing": "Extreme close-up | Close-up | Medium shot | Full body | Wide shot | Flat lay top-down",
    "camera_angle": "Eye level | Low angle | High angle | Dutch angle | Overhead 90-degree",
    "lens": "24mm wide | 35mm street | 50mm natural | 85mm portrait | 100mm macro",
    "depth_of_field": "Shallow (f/1.4 - f/2.8) with soft bokeh | Deep (f/8 - f/11) everything sharp",
    "focus_point": "Exact element in tack-sharp focus"
  },
  "lighting": {
    "type": "Natural window light | Golden hour sunlight | Studio softbox | Rim lighting | Neon noir | Diffused overcast",
    "direction": "Side-lit | Back-lit | Front diffused | Top-down butterfly",
    "color_temperature": "Warm 3200K | Daylight 5600K | Cool 6500K",
    "shadows": "Soft gradual falloff | High contrast chiaroscuro"
  },
  "environment": {
    "location": "Specific realistic setting",
    "background_elements": "Secondary background details that build depth",
    "atmosphere": "Dust motes in light beams, light mist, clean minimalist studio, morning fog"
  },
  "style": {
    "aesthetic": "Documentary realism | High-fashion editorial | Candid 35mm film | Commercial packshot",
    "film_stock_or_sensor": "Kodak Portra 400 | Fujifilm Provia | Hasselblad H6D-100c medium format sensor",
    "color_grading": "Natural color palette, realistic skin tones, uncompressed tonal range"
  },
  "technical": {
    "aspect_ratio": "1:1 | 16:9 | 9:16 | 4:3 | 3:4 | 2:3 | 3:2",
    "image_size": "1K | 2K | 4K",
    "google_search_grounding": false
  },
  "negative_prompt": "cartoon, 3d render, CGI, plastic waxy skin, airbrushed, oversaturated, deformed hands, missing fingers, extra limbs, blurry, pixelated, watermark, stock photo fake smile"
}
```

---

## 🎨 Best Practices by Domain

### 1. People & Portraits
- **Skin Realism**: Explicitly request `"visible natural skin texture, delicate pores, subtle natural blemishes, realistic peach fuzz, accurate specular highlights on brow and nose bridge"`.
- **Eyes**: `"Crisp catchlights in iris, visible cornea reflections, natural lash separation"`.
- **Avoid**: `"perfect porcelain skin"`, `"flawless"`, `"smooth face"` — these trigger synthetic plastic AI looks.

### 2. Products & Commercial Ads
- **Materials**: Specify refractive index, surface finishes (brushed aluminum, frosted glass, matte paper, glossy acrylic).
- **Hero Angle**: Three-quarter hero angle or flat-lay.
- **Lighting**: Softbox key light at 45 degrees, subtle rim kicker to outline silhouette against backdrop.
- **Text & Branding**: Provide explicit string characters (e.g. `"text 'EAU DE PARFUM' and '100ml 3.4 FL.OZ' crisply printed in clean Helvetica typography"`).

### 3. Infographics & Diagrams
- Nano Banana 2 has superior spatial reasoning and text rendering.
- Specify exact labels, flow arrows, clean callout cards, isometric or flat 2D layout.
- Set `google_search_grounding: true` if grounding with real-world scientific or geographical data.

---

## 🚀 Execution Workflow

When requested:
1. Create the JSON file under `prompts/<category>/<name>.json`.
2. Run generation:
   ```bash
   python3 generate.py prompts/<category>/<name>.json
   ```
3. The generated PNG is saved to `images/<category>/<name>.png`.
4. Inspect the output and provide the user with the file path and summary of chosen aesthetics.
