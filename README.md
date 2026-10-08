#  Secure OpenVINO Prompt Injection & Threat Detector Agent

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]([https://share.streamlit.io/](https://openvino-prompt-injection-threat-detector-yy5j8htvtavlpr24enjv.streamlit.app/))
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenVINO](https://img.shields.io/badge/OpenVINO-Accelerated-purple.svg)](https://openvino.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust, production-ready AI cybersecurity agent featuring a **Dual-Layer Defense Architecture** designed to detect, filter, and block prompt injection attacks, jailbreak attempts, and malicious payloads in real time. Built with **Streamlit**, **Hugging Face Transformers**, and **Intel OpenVINO/Optimum** optimizations.

---

## Architecture & Defense Layers

To ensure comprehensive protection against sophisticated adversarial inputs, incoming user prompts pass through two sequential security gates before any agent execution:

1. **Layer 1: Regex Pattern Matching (Fast Filter)**
   * Instantly screens inputs for known adversarial signatures, system prompt override triggers (`"ignore previous instructions"`), jailbreak formats (`"act as"`, `"you are now"`), and harmful shell/SQL command fragments (`"rm -rf"`, `"drop table"`).
   * Automatically terminates sessions upon detecting explicit rule violations.

2. **Layer 2: Semantic Threat Classifier (Deep Inspection)**
   * Leverages a fine-tuned transformer pipeline (`protectai/deberta-v3-base-prompt-injection-v2`) optimized for semantic intent analysis.
   * Evaluates nuanced prompt injection patterns that bypass static keyword lists, outputting confidence scores to dynamically block adversarial requests.

---

##  Tech Stack

* **Frontend & UI:** [Streamlit](https://streamlit.io/) (Interactive web chat interface with stateful session management)
* **Core Machine Learning:** [Hugging Face Transformers](https://huggingface.co/transformers/) & PyTorch
* **Hardware Acceleration:** Intel [OpenVINO Toolkit](https://docs.openvino.ai/) and `optimum-intel`
* **Cloud Hosting:** Streamlit Community Cloud

---

##  Local Installation and Setup

git clone [https://github.com/YourUsername/Openvino-Prompt-Injection-Threat-Detector.git](https://github.com/YourUsername/Openvino-Prompt-Injection-Threat-Detector.git)
cd Openvino-Prompt-Injection-Threat-Detector

Bash: python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

##  Project Structure

```text
Openvino-Prompt-Injection-Threat-Detector/
├── app.py                # Main Streamlit application and security pipeline
├── requirements.txt      # Project dependencies and acceleration libraries
└── README.md             # Project documentation



Bash: streamlit run app.py



