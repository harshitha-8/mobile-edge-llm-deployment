# Quantization Analysis Log

## Objective
To determine the optimal quantization level for deploying Llama-3-8B on a Pixel 7 Pro (12GB RAM) and standard Android devices (8GB RAM).

## Methods Tested
| Method | Description | Size (GB) | Perplexity Loss | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **f16** | Full Precision (half) | ~16.0 GB | 0.0% | ❌ Too large for mobile RAM |
| **q8_0** | 8-bit Integer | ~8.5 GB | <0.1% | ⚠️ Good for Jetson Orin, risky for phones |
| **q4_k_m** | 4-bit Medium | ~4.8 GB | ~1.5% | ✅ **Selected Standard** |
| **q2_k** | 2-bit | ~2.6 GB | >10.0% | ❌ Too incoherent for reasoning |

## Conclusion
We selected **q4_k_m** for the final deployment. It fits comfortably within the 8GB RAM envelope of standard field tablets while retaining sufficient reasoning capability for robotic command parsing.
