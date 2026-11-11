---
title: Kora is a Linux OS that splits AI models across the CPU, GPU, and NPU
source_url: https://www.tomshardware.com/uk/software/linux/cyanogen-co-founder-unveils-kora-a-linux-os-that-splits-ai-models-across-the-cpu-gpu-and-npu-snapdragon-x2-elite-and-hexagon-npu-get-full-support-first
source_site: Tom's Hardware
source_slug: toms-hardware
description: Kora, a Linux OS that offers built-in AI models and agents for local
  agentic work, is coming to PCs in 2027, including Snapdragon X2 Elite systems.
image: https://cdn.mos.cms.futurecdn.net/rJ9DVssjvfgAJwQazxQhbm-2496-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:36:53Z'
categories:
- Technology & Software
- Hardware
people:
- Kirt McMaster
- Kora
- Shane Downing
locations:
- Cortex
- GameOS
- Playtron
organisations:
- AMD NPU
- AMD NPUs
- CPU
- Cortex
- Cyanogen
- FastRPC
- Follow Tom’s
- GPU
- GameFrame
- Gemma
- Get Tom's Hardware
- Google News
- Hexagon NPU
- Humain OS
- IPEX
- Intel NPU
- KORA
- Kora Systems Inc
- LLMs
- ONNX Runtime
- OpenVINO
- PyTorch
- QAIRT
- QNN
- Qualcomm Hexagon
- Qualcomm Hexagon NPU
- Ryzen AI
- Saudi AI
- Shane Downing
- Snapdragon X2 Elite NPU
- Tom’s Hardware
- llama.cpp
---

![An illustration of a developer seen from behind at a three-monitor desk, wearing a cap with KORA’s emblem.](https://cdn.mos.cms.futurecdn.net/rJ9DVssjvfgAJwQazxQhbm-1920-80.jpg)

A team led by Cyanogen co-founder Kirt McMaster has unveiled Kora, a new Linux desktop OS with integrated AI models and agents that can split workloads across CPU, GPU, and NPU resources, as well as other machines on the same local network. We reached out to the firm for more info.

Kora, the first product from Kora Systems Inc., previously Playtron, carries the tagline “The Operating System for Intelligence” and has its own Cortex “hybrid inference engine” technology, which is not open source and is optimized for local models. The OS, built “from the kernel to the shell,” runs local models by default and cloud models when needed, and is expected to arrive on PCs in 2027.

The desktop follows the AI-focused motif with “neural workspaces” and a “neural file system,” which refer to sandboxed workspaces and files indexed by semantic meaning. Kora has three operating modes: “Work," "Create," and "Play." That last base is covered by GameFrame, which descends from Playtron’s GameOS. Humain OS, which Kora is developing with Saudi AI company Humain, is the enterprise variant of this OS.

Currently, the only NPU named in the release material is the Hexagon NPU found in the Snapdragon X2 Elite, which Qualcomm pegs at 80 TOPS. On the X2 Elite, Cortex can schedule AI workloads across the CPU, GPU, and NPU, as well as other systems on the local network, which could be a novel capability if it works beyond the Qualcomm hardware.

McMaster told *Tom’s Hardware* that the Snapdragon X2 Elite NPU runs Google's Gemma 4 26B model at 25 tokens per second for decode. Intel and AMD NPU support is in the works, but according to the developer, neither NPU will be used for LLMs, as GPUs are “just better for LLM workloads on x64.”

Each NPU vendor has its own software stack, or runtime, and prefers that models are compiled in its own format: Qualcomm with QAIRT/QNN, Intel with OpenVINO, and AMD with Ryzen AI software. The press kit doesn't identify support for any Intel or AMD chip, NPU runtime, model format, quantization, or speed figures for those platforms.

Our earlier Windows testing showed the same kind of divide: Snapdragon reached its NPU through the QNN provider under ONNX Runtime, while Intel’s work ran through IPEX, its extension for PyTorch, on the GPU because it was faster than the NPU.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

When asked about cross-vendor support, McMaster reiterated that “only Hexagon on Snapdragon X2 Elite is supported today.” Intel NPU support is planned, with “conversations underway,” though McMaster later clarified that neither Intel’s nor AMD’s NPU will be used for LLMs. On AMD’s Ryzen AI chips, Kora will likely use the NPU for embedding and speech-recognition models through ONNX.  
As for what drives the Qualcomm Hexagon NPU, McMaster said Kora uses the “llama.cpp Hexagon backend” and “the upstream FastRPC driver.” That suggests the operating system reaches the NPU through the open-source llama.cpp project, not Qualcomm’s own QAIRT/QNN runtime, by way of the FastRPC driver in the mainline kernel.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Kora NPU support by vendor, per the company |  |  |  |  |
| NPU | Vendor’s own framework | Status in Kora | Runtime KORA uses | What it runs |
| Qualcomm Hexagon (Snapdragon X2 Elite) | QAIRT/QNN | Supported today | llama.cpp’s Hexagon backend | Language models; KORA cites Gemma 4 26B at 25 tokens per second |
| AMD XDNA 2 (Ryzen AI) | Ryzen AI software | Planned for launch | ONNX | Likely embedding and speech-recognition models; not language models |
| Intel NPUs | OpenVINO | Planned, “conversations underway” | Not stated | Not language models |

When asked about model formats, McMaster said, “we predominantly support GGUF,” llama.cpp’s model file format, and that Lemma, the inference engine inside Cortex, “can split model layers across processors as needed.” Lemma is built on llama.cpp, whisper.cpp, stable-diffusion.cpp, and ONNX. McMaster says that which runtime is used depends on the model's requirements, and more runtimes will be added down the line.

For today, llama.cpp has a Hexagon backend for Snapdragon and an OpenVINO backend for Intel CPUs, GPUs, and NPUs, although the latter is still marked “In Progress,” and no AMD NPU backend, which would explain why AMD goes through ONNX. AMD NPUs can run LLMs on Linux through the separate Lemonade 10.0 stack with FastFlowLM, as reported by *Phoronix* in March, though that isn’t the route Kora has chosen.

Beyond NPU stacks, those hoping to run Kora will need to be mindful of their system's available memory. The Gemma 4 26B model Kora uses, which Google lists as Gemma 4 26B A4B, needs about 14.4GB of memory to load its weights at 4-bit (Q4\_0) quantization, by Google’s estimate, before any context window, while third-party listings put the download for the Q4\_K\_M file Kora uses at about 16–17GB. The model only activates about 4 billion of its 26 billion parameters per token but still needs to be fully loaded into memory.

McMaster said that with the model, the X2 Elite reaches “25 TPS decode throughput and 550 TPS prefill throughput,” or tokens per second, running “entirely on the Hexagon NPU with 32K context.” A dense model, rather than a mixture-of-experts, would be far slower. Not given are the RAM configuration or the specific X2 Elite chip.

On memory, McMaster said that “we recommend 64GB because it gives you access to better models,” but that is not a firm requirement. The company projects that “about 70 percent of the model calls it manages will run locally in 2027.”

Kora says its enterprise-focused Humain OS is due first and will be “commercially available in 2027,” on OEM PCs using the Snapdragon X2 Elite. Kora will follow "later in 2027.”

McMaster says that “Kora will be posted on our site and downloadable for anyone to install.” Included will be a list of recommended configurations, “but it should be installable on most modern PCs.” Exact pricing and the overall business model will be shared closer to the date of availability.  
*Edit: 11/11/2026 9:06am PT: Added further follow-up details provided by the maker.*



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
