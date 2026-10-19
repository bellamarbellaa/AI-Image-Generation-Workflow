# Nano Banana 2 — Image Generation System

This project implements the **Nano Banana 2 (Gemini 3.1 Flash Image) & Nano Banana Pro (Gemini 3 Pro Image)** system using structured **JSON Prompting** within Google Antigravity.

---

## 🎯 Core Operating Principles

1. **Always Use Structured JSON Prompting**
   - Never send raw, vague, single-line text prompts directly to image generation models.
   - Every user request must be converted into a structured JSON prompt adhering to the schema defined in the `nano-banana` skill (`.agents/skills/nano-banana/SKILL.md`).
   - Granular control over camera lens, lighting, composition, texture, color grading, and negative prompts is mandatory for photorealism and consistency.

2. **Strict File & Directory Organization**
   - Prompts and generated images MUST mirror each other across these 5 categories:
     - `infographics/` (diagrams, explanatory posters, step-by-step guides)
     - `people/` (portraits, candid shots, lifestyle, fashion, character studies)
     - `photography/` (landscapes, architectural, street, wildlife, fine-art)
     - `products/` (e-commerce, studio shoots, advertising mockups, editorial packshots)
     - `miscellaneous/` (creative UI design, conceptual art, abstract, hybrid styles)
   - JSON prompt files go to: `prompts/<category>/<descriptive_name>.json`
   - Generated images go to: `images/<category>/<descriptive_name>.png`

3. **Autonomous Execution Workflow**
   When the user asks to create, test, or iterate on an image:
   - **Step 1: Analyze & Clarify**: Identify the category and visual intent. If the user asks for multiple styles (e.g., documentary realism vs lifestyle vs studio), formulate distinct style directions.
   - **Step 2: Generate JSON Prompts**: Write the JSON prompt files and save them to `prompts/<category>/<name>.json`.
   - **Step 3: Render the Image**: Execute generation via `python3 generate.py prompts/<category>/<name>.json` (or native Antigravity generation tools).
   - **Step 4: Present & Review**: Present the generated image and key parameters back to the user.
   - **Step 5: Feedback & Refinement**: If the user provides feedback (e.g., "more skin texture", "warmer lighting"), update the prompt and the skill's reference rules if generalizable.

---

## 🛠️ Tooling & Scripts

- **Generation CLI**: `python3 generate.py <path_to_json_prompt>`
- **Models Supported**:
  - `gemini-3.1-flash-image` (Nano Banana 2 — default, fast, cost-effective, excellent text rendering)
  - `gemini-3-pro-image` (Nano Banana Pro — highest detail, complex reasoning, premium aesthetic)
  - `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite — ultra-fast, high volume)
- **Reference Guide**: Inspect `.agents/skills/nano-banana/references/master_reference_guide.md` for specific lens focal lengths, lighting setups, and negative prompt libraries.
