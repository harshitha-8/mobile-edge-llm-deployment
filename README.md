# Mobile-Edge LLM Deployment: On-Device Inference for Field Robotics

## Abstract
This repository implements a complete pipeline for fine-tuning Large Language Models (LLMs) and deploying them onto resource-constrained edge devices (smartphones, NVIDIA Jetson). The goal is to enable **offline, low-latency natural language reasoning** for agricultural drones and ground robots operating in disconnected environments.

## Methodology
The pipeline utilizes **Unsloth** for memory-efficient fine-tuning (reducing VRAM usage by up to 60%) and **GGUF quantization** to compress models (e.g., Llama-3-8B) into 4-bit formats suitable for mobile RAM (<8GB).

## Repository Structure
- `training/`: Jupyter notebooks and configurations for LoRA fine-tuning.
- `export/`: Scripts for converting PyTorch weights to GGUF format.
- `mobile_app/`: Documentation for hosting the inference engine on Android (via Termux).
- `benchmarks/`: Latency and power consumption data collected from edge devices.

## Quick Start
1. Install dependencies: `pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"`
2. Run the training script in `training/`.
3. Export the model using `export/convert_to_gguf.py`.
4. Push the `.gguf` file to your mobile device.

## Citation
If you use this pipeline in your research, please cite [Your Name/Lab].
