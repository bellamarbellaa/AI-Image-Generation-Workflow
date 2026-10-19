#!/usr/bin/env python3
"""
Nano Banana 2 & Pro Image Generator
Converts structured JSON prompts into high-fidelity image outputs using the official Google GenAI SDK.
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Optional .env loading
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def compile_json_to_prompt(data: dict) -> str:
    """
    Compiles structured JSON prompt fields into an optimized textual prompt for the image model,
    retaining explicit key descriptors, camera settings, lighting, and negative prompts.
    """
    lines = []

    # Title / Subject
    if "title" in data:
        lines.append(f"Subject: {data['title']}")

    subject = data.get("subject", {})
    if isinstance(subject, dict):
        entity = subject.get("entity", "")
        details = subject.get("details", "")
        expr = subject.get("expression_or_state", "")
        wardrobe = subject.get("wardrobe_or_material", "")
        sub_desc = []
        if entity:
            sub_desc.append(entity)
        if details:
            sub_desc.append(f"Physical details: {details}")
        if expr:
            sub_desc.append(f"Expression/State: {expr}")
        if wardrobe:
            sub_desc.append(f"Attire/Material: {wardrobe}")
        if sub_desc:
            lines.append("Description: " + "; ".join(sub_desc))
    elif isinstance(subject, str):
        lines.append(f"Subject details: {subject}")

    # Composition
    comp = data.get("composition", {})
    if isinstance(comp, dict):
        comp_parts = []
        for k in ["framing", "camera_angle", "lens", "depth_of_field", "focus_point"]:
            if comp.get(k):
                comp_parts.append(f"{k.replace('_', ' ').title()}: {comp[k]}")
        if comp_parts:
            lines.append("Optics & Composition: " + ", ".join(comp_parts))

    # Lighting
    lighting = data.get("lighting", {})
    if isinstance(lighting, dict):
        light_parts = []
        for k in ["type", "direction", "color_temperature", "shadows"]:
            if lighting.get(k):
                light_parts.append(f"{k.replace('_', ' ').title()}: {lighting[k]}")
        if light_parts:
            lines.append("Lighting: " + ", ".join(light_parts))

    # Environment
    env = data.get("environment", {})
    if isinstance(env, dict):
        env_parts = []
        for k in ["location", "background_elements", "atmosphere"]:
            if env.get(k):
                env_parts.append(f"{k.replace('_', ' ').title()}: {env[k]}")
        if env_parts:
            lines.append("Environment: " + ", ".join(env_parts))

    # Style
    style = data.get("style", {})
    if isinstance(style, dict):
        style_parts = []
        for k in ["aesthetic", "film_stock_or_sensor", "color_grading"]:
            if style.get(k):
                style_parts.append(f"{k.replace('_', ' ').title()}: {style[k]}")
        if style_parts:
            lines.append("Aesthetic Style: " + ", ".join(style_parts))

    # Negative Prompt
    neg = data.get("negative_prompt", "")
    if neg:
        lines.append(f"Negative prompt (elements to strictly avoid): {neg}")

    return "\n\n".join(lines)


def generate_image(prompt_file: Path, model_override: str = None):
    # Verify file
    if not prompt_file.exists():
        print(f"❌ Error: Prompt file '{prompt_file}' not found.", file=sys.stderr)
        sys.exit(1)

    with open(prompt_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Error decoding JSON in {prompt_file}: {e}", file=sys.stderr)
            sys.exit(1)

    category = data.get("category", prompt_file.parent.name)
    model = model_override or data.get("model", "gemini-3.1-flash-image")
    tech = data.get("technical", {})
    aspect_ratio = tech.get("aspect_ratio", "1:1")
    image_size = tech.get("image_size", "1K")
    grounding = tech.get("google_search_grounding", False)

    # Compile prompt
    compiled_prompt = compile_json_to_prompt(data)
    print(f"\n========================================================")
    print(f"🍌 Nano Banana Generation")
    print(f"📂 Prompt:       {prompt_file}")
    print(f"🤖 Model:        {model}")
    print(f"📐 Aspect Ratio: {aspect_ratio}")
    print(f"🔍 Resolution:   {image_size}")
    print(f"🌐 Grounding:    {'Google Search Enabled' if grounding else 'Disabled'}")
    print(f"========================================================\n")

    # Output path
    output_dir = Path("images") / category
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{prompt_file.stem}.png"

    # Check google-genai
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("❌ Missing dependency 'google-genai'. Please run:")
        print("   pip install -r requirements.txt\n")
        print("Or install directly via:")
        print("   pip install google-genai pillow python-dotenv")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("⚠️ Warning: GEMINI_API_KEY environment variable is not set.")
        print("   Please set it via: export GEMINI_API_KEY='your_api_key'")
        print("   Or create a .env file with GEMINI_API_KEY=your_key\n")

    # Load reference images if specified
    ref_images_paths = tech.get("reference_images", [])
    loaded_images = []
    if ref_images_paths:
        try:
            from PIL import Image
            for ref_path in ref_images_paths:
                p = Path(ref_path)
                if p.exists():
                    loaded_images.append(Image.open(p))
                    print(f"🖼️  Loaded reference image: {p}")
                else:
                    print(f"⚠️ Reference image not found: {p}")
        except Exception as e:
            print(f"⚠️ Error loading reference images: {e}")

    try:
        client = genai.Client()

        # Tools configuration (search grounding if requested)
        tools = []
        if grounding:
            tools.append(types.Tool(google_search=types.GoogleSearch()))

        # Config with image_config and response_modalities
        img_cfg_kwargs = {}
        if aspect_ratio:
            img_cfg_kwargs["aspect_ratio"] = aspect_ratio
        if image_size:
            img_cfg_kwargs["image_size"] = image_size

        config = types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(**img_cfg_kwargs) if img_cfg_kwargs else None,
            tools=tools if tools else None,
        )

        print("⏳ Generating image with Gemini...")
        contents = [compiled_prompt] + loaded_images
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=config,
        )

        saved = False
        # Try reading parts directly or from candidates
        parts_to_check = []
        if hasattr(response, "parts") and response.parts:
            parts_to_check = response.parts
        elif hasattr(response, "candidates") and response.candidates:
            for cand in response.candidates:
                if hasattr(cand, "content") and cand.content and hasattr(cand.content, "parts"):
                    parts_to_check.extend(cand.content.parts)

        for part in parts_to_check:
            if getattr(part, "text", None):
                print(f"💬 Model Note: {part.text}")
            if getattr(part, "inline_data", None):
                image = part.as_image()
                image.save(output_file)
                saved = True
                print(f"\n✅ Image successfully generated and saved to:")
                print(f"   🖼️  {output_file.resolve()}\n")

        if not saved:
            print("⚠️ No image was returned in the response payload.")

    except Exception as e:
        print(f"❌ Generation error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate images from JSON prompts using Nano Banana 2")
    parser.add_argument("prompt_file", type=str, help="Path to the JSON prompt file (e.g. prompts/people/portrait.json)")
    parser.add_argument("--model", type=str, default=None, help="Override model (gemini-3.1-flash-image, gemini-3-pro-image, etc.)")
    args = parser.parse_args()

    generate_image(Path(args.prompt_file), model_override=args.model)


if __name__ == "__main__":
    main()
