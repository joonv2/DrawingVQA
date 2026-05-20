# DrawingVQA

[![Paper](https://img.shields.io/badge/arXiv-Coming_Soon-b31b1b)](#)
[![Website](https://img.shields.io/badge/Project_Page-joonv2.github.io-blue)](https://joonv2.github.io/DrawingVQA/)
[![Dataset Example](https://img.shields.io/badge/Dataset-HuggingFace-yellow)](https://huggingface.co/datasets/S2-MIND/DrawingVQA)
[![HuggingFace Leaderboard](https://img.shields.io/static/v1?label=Huggingface&message=AGI-LEADERBOARD&color=%23d4a574&labelColor=%238b6239&logo=HUGGINGFACE&logoColor=%23faf8f5&style=for-the-badge)](https://huggingface.co/spaces/S2-MIND/DrawingVQA-leaderboard)

**[CVPR Findings 2026]** DrawingVQA: A Real-World Benchmark for Multi-Depth Visual–Textual Reasoning on Construction Drawings.

**Authors**: Yoonhwa Jung*, Junryu Fu*, Mani Golparvar-Fard
(*Equal contribution)

**Paper**: [Link to arXiv (Coming Soon)](#)

DrawingVQA is the first benchmark designed to evaluate multimodal large language models (MLLMs) on real-world "Issued for Construction" (IFC) structural drawings. Unlike standard natural images or simplified schematic floor plans, this dataset fuses abstract geometry, symbolic notation, tabular data, annotations, and domain-specific text, reflecting authentic engineering workflows.

---

## 🏗️ Benchmark Highlights

* **Authentic Domain Data**: 33 full IFC-grade structural drawings and 92 expertly curated QA pairs.
* **Three Reasoning Depths**: Questions are categorized into Perceptual Understanding (R1), Contextual Interpretation (R2), and Domain-Expert Reasoning (R3).
* **Dual Categorization Framework**: The first benchmark to explicitly map engineering workflows (QTO, Compliance, etc.) to core AI reasoning competencies (OCR, Visual Perception, Spatial Reasoning).
* **Expert-Level Baselines**: Compares frontier models (Gemini 2.5 Pro, GPT-4o, Claude 3.5 Sonnet, Qwen-VL) against robust human baselines (Undergraduates, Young Professionals, and Experienced Professionals). 

---

## 🚀 Quick Start

The dataset and leaderboard is hosted on Hugging Face. You do not need to download local images, as all the text and QA structure is available directly via the Hugging Face.

```bash
Coming soon
```
---

## 📊 Dataset Structure

Each record in the dataset is flattened and normalized for easy downstream evaluation. The schema includes the following features:

| Field | Type | Description |
| :--- | :--- | :--- |
| `image_name` | `string` | SHA-256 hashed filename of the primary drawing image. |
| `image2_name` | `string` | Hashed filename for a secondary image (if applicable). |
| `image3_name` | `string` | Hashed filename for a secondary image (if applicable). |
| `image4_name` | `string` | Hashed filename for a secondary image (if applicable). |
| `image5_name` | `string` | Hashed filename for a secondary image (if applicable). |
| `question` | `string` | The text of the multiple-choice or open-ended question. |
| `option_a` | `string` | Distractor / Option A (expertly crafted to avoid language shortcuts). |
| `option_b` | `string` | Distractor / Option B. |
| `option_c` | `string` | Distractor / Option C. |
| `option_d` | `string` | Distractor / Option D. |
| `option_e` | `string` | Distractor / Option E (if applicable). |
| `answer` | `string` | The correct answer option (e.g., "A", "B", "C", "D" or short text). |
| `explanation` | `string` | Step-by-step reasoning and explanation provided by the domain expert. |
| `cv_field` / `cv_subfield` | `list[string]` | MLLM cognitive capability tags (e.g., OCR, Visual Perception, Spatial Reasoning). |
| `ce_field` / `ce_subfield`| `list[string]` | Construction-Engineering workflow tags (e.g., Quantity Take-Off, Compliance). |
| `topic_difficulty` | `string` | The reasoning depth required (e.g., R1, R2, R3). |

*Note: Due to privacy constraints regarding real-world "Issued for Construction" documents, image filenames are hashed and the original high-resolution PDFs/images are kept private. The text-based question set is fully open for evaluation.*

---

## 🏆 Leaderboard

We evaluated top-tier models and compared them to human experts. As of early 2025, human professionals significantly outperform all SOTA models, especially on tasks requiring Quantity Take-Off (QTO) and Level 3 Expert Reasoning.

* **Top Model**: Gemini-3-pro-preview (77.2%) / Gemini-2.5-pro (71.7%)
* **Human Professional**: 94.9%
* **Undergraduate Baseline**: 62.8%

For the full leaderboard and fine-grained dual-category breakdowns, visit our [Project Page](https://joonv2.github.io/DrawingVQA/).

---

## 📝 Citation

If you use DRAWINGVQA in your research, please cite our CVPR 2026 paper:

```bibtex
@inproceedings{jung2026drawingvqa,
  title     = {DrawingVQA: A Real-World Benchmark for Multi-Depth Visual-Textual Reasoning on Construction Drawings},
  author    = {Jung, Yoonhwa and Fu, Junryu and Golparvar-Fard, Mani},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Findings},
  year      = {2026},
  note      = {In press},
  url       = {[https://joonv2.github.io/DrawingVQA/](https://joonv2.github.io/DrawingVQA/)}
}
```

---

## 📄 License

The text-based question-answer pairs and benchmark metadata are released under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/) license.
