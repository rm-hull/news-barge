---
title: One gigabyte of Wikipedia losslessly compressed to 105.39MB with self-learning
  AI transformer model — 'tufazip' needs two Nvidia B200 GPUs and about a week to
  compress or decompress
source_url: https://www.tomshardware.com/uk/tech-industry/artificial-intelligence/one-gigabyte-of-wikipedia-losslessly-compressed-to-105-39mb-with-self-learning-ai-transformer-model-tufazip-needs-two-nvidia-b200-gpus-and-about-a-week-to-compress-or-decompress
source_site: Tom's Hardware
source_slug: toms-hardware
description: Tufa Labs’ tufazip compresses 1GB of Wikipedia to 105.39MB with a 163M-parameter
  Transformer as its only predictor, on two Nvidia B200s.
image: https://cdn.mos.cms.futurecdn.net/iPmrEtNmpAx79TNibeBMXb-1920-80.jpg
published: '2026-11-21T00:00:00Z'
scraped_at: '2026-11-21T19:07:54Z'
categories:
- Technology & Software
- Hardware
- Science
people:
- Shane Downing
- Tom
locations: []
organisations:
- Get Tom's Hardware
- Google News
- Shane Downing
- Tom’s Hardware
- Tufa Labs
- Wikipedia
---

![Nvidia Blackwell GPU package on a black background](https://cdn.mos.cms.futurecdn.net/iPmrEtNmpAx79TNibeBMXb-1920-80.jpg)

Tufa Labs’ tufazip has compressed 1GB of information from Wikipedia into just 105MB of space, losslessly, without using any hand-built models, according to a research post. The method uses a 163-million-parameter Transformer model as a predictor instead, and similar compression or decompression would take two Nvidia B200 GPUs about a week to manage. It’s the smallest result on the Large Text Compression Benchmark from any entry that uses a neural network as its only predictor.

> We shrank 1 GB of Wikipedia to 105.39 MB, losslessly. Introducing tufazip: the best entry on the Large Text Compression Benchmark using a neural network as its sole predictor. Everything above it mixes a transformer with hand-built models.November 19, 2026

Researcher Tommy He built tufazip, and the full package, at 105.39MB after optimization, includes a small, 4.33MB pre-trained starter model — stored at low precision, or quantized, to save space — that’s needed to unpack the file. The full model is a 12-layer Transformer, which means there are 12 stages for each guess to go through. The starter stores just two already-trained stages, copying them back and forth to fill all 12 once the full model spins up in memory; each copy keeps learning on its own.

![Tufa Labs chart comparing compressed size against transferred model size for enwik9, with Cycle2 at 105.39 MB total, under the 105.98 MB online baseline, and L6 at 110.12 MB.](https://cdn.mos.cms.futurecdn.net/TvqESA7Fr9cmdzMsoTswMA-1200-80.png)

This doesn’t work like a traditional chatbot or cloud AI but is, rather, a self-contained language model that learns on the fly. Notable here is that this compression is lossless, which means there’s no risk of any data being lost in the process. This means that predictor updates must be “fully deterministic.”

Training happens in two stages. The starter, a 34-million-parameter model, is trained offline, before any compression begins. Then, the full model begins to learn online, by predicting each token and training on it, with the unpacking side repeating the same steps, with the model itself being rebuilt alongside the text. For this reason, the total size must include, besides the compressed text, only the unpacking program and the files it needs, including the starter, but not the full trained model.

There is no traditional, hand-built compression model that assists, setting it apart, Tufa Labs says, from all 12 entries that now rank above it on the benchmark, which mix a Transformer with hand-built models. Its first, online-only version ranked second when submitted in early September; the 105.39MB version was 13th as of the benchmark’s Nov. 19 update. Emphasis should be placed on this being a text-only benchmark, for those imagining media files.

While this sounds more exciting than, say, WinRAR, it’s for research purposes and not a product, and that’s underlined by what you’d need to actually run it. Currently, two Nvidia B200 GPUs — plus two Intel Xeon Platinum 8570 CPUs in the test machine — would need 631,548 seconds to compress and 645,748 seconds to decompress the 105.39MB version, or about 7.3 and 7.5 days, respectively, not counting the starter’s offline training.

The first version, which learned entirely online and came in at 105.98MB, took 647,595 and 630,136 seconds. Its GPUs peaked at 43.37 GiB of VRAM between them, and total memory use, GPUs included, peaked at roughly 68,525 MiB during compression and 73,748 MiB during decompression.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| tufazip vs. other enwik9 compressors on the Large Text Compression Benchmark |  |  |  |  |
| Compressor | Total size (MB) | Hardware | Compress | Decompress |
| cmix-neif 2.0 | 89.35 | AMD Epyc 7B13, 4 cores | 49.2 hours | 49.3 hours |
| tufazip v2 | 105.39 | Two Nvidia B200s | 7.3 days (excl. offline training) | 7.5 days |
| DNA-4 | 105.55 | Nvidia RTX 4090 | 19.8 hours (incl. training) | 2.6 hours |
| NNCP v3.2 | 107.26 | Nvidia RTX 3090 | 67.2 hours | 66.3 hours |

The experiment is fundamentally interesting because it shows, for example, that a smaller vocabulary can actually help: a 4K-word tokenizer beats both 8K and 16K. Giving Wikipedia’s XML markup its own dedicated tokens made the compression worse. Bigger isn’t always better, and that goes for model size, too, as a 267-million-parameter model did slightly worse than a 188-million-parameter model on this data set. With a smaller, 100MB version of the file, gains leveled off at about 77 million parameters. A run started from a bigger, six-layer offline model predicted better, with just a 99.17MB payload, but its chunkier weights made the total file larger than the online-only run.

Improving compression can be costly, as widening the window of already-processed text used for extra training, from 15 to 35 million tokens, only cut the payload 1.21% at the cost of 40% more compute. The key takeaways are that optimization isn’t always as simple as throwing more at the problem, and that trade-offs can be more expensive than expected. He frames that six-layer trade-off as the next research question: how much predictive quality a smaller model can keep, which makes the vanishing point a balance between predictive quality and model size for this benchmark.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
