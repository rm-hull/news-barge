---
title: Just one instruction on AMD's 2015-era CPUs cracks open secret memory areas
  and gives full hardware-level control — exploit for 15h and 16h chip families gets
  you access to Platform Security Processor, microcode, and System Management Interface
source_url: https://www.tomshardware.com/tech-industry/cyber-security/just-one-instruction-on-amds-2015-era-cpus-gets-you-access-to-platform-security-processor-microcode-and-system-management-interface-exploit-for-15h-and-16h-chip-families-cracks-open-secret-memory-areas
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-14T13:34:21Z'
published: '2026-08-14T00:00:00Z'
description: Not a very practical exploit, but an exceedingly interesting one.
image: https://cdn.mos.cms.futurecdn.net/koM4rKdc9cgWLgThGyxpee-2000-80.jpg
---

![Bug](https://cdn.mos.cms.futurecdn.net/koM4rKdc9cgWLgThGyxpee.jpg) 

Many cybersecurity exploits have been deemed The One Ring To Rule Them All, but that moniker is rarely as true as a literal bit that disables the memory mapping on some AMD CPUs, granting access to normally inaccessible areas. With just one instruction, you can access off-limits software like Platform Security Processor (PSP) where the fTPM runs, the System Management Mode (SMM), microcode patch RAM, and other various sundries — in other words, full hardware-level control.

The exploit is called Skitter Creek Bath Salts (Skitter), and was developed by prolific hacker Christopher Domas, famous for finding CPU flaws like Sandsifter and God Mode Unlocked. Only AMD chips from the 15h and 16h families are affected, roughly 2011 to 2015 vintages. Family 15 is FX-series desktop chips and some Opterons, while 16h includes low-power Jaguar- and Puma-based SoCs like those in the PlayStation 4 and Xbox One, plus a handful of Athlon, Sempron, and Opteron-X chips, among others.

To pull off this exploit, you'll need kernel-level access, meaning the ability to run your own drivers. But once you do, the entirety of DRAM is your oyster. AMD published a security bulletin on the matter, saying these chips are out of security support, plus, as mentioned, the necessary access level means an attacker already controls the machine anyway.

If you're confused as to how one instruction opens up a system, here's our attempt at a simplification. Say you have 16 GB of RAM. You'd think that Windows gets all 16 GB to play with, from address 0 to the end of memory — but as you may have noticed before, it's actually a bit less than that. The rest is reserved for system-level data.

Some parts are visible to the OS so it can interact with devices, but others include Very Important Things like PSP, SMM, microcode patches, all in sections *supposed to be completely untouchable.* If they were accessible, the system as a whole wasn't secure by definition anymore — just think of a malicious driver being able to freely mess with how your processor handles data.

For performance reasons, modern processors' RAM controllers don't use memory in a straight line, so to speak — they use bank interleaving, meaning that the actual bytes in the DRAM are jumbled, all while the OS sees a nice, tidy, flat surface. As it turns out, the CPU setting that controls this feature is accessible to the OS in the aforementioned chip families, and it's called BankSwizzleMode (Swizzle). It can be toggled on or off with the instruction "xor dword [0xf80c2094], 0x00400000", a simple bit twiddle. And as it turns out, this can be exploited.

First, you run a loop to figure out how the mapping normally functions. You place a canary value in memory (say, 0xDEADBEEF, according to tradition), disable Swizzle, run through memory to see where it landed, and reenable Swizzle again. Do this enough times, and you know exactly how visible memory is mapped into physical DRAM, *and vice-versa.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

With the map now in your possession, you can now disable Swizzle and force a read or write to normally inaccessible areas of the DRAM, since you now know where it will land. With this, you can access all the previously hidden code and data, netting you hardware-level access to do anything you want, including reading fTPM signing code and any other low-level shenanigans you can think of.

Attentive readers might be wondering why the system doesn't crash during this process since you're effectively temporarily turning the RAM into a spaghetti mess. The answer is that every time you enable and disable Swizzle, you prepare the CPU by disabling interrupts, along with a number of other measures. Even still, the machine can crash during the map-collection step, but that only needs to be done once. After you have the map, the likelihood of a crash is fairly low since you'll be targeting specific locations.

Another question might be why sending a bit to a memory location somehow messes with the CPU, and the answer is that part of OS-accessible memory is actually mapped to hardware according to the Memory-Mapped Configuration Space standard (MMCONFIG) — meaning that reads or writes to that space are directed to hardware configuration settings, not actual RAM.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
ReplyWith this, you can access all the previously hidden code and data, netting you hardware-level access to do anything you want, including reading fTPM signing code and any other low-level shenanigans you can think of. And how do you propose we do that MR. Tom's AI. You do know that ftpm doesnt exist in these older AMD CPUs. Do we fuse it with newer ones using magic?
