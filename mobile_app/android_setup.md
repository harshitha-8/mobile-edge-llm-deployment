# Android Deployment Guide (Termux)

This guide details the steps to deploy the `.gguf` model on an Android device using Termux and `llama.cpp`.

## Prerequisites
1. Android Device with >8GB RAM (Recommended).
2. [F-Droid Store](https://f-droid.org/) installed.
3. **Termux** app installed via F-Droid.

## Installation Steps

### 1. Setup Termux Environment
Open Termux and update the repositories:
```bash
pkg update && pkg upgrade
pkg install git cmake clang build-essential
