---
title: Open-source USB tool unlocks Nvidia's half-speed GPU AI limiter on Windows
  — lifts GPU's FP16 math performance up to 65%, UEFI unlocker covers RTX 20, 30,
  and 40-series desktops and laptops
source_url: https://www.tomshardware.com/pc-components/gpus/open-source-usb-tool-unlocks-nvidias-half-speed-gpu-ai-limiter-on-windows-lifts-gpus-fp16-math-performance-up-to-65-percent-uefi-unlocker-covers-rtx-20-30-and-40-series-desktops-and-laptops
source_site: Tom's Hardware
source_slug: toms-hardware
description: It runs from a USB stick before Windows loads and has to run again on
  every boot.
image: https://cdn.mos.cms.futurecdn.net/u2vby2U8BuWxjdFzkUxZg9-1282-80.jpg
published: '2026-11-01T00:00:00Z'
scraped_at: '2026-11-01T16:50:11Z'
categories:
- Technology & Software
- Hardware
people:
- Shane Downing
- Tom
- Zagitta
locations: []
organisations:
- Booter
- FAQ
- GPU
- GeForce
- Get Tom's Hardware
- Google News
- Nvidia
- RTX
- Reddit
- Shane Downing
- Thunderbolt
- Tom’s Hardware
- UEFI
- Zagitta
---

![Nvidia GeForce RTX 2070 Founders Edition graphics card with two fans on a black background](https://cdn.mos.cms.futurecdn.net/u2vby2U8BuWxjdFzkUxZg9-1282-80.jpg)

A new open-source UEFI tool boots from USB and unlocks significant extra tensor performance on RTX 20, 30, and 40-series desktop and laptop GPUs, making the half-speed AI throttle hack a whole lot easier to try on Windows. No VBIOS flash or patched driver needed: the tool runs from a FAT32 stick before the Nvidia driver loads at every boot, and then voila, the developer’s own laptop RTX 4060 hit 65% higher FP16 math.

The “UEFI pre-driver NVIDIA GPU unlocker,” or nv-uefi-unlocker project, removes Nvidia’s tensor limiter using the community V67 payload with read-back verification. This tricks Nvidia’s signed Booter firmware into opening the write lock on two speed-selector registers, allowing the tensor units to run at full rate. The unlock can now run entirely from a bootable USB drive, on Windows as well as Linux, whereas previously it worked primarily through manually installed Linux modules, with Windows support only experimental. The read-back verification part makes things safer, which was a concern with the experimental builds.

![Bar chart comparing stock and unlocked tensor throughput on an RTX 4060 Ti 8GB under Windows, with FP16, BF16 and TF32 higher after the unlock and FP32 unchanged](https://cdn.mos.cms.futurecdn.net/8hKjW8J3WuVJBi5tGD2nKa-1200-80.png)

The release ships only scripts and self-built binaries, without any Nvidia firmware in the download. Instead, one of the scripts grabs Nvidia’s public 610.43.03 driver packages, verifies them, then rebuilds the firmware files locally. The project credits Zagitta’s gpu-unlock as its porting source and builds on several other community projects, including the RTX 40 fork gpu-unlock-ada and an earlier Windows EFI tool. Having one tool for the many GeForce owners on Windows should significantly open up the hack to a wider audience. Previously, it was scarier-looking, and project progression is rapid these days with AI tools.

The steps right now involve downloading the release, running that script, and then copying the rebuilt files and a BOOTX64.EFI for booting to a FAT32-formatted USB stick. The unlocker can then be run from a one-time boot menu by using the spacebar within 30 seconds for confirmation. Once complete, things are handed off to the respective OS loader.

The unlocker runs in a firmware stage before the OS loads Nvidia’s GPU driver, which means there’s no need to flash the card’s video BIOS or to modify the driver; as the FAQ puts it, the unlock doesn’t “persist through power loss.” The trade-off is running it again on every boot. The system must be booted in UEFI mode with Secure Boot either off or set to trust a self-signed EFI. For a game’s anti-cheat that requires Secure Boot, the tool “CANNOT bypass this requirement,” a developer team member relayed on Reddit. RTX 20 owners have to run a bundled script once to switch the Windows Nvidia driver into GSP firmware mode, before restarting.

Laptop GPUs were already supported by earlier projects, but here one of the developer’s own test cards is a laptop GPU, and laptop results are logged card by card. For laptops, the discrete Nvidia GPU must be powered at entry, which means dGPU-only, or MUX, mode is recommended. On Linux distributions such as Ubuntu, runtime power management can power down the GPU when idle and silently erase the unlock. The English FAQ covers workarounds for this, with instructions and guidelines for other situations.

Compatibility otherwise includes RTX 20-series support listed as “fully compatible; some models have known issues,” while RTX 30-series cards are “fully compatible,” and the tool is “fully compatible on laptops and desktops” using RTX 40-series cards. The GTX 16 is “theoretically compatible” with verification pending, but other cards, including pre-Turing, the GA100, and RTX 50-series cards, are unsupported. The project routes support by chip family, so a card being covered doesn’t mean that specific card has been tested. Cards verified by the tool’s own Windows results are listed in the table below.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

|  |  |  |
| --- | --- | --- |
| Which GeForce cards nv-uefi-unlocker has run on |  |  |
| Generation | Confirmed working on Windows | Known problems or untested |
| RTX 20 (Turing) | RTX 2070, RTX 2060 Super | RTX 2080, 2080 Ti and 2080 Super fail at boot or handoff; GTX 16 untested; needs GSP firmware mode and a restart first |
| RTX 30 (Ampere) | RTX 3080 (incl. LHR), 3060 Ti, 3060 12GB, 3080 Ti Laptop, 3070 Laptop | RTX 3050 untested; persistence on Thunderbolt eGPUs not guaranteed |
| RTX 40 (Ada Lovelace) | RTX 4090, 4080, 4070 Ti Super, 4070 Super, 4070, 4060 Ti 8GB and 16GB, 4060 Laptop, 4050 Laptop | RTX 4070 Laptop untested |
| RTX 50 (Blackwell) | None | Not supported |

Results compare each card before and after the unlock on the same test, but the tests differ from row to row, so they shouldn’t be compared across cards.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Reported Windows results with nv-uefi-unlocker |  |  |  |  |  |
| Card | Test (FP32 accumulate) | Stock (TFLOPS) | Unlocked (TFLOPS) | Gain | Who measured |
| RTX 2070 | FP16 matrix multiply | 36 | 60–63 | +67–75% | Developer |
| RTX 3060 12GB | FP16 matrix multiply, 4096 | 25.37 | 45.79 | 1.80x | Owner report |
| RTX 3070 Laptop | FP16 matrix multiply, 8192 | 35.43 | 56.04 | 1.58x | Owner report |
| RTX 4060 Laptop | FP16 matrix multiply | 29.89 | 49.33 | 1.65x | Developer |
| RTX 4080 | BF16 matrix multiply, 4096 | 100.37 | 192.18 | 1.91x | Owner report |
| RTX 4090 | FP16 matrix multiply, 4096 | 118.42 | 171.52 | 1.45x (power-limited) | Owner report |

The developer’s own desktop RTX 2070 went from about 34 TFLOPS in FP16 matrix multiply at 8192 to around 62 TFLOPS in the screenshots below.

![Windows PowerShell running a GPU stress test on an RTX 2070, reporting about 31 to 34 TFLOPS in FP16 matrix multiplication](https://cdn.mos.cms.futurecdn.net/5ykHQj7HGujeCcJUYvGrJH-1200-80.png)
![The same GPU stress test on the RTX 2070 after the unlock, reporting about 61 to 64 TFLOPS in FP16 matrix multiplication](https://cdn.mos.cms.futurecdn.net/doYzDt43RDzWyG3gz8yjCd-1200-80.png)
![Windows PowerShell running a GPU stress test on an RTX 2070, reporting about 31 to 34 TFLOPS in FP16 matrix multiplication](https://cdn.mos.cms.futurecdn.net/5ykHQj7HGujeCcJUYvGrJH-1712-80.png)
![The same GPU stress test on the RTX 2070 after the unlock, reporting about 61 to 64 TFLOPS in FP16 matrix multiplication](https://cdn.mos.cms.futurecdn.net/doYzDt43RDzWyG3gz8yjCd-1702-80.png)

Some caveats still exist, and Zagitta, whose gpu-unlock kicked off the GeForce unlocks, now says in its FAQ that “I don’t run windows and don’t plan to maintain it,” pointing Windows users to a separate port and warning to be careful with unofficial Windows installers. Results from the unlock are also contingent on power and thermal limits. The new project says it can be combined with the nvoc power-limit unlock, but warns this “can exceed factory power and thermal envelopes.” A per-card ROM hash check, which the project’s own safety rules require, isn’t built yet, and the unlock’s persistence on Thunderbolt eGPUs “is not guaranteed.”

Other cards, including the RTX 2080 and the RTX 2080 Ti, are under review. No dates are promised. The pro-card tensor feature can now be unlocked for many, though, and as simply as using a USB boot drive, which will get even easier with a boot-from-disk toggle the team says is in the works. RTX 50-series owners have to wait, for now, as the team is still trying to crack those cards, which have “a lot more security” than it anticipated.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
