# Nano Banana 2 & Pro: Master Reference Guide

This reference guide catalogues all parameters, optical properties, lighting techniques, and aesthetic tokens for crafting high-fidelity JSON prompts.

---

## 1. Camera & Optics Reference

### Lenses & Focal Lengths
| Focal Length | Typical Name | Characteristics & Use Cases |
|---|---|---|
| **16mm - 24mm** | Ultra-wide / Wide | Dynamic perspective, architectural interiors, environmental landscapes, dramatic foreground scaling. |
| **35mm** | Street / Documentary | Classic photojournalism, natural spatial relationship, editorial lifestyle, environmental portraits. |
| **50mm** | Standard "Nifty Fifty" | Human eye perspective, zero perspective distortion, balanced commercial and street photography. |
| **85mm** | Portrait Prime | Flattering facial compression, creamy bokeh background separation, professional headshots and beauty shoots. |
| **105mm - 135mm** | Telephoto Portrait | Strong background compression, isolating subjects from busy environments, beauty macro. |
| **90mm - 100mm Macro** | True Macro | 1:1 magnification, microscopic product details, watch mechanisms, water droplets, cosmetic textures. |

### Aperture & Depth of Field (DoF)
- **`f/1.2 - f/1.8`**: Razor-thin focal plane, soft dreamy bokeh, subject isolated completely from background.
- **`f/2.8 - f/4.0`**: Standard commercial portraiture, sharp facial features from tip of nose to ears, soft background falloff.
- **`f/8.0 - f/11.0`**: Sweet spot for studio product photography and commercial packshots, full product in tack-sharp focus.
- **`f/16.0`**: Landscape photography, infinite depth of field from foreground rocks to distant horizon.

### Camera Angles & Perspectives
- **Eye-level**: Relatable, candid, natural human connection.
- **Low-angle (worm's eye)**: Imposing, heroic, empowering, emphasizes height and dominance.
- **High-angle**: Vulnerable, artistic overview, contextualizes surrounding environment.
- **Dutch angle (tilted)**: Tension, kinetic motion, cinematic drama.
- **Flat-lay (knolling / 90° top-down)**: Clean geometric organization, culinary layouts, gear spreads, minimalist cosmetics.

---

## 2. Lighting & Illumination Setups

### Natural Lighting
- **Golden Hour**: Low-angle sun (15-20° above horizon), warm 3200K amber glow, long soft shadows, natural lens flare.
- **Blue Hour**: 20-30 minutes post-sunset, cool 7500K deep blue ambient wash, high dynamic range with interior practical lights.
- **Diffused Overcast**: Giant softbox sky, zero harsh shadows, gentle tonal gradients, ideal for high-detail documentary skin texture.
- **Direct Midday Sun**: High contrast, crisp defined shadows, high-fashion editorial, swimming pool reflections, summer campaign feel.
- **Window Light (North-facing)**: Classic painterly soft light, subtle falloff across face, Vermeer-inspired Vermeer look.

### Studio Lighting Techniques
- **Rembrandt Lighting**: Key light at 45° producing a distinct illuminated triangle on the shadow cheek.
- **Butterfly / Paramount Lighting**: Key light directly above and in front of camera, creating a small symmetrical shadow under the nose, cheekbones accentuated.
- **Split Lighting**: Key light placed 90° to the side, slicing face into 50% light and 50% dark shadow, intense dramatic mood.
- **Rim / Edge / Kicker**: Light positioned behind the subject to delineate hair, shoulders, or bottle contours from dark background.
- **Softbox & Scrim**: Studio flash diffused through large silk scrim for ultra-smooth reflections on glass and polished metal.

---

## 3. Surface & Material Physicality (Combating "AI Look")

### Human Skin & Features
- ✅ **Prompt Tokens**: `visible skin pores`, `fine micro-texture`, `natural sebum specularity on T-zone`, `fine vellus hair (peach fuzz)`, `subtle laugh lines`, `realistic skin subsurface scattering (SSS) with warm reddish glow along shadow boundaries`.
- ❌ **Forbidden Tokens**: `flawless skin`, `smooth skin`, `perfect complexion`, `porcelain face`, `airbrushed`, `doll-like`.

### Materials & Industrial Textures
- **Glass / Perfume Bottles**: `flint glass with high refractive index`, `crisp internal liquid caustics`, `laser-etched typography`, `microscopic air bubbles in tube`.
- **Cosmetics & Creams**: `velvety matte emulsion`, `viscous swirl with glossy apex`, `micro-droplets of condensation on frosted container`.
- **Metals**: `anodized brushed aluminum with linear grain`, `chamfered CNC edges catching subtle specular highlight`, `fingerprint-resistant satin finish`.
- **Fabrics**: `organic raw linen with tactile slub weave`, `heavyweight 400gsm cotton jersey`, `delicate silk chiffon with translucent drape`.

---

## 4. Aspect Ratios & Supported Resolutions in Nano Banana 2

| Aspect Ratio | Resolution Options | Ideal Applications |
|---|---|---|
| **`1:1`** | 1024x1024 (1K), 2048x2048 (2K), 4096x4096 (4K) | Instagram feed, square product tiles, avatars |
| **`9:16`** | 768x1376 (1K), 1536x2752 (2K), 3072x5504 (4K) | TikTok, Instagram Stories/Reels, mobile wallpaper |
| **`16:9`** | 1376x768 (1K), 2752x1536 (2K), 5504x3072 (4K) | YouTube thumbnails, widescreen cinematic, presentation hero |
| **`4:5`** | 928x1152 (1K), 1856x2304 (2K), 3712x4608 (4K) | Portrait Instagram posts |
| **`3:4` / `2:3`** | Standard photo portrait | Editorial magazine covers, classic 35mm portrait |
| **`4:3` / `3:2`** | Standard photo landscape | Classic DSLR landscape, editorial spreads |

---

## 5. Universal Negative Prompt Bank

Combine and curate from this library depending on the category:

```
cartoon, 3D CGI animation, digital render, plastic skin, silicone sheen, airbrushed, wax figure, mannequin, oversaturated colors, harsh chromatic aberration, distorted anatomy, extra fingers, fused digits, unnatural limb bending, asymmetrical pupils, blurry textures, compression artifacts, ugly typography, misspelled words, stock photo watermark, fake posed smile
```
