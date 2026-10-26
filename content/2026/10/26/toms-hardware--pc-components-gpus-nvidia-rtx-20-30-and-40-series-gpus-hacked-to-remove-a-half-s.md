---
title: Nvidia RTX 20, 30, and 40-series GPUs hacked to remove a half-speed AI throttle
  — firmware exploit doubles RTX 4090's peak tensor rate, lifts RTX 3090 Ti matrix
  math up to 80%
source_url: https://www.tomshardware.com/pc-components/gpus/nvidia-rtx-20-30-and-40-series-gpus-hacked-to-remove-a-half-speed-ai-throttle-firmware-exploit-doubles-rtx-4090s-peak-tensor-rate-lifts-rtx-3090-ti-matrix-math-up-to-80-percent
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T12:52:02Z'
published: '2026-10-26T00:00:00Z'
description: Real workloads gain less than peak tensor rates, and chatbot token speeds
  stay about the same.
image: https://cdn.mos.cms.futurecdn.net/4Yvp7ck4v6d8JPBoNXVPfe-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Blackwell
- Hopper
- KohakUnlock
- Shane Downing
- Tom
- Zagitta
locations:
- WildFlash1st
organisations:
- Crypto Mine
- Defeating Stack Protection
- Dell
- GPU Secure Coprocessor
- GeForce
- Get Tom's Hardware
- Google News
- LLM
- Modders
- Nvidia
- README
- Shane Downing
- Tom’s Hardware
- Turing
- WildFlash1st
- Zenodo
---

![Nvidia GeForce RTX 4090 Founders Edition graphics card, shown at an angle with its fan and silver shroud against a black background](https://cdn.mos.cms.futurecdn.net/4Yvp7ck4v6d8JPBoNXVPfe-1920-80.jpg)

Modders have discovered a way to remove imposed half-speed AI performance limits on Nvidia RTX 20, 30, and 40-series GPUs with a firmware exploit, *VideoCardz* reports. Without the limitation, the RTX 4090 can achieve double its peak tensor rate, and matrix math can improve by up to 80% for the RTX 3090 Ti, with gains on other cards varying. Real workloads gain significantly less than the RTX 4090’s doubled peak would imply, and chatbot token speeds remain about the same, as that performance is dependent on memory bandwidth.

For all impacted GeForce generations, Nvidia imposed a limit that, per its own published specs, runs FP32-accumulate math at half each card’s FP16-accumulate rate. That does not apply to its Turing and Ampere pro cards. The unlock returns native matrix-math throughput to owners of the cards, which can speed up prompt processing and image generation.

Three separate projects offer generation unlocks, each with its own unofficial Linux module, while experimental Windows builds pursue a different approach. Card coverage varies by generation, with gpu-unlock handling Ampere and listing the GA102/GA103/GA104/GA106 series IDs. An Ada fork, gpu-unlock-ada, covers the RTX 4090 and, experimentally, the 4090 D, 4070 Ti Super, and the 4060 Ti 16GB. The turing-unlock project, adapted from gpu-unlock, works with the RTX 2080 Ti. See Table 1 for a breakdown.

|  |  |  |  |
| --- | --- | --- | --- |
| Which GeForce cards each unlock covers |  |  |  |
| Generation | Project | Cards with reported results | Experimental or untested |
| RTX 20 (Turing) | turing-unlock | RTX 2080 Ti (22GB memory-modded cards) | Other Turing GPUs, added untested; FP16 only, since Turing lacks BF16 support |
| RTX 30 (Ampere) | gpu-unlock | RTX 3090 Ti, 3090, 3080 10GB, 3080 20GB (memory-modded), 3070, 3060 12GB | RTX 3070 Ti and GA103 cards untested; one RTX 3080 Ti 20GB OEM card stays at half rate |
| RTX 40 (Ada Lovelace) | gpu-unlock-ada | RTX 4090 | RTX 4090 D, 4070 Ti Super, 4060 Ti 16GB (experimental, one card each) |
| RTX 50 (Blackwell) | None | — | Not supported; gpu-unlock’s developer calls it out of scope |

## How much faster the cards get

The peak doubling is for tensor rates, with the Ada fork developer’s RTX 4090 moving from 165.6 to 331.6 TFLOPS on FP16 and 165.5 to 330.6 TFLOPS on BF16. The gpu-unlock-ada README states that, in one independent owner’s matrix-multiply benchmark, cuBLAS GEMM medians only saw improvements of 12–34% and up to 20%, respectively. A separate data point, for an RTX 4070 Ti on Windows, saw larger matrix-multiply gains of +80.1% and +76.4%, the difference possibly caused by power limits.

In the matrix-multiply benchmark, a tested RTX 3090 Ti scored +35% for FP16, +80% for BF16, and +94% for TF32, based on a user’s test with a modified Nvidia driver. The gpu-unlock README lists BF16 matrix-multiply gains from user reports of +25–67% for the RTX 3090, +70–73% for the 3080 10GB, +56–59% for a memory-modded 20GB version, +73–81% for the 3070, and around +80% for the 3060 12GB, though it notes they are not directly comparable. The power limit “matters a lot”: the lowest figure, +25%, came from cards capped at 225 W. For Ampere, LLM prefill improved 14–36%, with diffusion and FlashAttention speeding up, but LLM decode and INT8 stayed “about the same.”

An RTX 2080 Ti with a 22GB memory mod, a Dell OEM card limited to 250 W, saw FP16 matrix-multiply improvements of +36% to +64% depending on size; BF16 is unaffected, since Turing has no BF16 hardware. A user’s variant of the card at 260 W saw a +59% improvement. A separate project, KohakUnlock, on a Leadtek 2080 Ti 22GB saw an 85% improvement on an instruction rate test, with a best matrix-multiply median of +53% against a second, locked card of the same model.

There is “not a claim of a 2× application/game speedup,” says KohakUnlock’s README. See Table 2 for a rundown of the numbers for all three generations. The turing-unlock README notes that the mod “may damage your hardware,” while KohakUnlock adds that it “can hang a GPU or host, prevent boot, corrupt data, or damage hardware,” so caution is advised.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

|  |  |  |  |
| --- | --- | --- | --- |
| Matrix-multiply benchmark gains, unlocked vs. stock |  |  |  |
| Card | Precision | Gain | Tested by |
| RTX 4090 | FP16 / BF16 | +12–34% / up to +20% | One owner, Linux, 450 W |
| RTX 4070 Ti (MSI) | FP16 / BF16 | +80.1% / +76.4% | Separate Windows port, one card |
| RTX 3090 Ti | FP16 / BF16 / TF32 | +35% / +80% / +94% | One user, modified Nvidia driver, 450 W |
| RTX 3090 | BF16 | +25–67% | User reports; lowest at a 225 W cap |
| RTX 3080 10GB | BF16 | +70–73% | User report |
| RTX 3080 20GB mod | BF16 | +56–59% | User reports |
| RTX 3070 | BF16 | +73–81% | User reports |
| RTX 3060 12GB | BF16 | About +80% | User reports |
| RTX 2080 Ti 22GB mod (Dell) | FP16 | +36–64% | turing-unlock developer, 250 W, by matrix size |
| RTX 2080 Ti 22GB mod | FP16 | +59% | One user, 260 W |
| RTX 2080 Ti 22GB mod (Leadtek) | FP16 | +53% | KohakUnlock; best median vs. a locked card |
| RTX 2080 Ti 11GB (ASUS, stock) | FP16 | +77% | haohervchb pre-boot loader |

## How the exploit works

The explainer for gpu-unlock states that the rate limits are in two “speed selector” registers that the host driver can’t write, but Nvidia’s signed SEC2 “Booter” firmware has a stack buffer overflow which can be exploited to run code in “heavy secure” mode. This was discovered after Nvidia published a debug Booter encrypted with a known public test key. A single 4-byte write with the V67 payload opens the privilege mask so the host can set the full rate, and the module then resets the card before Nvidia’s driver binds it.

The underlying bug is described in Jon Pry’s “A Canary in the Crypto Mine: Defeating Stack Protection in a GPU Secure Coprocessor,” published on Zenodo in June. The stack overflow was found on the CMP 170HX in the Heavy Secure Falcon, and the V67 constants come from WildFlash1st/cmp90hx-unlock. The pre-driver timing gpu-unlock uses appear to come from WildFlash1st’s separate Windows EFI bootloader, cmp90hx-unlock-for-windows, while the best-known use of the exploit is the CMP Unlocker for the CMP 170HX. Zagitta, the maintainer of gpu-unlock, said on *Hacker News* that the project is their work but “the exploits … aren’t my ideas by any means” and that the unlock “just flips the 2 bits” needed.

Zagitta said that RTX 40 support is in progress and that forks are already unlocking those cards. Zagitta added that Hopper and Blackwell cards are “out of scope for this approach” at least.

The Ada fork says other boards “remain unverified” and that shared firmware “does not establish support for untested cards.” The turing-unlock project, likewise, has a list of untested Turing IDs. Gaps remain for GA103 and most Ada and Turing cards. None of the projects contains a roadmap, but data is being gathered, as gpu-unlock is asking GPU owners for compatibility reports.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
