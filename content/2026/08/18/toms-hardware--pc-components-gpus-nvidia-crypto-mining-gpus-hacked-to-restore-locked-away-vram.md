---
title: Nvidia crypto mining GPUs hacked to restore locked-away VRAM — software mod
  unlocks 64GB of VRAM on $250 CMP 170HX
source_url: https://www.tomshardware.com/pc-components/gpus/nvidia-crypto-mining-gpus-hacked-to-restore-locked-away-vram-in-order-to-feed-ai-boom-software-mod-unlocks-64gb-of-vram-on-usd250-cmp-170hx
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-18T13:04:32Z'
published: '2026-08-18T00:00:00Z'
description: The CMP 170HX has quickly gone from crypto trash to AI treasure.
image: https://cdn.mos.cms.futurecdn.net/QDZdfYqJbKd5P6QKeMwVEk-2560-80.jpg
---

![GPUs in a crypto mining farm](https://cdn.mos.cms.futurecdn.net/QDZdfYqJbKd5P6QKeMwVEk.jpg) 

Now that the best graphics cards are worth a fortune for both gamers and AI enthusiasts, modders have resorted to hacking Nvidia’s older Cryptocurrency Mining Processor (CMP) series, originally released five years ago, as a way to overcome the ongoing memory shortage and ludicrous prices. CMP Unlocker, a completely software-based solution, has restored the previously locked-away memory on the CMP 170HX, boosting its memory capacity by up to 8X — from just 8GB to a massive 64GB, and from 10GB to 40GB.

 ![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d.png) 


To truly understand how the hack works, you need to dissect the CMP 170HX. The CMP 170HX is the flagship SKU in Nvidia's CMP series and leverages the GA100 (Ampere) silicon. It is the same 7nm die that powers the more expensive A100 accelerator. Unlike other Nvidia silicon with separate soldered memory chips, the GA100 itself is a monolithic chip with on-package memory. That means the total amount of memory is physically present on all GA100 silicon, so it comes down to how many memory stacks are active.

The GA100 silicon features a total of six HBM2e memory stacks. Depending on the SKU Nvidia is aiming for, it could have five or six memory stacks enabled. The chipmaker carves the CMP 170HX from defective or binned GA100 silicon that did not meet the stringent quality requirements for the enterprise-grade A100. Nvidia officially sold the CMP 170HX in 8GB and 10GB variants. All the chipmaker did was disable the additional memory through firmware, along with other limitations, such as nerfing compute performance and PCIe interface speeds.

Nvidia's approach is somewhat reminiscent of the old AMD Phenom II and Athlon II days, where some models shipped with disabled cores that could sometimes be unlocked through BIOS tweaks. Similarly, the CMP 170HX 8GB and 10GB models can potentially be unlocked to access their full memory capacity of 64GB and 80GB, respectively, though only 40GB is confirmed to be working from user feedback. As detailed in "A Canary in the Crypto Mine: Defeating Stack Protection in a GPU Secure Coprocessor," Jon Pry's research paper provides the technical blueprint for bypassing Nvidia’s Falcon security microprocessor, which tools like CMP Unlocked are based on.

One of the most remarkable aspects of this exploit is that it is entirely software-based and requires no physical modifications to the CMP 170HX. It sounds like a joke, but you are literally downloading more memory for your graphics card. It’s important to note, however, that the amount of memory you can successfully unlock and maintain stability will vary. The issue is that there is no way to know whether the locked-away memory is fully functional because Nvidia did so for product segmentation, or whether the chipmaker deactivated it due to physical defects. It's a similar situation to another repurposed crypto device, AMD's BC-250, that we recently tested.

Beyond unlocking the hidden memory, the software exploit can also restore processing power to the CMP 170HX’s Streaming Multiprocessors (SMs), which increases its computational performance. Another notable benefit is the upgrade to a faster PCIe interface speed. The CMP 170HX can now operate at PCIe 2.0 x4 speeds, a significant upgrade from its original restriction to PCIe 1.0 x4. There is still untapped performance, though. Nvidia implemented hard restrictions on the CMP 170HX’s connectivity by limiting the accelerator to just four PCIe lanes and physically omitting 12 capacitors from the PCB. If you solder the missing capacitors to the PCB, it could unlock full PCIe x16 bandwidth and enable the accelerator's maximum throughput, though we haven't seen that in action.

The CMP 170HX launched with a hefty price tag of $4,300 at the height of the cryptocurrency mining boom. Nowadays, they used to sell for around $250 on eBay. However, when word of the exploit got out, they immediately jumped to over $1,000, a 4X increase in market value. Nvidia’s A100, offered in 40GB and 80GB PCIe variants, starts at around $3,500 and $11,500, respectively. The CMP 170HX is attractive for AI users because it costs a fraction of the A100 but can offer the same memory capacity, though the silicon lottery is not always generous. Regardless, Nvidia’s Ampere architecture is now two generations old. Even with added memory capacity, it cannot match the raw computational performance or efficiency of Hopper or Blackwell.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zhiye Liu](https://cdn.mos.cms.futurecdn.net/HhmwL5w9ggUtLCPfqGjTi4.jpg)

Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.

- 
that's why , as a miner I don't buy Nvidia GPU , not since the LHR story , if they accept my money for a piece of hardware they don't get to tell me what I can or cannot do with it , I'm not a tenant I'm an owner I'm not a Apple user , I'm a miner and Nvidia can shove their CMP modules where the sun don't shineReply
- 
Reply
 Come come, this is a happy occasion! People are downloading more RAM on cheap used hardware and you're complaining!re3eyul said:that's why , as a miner I don't buy Nvidia GPU , not since the LHR story , if they accept my money for a piece of hardware they don't get to tell me what I can or cannot do with it , I'm not a tenant I'm an owner I'm not a Apple user , I'm a miner and Nvidia can shove their CMP modules where the sun don't shine
 
Another angle from this is that there could be some legitimately defective components on any card you try this on. I don't know whether it's the memory or controllers or something else.
