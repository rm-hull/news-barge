---
title: Voltage glitch unlocks 80GB on Nvidia's CMP 170HX, but 'faster than an A100'
  rests on a single benchmark
source_url: https://www.techradar.com/pro/voltage-glitch-unlocks-80gb-on-nvidias-cmp-170hx-but-faster-than-an-a100-rests-on-a-single-benchmark
source_site: TechRadar UK
source_slug: techradar-uk
description: Nvidia built the CMP 170HX to be a worse A100
image: https://cdn.mos.cms.futurecdn.net/QphU2iRAAXWSDt3nL5UNhg-1920-80.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-19T02:31:26Z'
categories:
- Technology & Software
people:
- Jon Pry
- Kate
- Ken Ashe
- Rowhammer
locations:
- Arizona State
- Ethereum
organisations:
- A100
- AI
- AMD
- Amogh Munikote
- Astra
- CMP
- ECC
- GeForce
- HBM
- MIG
- Multi-Instance GPU
- NVLink
- Nvidia GPU
- OpenAI
- PCIe Gen2
- TechRadar Pro
- Tesla
---

![Nvidia GPU hardware](https://cdn.mos.cms.futurecdn.net/QphU2iRAAXWSDt3nL5UNhg-1920-80.jpg)

* **Researcher uses voltage fault injection on Nvidia's GA100 die to blow normally locked fuses and re-enable memory and compute on the crippled CMP 170HX mining card**
* **An 8GB card can be pushed to a full 80GB of HBM and 120 to 126 working SMs, more than the 108 Nvidia currently enables on a retail A100**
* **The "faster than an A100" claim, however, rests on a single FP16 benchmark and leaves tensor performance, ECC, NVLink, and MIG untested or incomplete**

Nvidia spent the better part of a decade teaching its silicon to keep secrets from its own owners, but a new piece of hardware research argues that, on at least one chip, those secrets were only ever a power glitch away.

Writing on her personal blog, a researcher known as Kate published a voltage fault injection attack on Nvidia's GA100, the Ampere die at the heart of the A100 data center accelerator.

Her claim is blunt but one backed by proof: by disrupting the chip's power delivery at the right moment during boot, she can write fuses that Nvidia designed to be unwritable, and in doing so re-enable the memory and compute the company switched off at the factory, resulting in a card that behaves as an 80GB A100, assembled from a mining accelerator that was never meant to be anything of that sort.

## The card Nvidia built to be worse than it is

The subject of the work is the CMP 170HX, a passively cooled mining card Nvidia introduced in 2021 to steer harvested GA100 dies toward Ethereum and away from the GeForce stock gamers were fighting over as GPU prices skyrocketed because of their potential for cryptomining.

The company was explicit about the segmentation at the time, pairing the CMP line with a hash-rate limiter on the RTX 3060 under the banner "GeForce Is Made for Gaming, CMP Is Made to Mine." The 170HX shipped with 8GB or 10GB of HBM2e exposed to software, 70 streaming multiprocessors, a PCIe Gen1 link, and no video output.

Underneath, it carries the same die that powers accelerators costing many thousands of dollars, and a nominal 8GB card physically holds closer to 80GB of HBM, with firmware and fuses doing the hiding.

That gap is why a five-year-old mining card has become an unlikely object of desire. The industry is in the grip of a memory shortage severe enough that HBM is effectively sold out, so hardware that hides usable high-bandwidth memory behind a software lock is suddenly worth prying open.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This isn't the first attempt to do so: a community project called cmpunlocker, built on earlier work by Amogh Munikote and others, had already shown that patched drivers could expose 64GB on the 8GB card and restore compute, though it stopped at PCIe Gen2 and left NVLink, ECC and Multi-Instance GPU partitioning untouched. Kate's contribution goes past the point where a pure software mod runs out of room to eke out more from the accelerator.

## A voltage glitch that writes the unwritable

The mechanism is voltage fault injection, a well-worn technique in hardware security rather than a niche one. In a nutshell, a small microcontroller board taps the signal line between the GPU and its voltage regulator and briefly disturbs the supply while the chip is starting up, nudging the fuse controller into a state where normally locked fuses can be burned.

This is not exclusive to Nvidia's hardware; the same class of attack was used to bypass AMD's secure processor and jailbreak the AMD-based computers inside Tesla's cars to switch on paid features for free. Kate reports that she had OpenAI's GPT-6 Astra design the glitching board. It's interesting to consider: an AI model helped pry open the very class of accelerator that trains AI models.

## Faster than an A100? Based on one benchmark

In Kate's testing, an unlocked card reached about 85.9 TFLOP/s of FP16 fused-multiply-add throughput against roughly 72.5 for a retail A100, a gain of about 1.2x. The reason is straightforward. A production A100 enables 108 of the die's 128 SMs for yield, whereas Kate's unlocked cards report between 120 and 126, so a healthy specimen simply has more working silicon than Nvidia ever ships.

That number, however, is non-tensor FP16 throughput from a single OpenCL benchmark. It says nothing about the tensor-core performance, the ECC, the NVLink, and the MIG partitioning that actually define what an A100 is for inside a data center, and Kate marks ECC, MIG, and the video engines as untested.

NVLink also isn't fully working, requiring further board surgery she hasn't completed, even though PCIe can be pushed to Gen4 only with additional hardware modification. A card that wins one synthetic test win is therefore arguably not the same object as a card that can drop into an A100's slot and do its job. The honest description is a GA100 running close to its native potential, which is remarkable to recover from a mining castoff that many wrote off years ago, but not a $20,000 accelerator cloned for pocket change.

## A flawed design?

The more durable finding is interestingly not the free compute: it is the flaw underneath it. Kate's argument is that a secure fuse scheme should only let a blown fuse make a chip more restricted, because a fuse cannot be unblown once set.

On the GA100, she says, the opposite can be true, and an operator can "relax restrictions by blowing more fuses." She reports disclosing the vulnerability to Nvidia's product security team before publishing, and going public only after another researcher independently found the same issue. Nvidia has not commented publicly, and for the cards already in the field there is little it can do, since the problem sits in silicon that has long since shipped.

That places the work within a wider run of Ampere-era security research rather than on its own. Academic teams have spent the past two years demonstrating Rowhammer bit flips on Nvidia GPUs and, more recently, defeating the ECC that Nvidia had recommended as the fix.

Kate's own write-up builds directly on Arizona State researcher Jon Pry's June 2026 paper "A Canary in the Crypto Mine," which defeated stack protection in the GPU's security coprocessor. The common thread is a generation of Nvidia silicon whose protections keep proving softer than the marketing implied.

For anyone reading this as a cheap route to an AI box, the caveats matter more than the TFLOPS. Kate reports that unlocking a single card takes somewhere between one and 48 hours, and that of ten cards she examined, one had only 64GB of healthy memory rather than the full 80.

The procedure needs physical rework and per-card tuning, and the fuse burns are permanent, so a mistake isn't something you can walk back. One analyst, Ken Ashe, captured this well, calling the work "silicon archaeology with a soldering iron" and noting that one success is a hack while ten repeatable cards would be infrastructure.

The economics are softer than they look, too. The street prices that make the comparison dramatic- a mining card at a couple of thousand dollars against an A100 near $20,000- come from volatile secondhand listings rather than any stable supply, and they have already climbed as word spread. The 170HX traded for as little as $250 before the first software unlock, then surged past $1,000 once buyers realized what was inside.

What the research really demonstrates here is less a bargain than a warning. In a market this starved of memory, the hardware people already own may be concealing far more than its vendor cares to admit, and the locks keeping it hidden are not as solid as they appear, especially when it comes to last-generation hardware that repurposed higher-end die and memory configurations into lower-end packages regularly.
