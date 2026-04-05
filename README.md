# The Complete MSc Reference: AI & ML — Companion Notebooks

**Official code companion for the book by Jijesh Puliyappottammal**  
 AI & Technology Series, Book 4*

---

## 📖 About This Repository

This repository contains **24 Jupyter notebooks**, one per chapter, with all code examples from the book plus additional visualisations and worked exercises not in the print edition.

### Book Overview

| | |
|---|---|
| **Title** | The Complete MSc Reference: Artificial Intelligence & Machine Learning |
| **Subtitle** | A University Companion for Students and Academic Staff |
| **Author** | Jijesh Puliyappottammal |
| **Publisher** | Digichange Publication |
| **Year** | 2026 |
| **Chapters** | 24 across 7 parts |
| **Audience** | MSc AI & ML students, lecturers, AI practitioners |

---

## 🚀 Quick Start

### Option 1 — Run in the cloud (no installation)

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/digichange/msc-ai-ml-companion/blob/main/notebooks/ch01_a_brief_history_and_landscape_of_ai.ipynb)

Click any notebook below and choose **Open in Colab**.

### Option 2 — Run locally

```bash
git clone https://github.com/pJijesh/msc-ai-ml-companion.git
cd msc-ai-ml-companion
pip install -r requirements.txt
jupyter notebook
```

---

## 📚 Notebook Index

### Part I — Foundations

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 1 | [A Brief History and Landscape of AI](notebooks/ch01_a_brief_history_and_landscape_of_ai.ipynb) | matplotlib |
| Ch 2 | [Mathematical Foundations](notebooks/ch02_mathematical_foundations.ipynb) | numpy, matplotlib, torch |
| Ch 3 | [Python for AI Practitioners](notebooks/ch03_python_for_ai_practitioners.ipynb) | numpy, pandas, matplotlib, sklearn |
| Ch 4 | [Research Methods for AI](notebooks/ch04_research_methods_for_ai.ipynb) | sklearn, scipy |

### Part II — Machine Learning Core

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 5 | [Supervised Learning](notebooks/ch05_supervised_learning.ipynb) | sklearn, matplotlib |
| Ch 6 | [Unsupervised Learning](notebooks/ch06_unsupervised_learning.ipynb) | sklearn, matplotlib |
| Ch 7 | [Probabilistic and Bayesian Learning](notebooks/ch07_probabilistic_and_bayesian_learning.ipynb) | sklearn, matplotlib |
| Ch 8 | [Optimisation and Model Selection](notebooks/ch08_optimisation_and_model_selection.ipynb) | torch, sklearn, matplotlib |

### Part III — Deep Learning

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 9 | [Neural Network Fundamentals](notebooks/ch09_neural_network_fundamentals.ipynb) | torch, matplotlib |
| Ch 10 | [Convolutional and Recurrent Networks](notebooks/ch10_convolutional_and_recurrent_networks.ipynb) | torch, torchvision |
| Ch 11 | [Transformers and Large Language Models](notebooks/ch11_transformers_and_large_language_models.ipynb) | torch, transformers |
| | | |

### Part IV — Specialist Domains

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 12 | [Natural Language Processing](notebooks/ch12_natural_language_processing.ipynb) | transformers, sentence-transformers |
| Ch 13 | [Computer Vision](notebooks/ch13_computer_vision.ipynb) | torch, torchvision |
| Ch 14 | [Reinforcement Learning](notebooks/ch14_reinforcement_learning.ipynb) | numpy, matplotlib |
| Ch 15 | [Generative AI](notebooks/ch15_generative_ai.ipynb) | torch, diffusers |
| Ch 16 | [Knowledge Representation and Reasoning](notebooks/ch16_knowledge_representation_and_reasoning.ipynb) | networkx, rdflib |

### Part V — AI Ethics, Governance & Law

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 17 | [Algorithmic Fairness and Bias](notebooks/ch17_algorithmic_fairness_and_bias.ipynb) | sklearn, fairlearn |
| Ch 18 | [Explainability and Trustworthy AI](notebooks/ch18_explainability_and_trustworthy_ai.ipynb) | shap, sklearn |
| Ch 19 | [AI Governance, Regulation and Policy](notebooks/ch19_ai_governance_regulation_and_policy.ipynb) | (no dependencies) |

### Part VI — MLOps & Production AI

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 20 | [Data Engineering for Machine Learning](notebooks/ch20_data_engineering_for_machine_learning.ipynb) | pandas, sklearn |
| Ch 21 | [Model Deployment and Serving](notebooks/ch21_model_deployment_and_serving.ipynb) | torch, sklearn, joblib |
| Ch 22 | [MLOps: CI/CD for AI Systems](notebooks/ch22_mlops_ci_cd_for_ai_systems.ipynb) | sklearn, matplotlib |

### Part VII — Career, Research & Future Directions

| Chapter | Notebook | Key Libraries |
|---------|----------|--------------|
| Ch 23 | [The MSc Dissertation: A Practical Guide](notebooks/ch23_the_msc_dissertation_a_practical_guide.ipynb) | matplotlib |
| Ch 24 | [AI Futures and Emerging Frontiers](notebooks/ch24_ai_futures_and_emerging_frontiers.ipynb) | numpy, matplotlib |

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

### Core requirements

```
numpy>=1.24
pandas>=2.0
matplotlib>=3.7
seaborn>=0.12
scikit-learn>=1.3
torch>=2.0
torchvision>=0.15
transformers>=4.35
sentence-transformers>=2.2
diffusers>=0.21
xgboost>=2.0
lightgbm>=4.0
shap>=0.43
fairlearn>=0.9
networkx>=3.1
rdflib>=7.0
mlflow>=2.8
joblib>=1.3
scipy>=1.11
```

---

## 🗂️ Repository Structure

```
msc-ai-ml-companion/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── notebooks/
│   ├── ch01_a_brief_history_and_landscape_of_ai.ipynb
│   ├── ch02_mathematical_foundations.ipynb
│   ├── ...
│   └── ch24_ai_futures_and_emerging_frontiers.ipynb
└── utils/
    └── plot_helpers.py
```

---

## 📋 Notes for Lecturers

Each notebook follows the same structure as the corresponding chapter:
- **Setup cell** — imports and version check
- **Book code examples** — all `codeBlock()` examples from the print edition
- **Extended examples** — additional visualisations and worked exercises
- **Review questions** — pointers back to the textbook's exam preparation material

Notebooks are designed to be **self-contained** — students can run each independently without completing previous chapters.

---

## 📄 Licence

**Code:** MIT Licence — free to use, modify, and distribute for educational purposes.  
**Text and book content:** Copyright © 2026 Jijesh Puliyappottammal. All rights reserved.

---

## 🔗 Links

- **Book on Amazon KDP:** *(link to be added after publication)*
- **Author:** [Jijesh Puliyappottammal](https://www.linkedin.com/in/jijesh)

- **Issues / corrections:** Please open a GitHub issue

---

*If this repository helped your studies, please ⭐ star it — it helps other students find it.*
