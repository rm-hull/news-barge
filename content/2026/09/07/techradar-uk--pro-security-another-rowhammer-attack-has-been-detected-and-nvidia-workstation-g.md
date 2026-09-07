---
title: Another Rowhammer attack has been detected, and Nvidia workstation GPUs are
  firmly in the firing line
source_url: https://www.techradar.com/pro/security/another-rowhammer-attack-has-been-detected-and-nvidia-workstation-gpus-are-firmly-in-the-firing-line
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-07T19:53:56Z'
published: '2026-09-07T00:00:00Z'
description: Nvidia spent a year telling people ECC was the answer to GPU Rowhammer.
  GPUThor tells another story, however
image: https://cdn.mos.cms.futurecdn.net/D9pZcgdPinp5ty7pPDjKeY-1920-80.png
---

![Nvidia](https://cdn.mos.cms.futurecdn.net/D9pZcgdPinp5ty7pPDjKeY.png) 

- **GPUThor is the first Rowhammer attack to defeat ECC on Nvidia GPUs and reach a root shell on the host**
- **It affects four Ampere workstation cards with GDDR6 memory, the RTX A4000, A4500, A5000 and A6000**
- **Non-uniform hammering, enabled by defeating GPU memory coalescing and finding that Target Row Refresh (TRR) mitigations fire once every 72 refresh intervals, delivers effectively 6.6 times the hammering intensity of prior attacks**

Four researchers at the University of Toronto have disclosed GPUThor, a Rowhammer technique that breaks the error correction Nvidia has spent the past year recommending as the defense against exactly this class of attack.

Chris S. Lin, Joyce Qu, Aditya Rajeev and Gururaj Saileshwar are expected to present the paper outlining their approach and subsequent findings at ACM CCS 2026.

The attacks target Ampere-generation workstation cards with GDDR6 memory, specifically the RTX A4000, A4500, A5000 and A6000, and it turns an unprivileged CUDA program into a root shell on the host.

## An attack that matters much more than its predecessors

Rowhammer works by repeatedly activating a DRAM row until charge leaks from cells in the physically adjacent rows and flips their bits. The attacker never touches the victim's data directly, making it an excellent precursor to tampering, sandbox escape, and privilege escalation, among other things.

This approach is possible despite an in-chip countermeasure called TRR that accompanies ECC-enabled chips on these GPUs. TRR aims to prevent Rowhammer attacks by tracking how frequently specific memory rows are activated and automatically refreshing adjacent rows before a malicious bit flip can occur.

This approach works well on paper and, when Rowhammer attacks hammer uniformly, offers decent protection. The problem arises when approaches such as GPUThor use non-uniform hammering, which is much more likely to succeed. Non-uniform hammering is not exactly new, having already succeeded on the CPU side of the spectrum thanks to the well-documented Blacksmith attack vector.

GPUThor is the third attack from broadly the same group in eighteen months, following GPUHammer in 2025 and GPUBreach earlier this year, and it matters because the previous two stopped working the moment a user typed the command to enable ECC.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

ECC was essentially Nvidia's go-to response to reported Rowhammer attacks, but it may no longer be a solution in its current state. By hammering non-uniformly, the researchers opened another attack vector for Nvidia's Ampere-based GPUs, which are overwhelmingly affected by the technique.

With ECC disabled, GPUThor produced 72,000 to 377,000 bit flips per gigabyte across four Ampere-based cards, with Nvidia's A5000 being reported as the most vulnerable. That approaches the roughly 550,000 flips per gigabyte that Blacksmith achieves on DDR4, which is cause for concern: GPU Rowhammer is now in the same league as CPU Rowhammer.

When enabled, the researchers said ECC protectors reduced, but did not completely mitigate, the issue: they delivered double-bit errors and 2 triple-bit errors that the technique 'fixed' by choosing the wrong value.

On an RTX A6000 with ECC enabled, the GPUThor technique forces one GPU reset every 2 hours, killing all running processes on the GPU; as a result, the GPU flags itself as RMA-read within a day.

The team disclosed the attack pattern to Nvidia on 29 April 2026 and subsequently to Google, Microsoft and AWS, and held the work until the 25th of August. A code release is scheduled for the 15th of November, even though there is currently no CVE information or patch being deployed to address the issue.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png) 

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
