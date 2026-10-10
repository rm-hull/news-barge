---
title: We tested gaming performance in 17-year-old Windows 7 against Windows 11 on
  a modern gaming PC — older operating system delivers advantages in some scenarios
source_url: https://www.tomshardware.com/software/windows/we-tested-gaming-performance-in-17-year-old-windows-7-against-windows-11-on-a-modern-gaming-pc-older-operating-system-delivers-advantages-in-some-scenarios
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-10T17:23:17Z'
published: '2026-10-10T00:00:00Z'
description: Can an old OS beat a new modern rig?
image: https://cdn.mos.cms.futurecdn.net/GK5BBzfVnS4uShqz4uQXpb-1999-80.png
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Admin
- Arkham Knight
- Dan Mateescu
locations:
- Arkham City
organisations:
- AMD
- Arkham Asylum
- Arkham City
- Arkham Knight
- Arkham Origins
- Batman
- Borderlands
- CD Projekt Red
- CPU
- CSM
- Corsair Nautilus
- DXVK
- DoF
- GPU
- Get Tom's Hardware
- Google
- HVCI
- Hitman
- Hypervisor-Protected Code Integrity
- ISO
- Microsoft
- OS
- PC
- PCSS
- Percentage Closer Soft Shadows
- RAM
- Redux
- Secure Boot
- Tessellation
- The Witcher
- UAC
- USAFRet
- User Account Control
- VBS
- Virtualization-Based Security
- Vista
- Wild Hunt
- Windows 7
- YouTube
---

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/GK5BBzfVnS4uShqz4uQXpb-1920-80.png)
![](https://cdn.mos.cms.futurecdn.net/fsmmX34yhrKZwE44QQk7Qg-200-100.png)

After the rough reception of Windows Vista, Windows 7 launched in 2009 to largely positive reviews. Even 17 years later, it remains one of the most beloved versions of Windows ever released. But how does this nearly two-decade-old operating system hold up on modern hardware? We managed to install Windows 7 on a modern PC and put it to the test across eight DirectX 11 games and two DirectX 9 titles to see how its gaming performance compares to Windows 11 today. Surprisingly, Windows 7 still carves out many notable wins over its successor.

At launch, Windows 7 was very similar to Windows Vista in many respects. Vista had introduced significant changes under the hood compared to Windows XP, including technologies such as SuperFetch, ReadyBoost, ReadyDrive, new asynchronous APIs, and other I/O improvements. It also introduced native processor power management and various memory-management enhancements. On the visual side, Vista was the first version of Windows to feature Windows Aero, with its distinctive glass-like window borders.

Windows 7 retained many of these underlying technologies while addressing several of Vista’s biggest criticisms. One notable improvement was greater control over User Account Control (UAC), allowing users to adjust how frequently they received UAC prompts. In Vista, these prompts could appear far too often, becoming a major source of frustration for many users.

Windows 7 also benefited from something that had nothing to do with the operating system itself: more powerful hardware. When Vista launched, many mid-range and budget PCs struggled to deliver smooth performance, particularly when using more demanding visual features such as Windows Aero. By 2009, however, PC hardware had advanced considerably, and the performance required to run these features smoothly was no longer a significant concern for most users.

### The Challenge of Running Windows 7 on a Modern PC

Getting Windows 7 running on modern hardware is not as straightforward as installing a current version of Windows. At 17 years old, the operating system predates many of the technologies used by modern PCs, meaning driver support is extremely limited. For example, Windows 7 does not include native NVMe or USB 3.0 support, so the necessary drivers have to be slipstreamed into the installation ISO. Microsoft did eventually release patches that added NVMe support, but without injecting the appropriate drivers into the ISO, the Windows 7 installer will not recognize an NVMe drive.

Our system is based on AMD’s AM5 platform (with the full system specifications detailed later in the article), which presents another limitation: there are no official Windows 7 chipset drivers for the platform.

Fortunately, we are using an RDNA 2 GPU, which does have Windows 7 driver support, allowing us to use a relatively modern graphics card for our testing.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The motherboard is also an important consideration. Modern motherboards that have dropped CSM (Compatibility Support Module) and legacy boot support can make installing Windows 7 considerably more difficult, and in some cases may prevent the operating system from booting altogether. Fortunately, our motherboard still supports CSM, so this was not an issue for our setup.

### Test System

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/K4XmUAhc2bvtfDrbWuPXnb-1200-80.png)

## Windows 7 system specs

* AMD Radeon RX 6950 XT
* Ryzen 7 9800X3D
* 64GB (2x32GB) G.SKILL Flare X5 DDR5 @6000 MHz CL30
* Seagate Lightsaber FireCuda (530) NVMe SSD
* ASUS ROG STRIX B850-F Gaming WiFi
* Corsair Nautilus 360 RS AIO Cooler
* HAGS not supported by driver
* Windows 7 Ultimate 64-bit Service Pack 1 (Build 7601)
* AMD Adrenalin 22.6.1 for Windows 7 (2022)

## Windows 11 system specs

* AMD Radeon RX 6950 XT
* Ryzen 7 9800X3D
* 64GB (2x32GB) G.SKILL Flare X5 DDR5 @6000 MHz CL30
* Seagate Lightsaber FireCuda (530) NVMe SSD
* ASUS ROG STRIX B850-F Gaming WiFi
* Corsair Nautilus 360 RS AIO Cooler
* HAGS not supported by driver
* Windows 11 25H2 (Build 26200.9278)
* AMD Adrenalin 22.6.1 for Windows 11 (2022)

For Windows 7, we disabled Secure Boot, enabled CSM, and set Boot Device Control to Legacy OPROM Only. Enabling CSM means that we no longer have access to Resizable BAR (it's not supported anyway). For Windows 11, we disabled VBS (Virtualization-Based Security) and HVCI (Hypervisor-Protected Code Integrity).

It is important to note that while we used Adrenalin 22.6.1 for both Windows 11 and Windows 7 testing, the two packages contain different internal driver versions. Although both packages were released in June 2022, the Windows 11 driver is based on a more advanced codebase than the Windows 7 driver.

In both cases, we performed a clean install of each operating system and filled the SSD to about 50-60%.

### Performance Testing

We tested ten games in total: eight using DirectX 11 and two using DirectX 9. The DirectX 11 titles are the primary focus, as both systems support them natively. By comparison, our Windows 11 system will run DirectX 9 games through the D3D9On12 mapping layer, while our Windows 7 system will run them natively. There are ways to get around the use of D3D9On12 on Windows 11, but we want to evaluate the out-of-the-box experience that most gamers would encounter. As a result, we expect Windows 7 to have an advantage in the DirectX 9 titles.

It will become apparent in the results below that the advantages of each operating system will vary depending on whether we are **CPU-limited** or**GPU-limited**.

## Metro 2033 Redux (DX11)

Metro 2033 Redux was released in 2014 and features a new lighting engine, higher visual fidelity, and new locations for certain levels. The game is predominantly GPU-bound, but there are moments when GPU utilization drops sharply as you traverse the game world. At these points, the CPU becomes the limiting factor, resulting in a corresponding drop in performance.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/cuWUEZA4Nrgq3RtyP87Bib-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/7CaiQeDXQeeX7qQ5oKRShb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/JbSoRpc63FHUwAN3ECgCib-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/cuWUEZA4Nrgq3RtyP87Bib-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/7CaiQeDXQeeX7qQ5oKRShb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/JbSoRpc63FHUwAN3ECgCib-468-80.png)

Although Windows 11 delivers a higher average frame rate, Windows 7 handles the CPU-related performance drops much better, resulting in significantly stronger 1% lows. Installing the AMD chipset drivers and enabling Resizable BAR improves 1% lows on Windows 11 slightly, but it still falls well behind Windows 7.

Windows 11’s more advanced graphics driver appears to provide an advantage in GPU-limited scenarios, while Windows 7’s lower CPU overhead offers more consistent frame pacing, though with lower peak performance.

## Batman: Arkham Origins (DX11)

Batman: Arkham Origins runs on a modified version of Unreal Engine 3 and uses several DX11 enhancements such as Tessellation, Ambient Occlusion HBAO+, Percentage Closer Soft Shadows (PCSS), and Depth of Field (DoF).

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/UKbxNKvSyjvuwap5bhCyya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/NsrypLpiKhEwyrkzSubzya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/ntMXHwu39jdunESyzsgyya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/UKbxNKvSyjvuwap5bhCyya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/NsrypLpiKhEwyrkzSubzya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/ntMXHwu39jdunESyzsgyya-468-80.png)

When CPU-limited at 1080p, Windows 7 once again puts in a strong showing, outperforming Windows 11 in both average frame rate and 1% lows. Surprisingly, Windows 7 also comes out ahead at 4K in Origins, though with a far smaller advantage. As we will see throughout the remainder of our testing, however, this is a rare occurrence. Even so, Windows 7 maintains a slight performance advantage over Windows 11 at 4K in this title.

## Batman: Arkham Knight (DX11)

Batman: Arkham Knight was both a critical and commercial success, despite a notoriously troubled PC launch plagued by severe bugs and major performance issues. Visually, however, the game still holds up remarkably well, and modern hardware is more than capable of brute-forcing this demanding PC port.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/KFLEuhKXzr2bs2YY6VSRya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/DxVJD8rkixqyFdJdsyDVya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/VswQJsWpmUujaLHBeNThya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/KFLEuhKXzr2bs2YY6VSRya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/DxVJD8rkixqyFdJdsyDVya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/VswQJsWpmUujaLHBeNThya-468-80.png)

Windows 7 again delivers higher performance at 1080p when we are CPU-limited. Windows 11 jumps ahead when we become GPU-limited at 1440p and 4K.

## Batman: Arkham City (DX11)

Batman: Arkham City was the second entry in the series, following Arkham Asylum, and the first to support DirectX 11. This introduced features such as tessellation, which adds greater geometric detail to characters and environments.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/Ttat94CoVC3VhUXxiHgSya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/YFWX8CuwN4AJtgNWkq392b-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/GyapAJH7bXa3SCPVmDuUya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/Ttat94CoVC3VhUXxiHgSya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/YFWX8CuwN4AJtgNWkq392b-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/GyapAJH7bXa3SCPVmDuUya-468-80.png)

In Arkham City, our system is GPU-bound at every resolution tested, giving Windows 11 the advantage across the board.

## The Witcher 3: Wild Hunt (DX11)

The Witcher 3 faced some controversy at launch over reductions in image quality compared to its initial reveal. CD Projekt Red quickly released a patch addressing these concerns and improving the game’s visuals. From a performance perspective, however, the game was extremely demanding at launch.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/DFr38poxhf4ojCNmykUmhb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/3K269j84cpGjC7HUQn54ib-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/kvG6n59y7tRgsmxWQeQYjb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/DFr38poxhf4ojCNmykUmhb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/3K269j84cpGjC7HUQn54ib-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/kvG6n59y7tRgsmxWQeQYjb-468-80.png)

While the game is very GPU bound in general, at 1080p we did encounter a slight CPU bottleneck, which gave Windows 7 an advantage in 1% lows. At 1440p and 4K, Windows 11 takes a slight lead.

## Control (DX11)

Control is the newest title we tested for this comparison, having launched in 2019. While the game introduced several ray tracing features, these were exclusive to the DirectX 12 API. Since Windows 7 does not support DirectX 12, we tested Control using DirectX 11 on both operating systems. Even without ray tracing, Control remains the most graphically advanced title in our Windows 11 vs Windows 7 comparison.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/LsgcPnA3GwgDkVYAMkPJza-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/jYWNX47dft2RTdDUp4jatc-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/MkFQWvmSg7AVGfEAabMJhb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/LsgcPnA3GwgDkVYAMkPJza-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/jYWNX47dft2RTdDUp4jatc-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/MkFQWvmSg7AVGfEAabMJhb-468-80.png)

Windows 11 wins across the board. This is not a surprise, as we are GPU-limited across all resolutions tested.

## Hitman: Absolution (DX11)

Hitman: Absolution was released in 2012 and was the first game to use the Glacier 2 engine. The updated engine could handle crowds of up to 1200 characters, which was unprecedented at the time. The game also featured several DirectX 11 enhancements, including global illumination and tessellation.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/MhQv2Uspd69mtYSXLKdzkb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/LU9XujFNaowb8xSum9o8nb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/PLpgugYoo4Hk7LcqXbCVmb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/MhQv2Uspd69mtYSXLKdzkb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/LU9XujFNaowb8xSum9o8nb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/PLpgugYoo4Hk7LcqXbCVmb-468-80.png)

This is another game that pushes the GPU hard, regardless of resolution. Our test system was GPU-limited even at 1080p.

## Hitman 2 (DX11)

Hitman 2 was released in 2018, making it the second-newest game in our operating system comparison. It features detailed environments, dense crowds, and full reflections across many surfaces, making it an impressive-looking title overall.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/z6iCuE8zYJ8cEppU8zMvmb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/zQ4SnB3gcnAoA32TvgWhhb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/CMn3KQsdg746b265BFt9Ab-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/z6iCuE8zYJ8cEppU8zMvmb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/zQ4SnB3gcnAoA32TvgWhhb-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/CMn3KQsdg746b265BFt9Ab-468-80.png)

Hitman 2 is another example where our test system is GPU-limited at every resolution, giving Windows 11 a clean sweep across the board.

## Batman: Arkham Asylum (DX9)

We now move to our first DirectX 9 game. As previously mentioned, Windows 7 should have an advantage here because our Windows 11 system must use the D3D9On12 mapping layer for DirectX 11 games. But just how much of an advantage?

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/YGuVfpwFLGwaTw2Gcbfhea-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/Z57jTehZMPHaZ9Us8xJgfa-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/tM9quKyuy4LRPtBTxh72ga-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/YGuVfpwFLGwaTw2Gcbfhea-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/Z57jTehZMPHaZ9Us8xJgfa-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/tM9quKyuy4LRPtBTxh72ga-468-80.png)

Significant advantages for Windows 7 in average frame rate and 1% lows, especially at 1080p and 1440p. The advantage is reduced at 4K, but the performance is still smoother overall in Windows 7. Another translation layer, such as DXVK, may close the gap.

## Borderlands 2 (DX9)

Borderlands 2 is our second DirectX 9 game and the final overall game tested.

![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/de7Zwxebrm8QpC9Kd9dZrc-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/XH9GDKB7gw2scfM88fzyya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/rjqgnQS7BTP4nccCsBa72b-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/de7Zwxebrm8QpC9Kd9dZrc-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/XH9GDKB7gw2scfM88fzyya-468-80.png)
![We Tested Gaming Performance in Windows 7 on a Modern PC](https://cdn.mos.cms.futurecdn.net/rjqgnQS7BTP4nccCsBa72b-468-80.png)

Once again, another massive win for Windows 7 at the lower resolutions. The performance at 4K is virtually identical.

### Bottom Line

## Windows 11 is optimized for GPU-hungry games

The results are interesting, but perhaps not entirely surprising. The DirectX 9 results are largely in line with our expectations, given that Windows 11 must run these games through the D3D9On12 mapping layer, yielding substantial advantages for Windows 7.

The DirectX 11 results are more nuanced, but a clear trend emerges: Windows 7 has the advantage when we are CPU-limited, while Windows 11 performs better when we are GPU-limited. This makes sense given that Windows 11 uses graphics drivers built on a more advanced codebase, while Windows 7 is a leaner operating system with fewer background processes and, consequently, lower CPU overhead.

Microsoft has recently detailed its K2 plan, which aims to improve the performance and reliability of Windows 11. We hope these continued efforts to improve Windows 11 pay off.

The lower CPU performance we observed in Windows 11 cannot be attributed to its most notable security features, such as VBS (Virtualization-Based Security) and HVCI (Hypervisor-Protected Code Integrity), as we disabled both during testing. Notably, Windows 7 does not support VBS or HVCI at the software level, while Windows 11 supports hardware virtualization extensions (such as Intel VT-x or AMD-V) and Second Level Address Translation (SLAT). Additionally, fixed-function hardware can reduce the impact of virtualization to varying degrees, based on the CPU architecture's capabilities. However, additional telemetry and other background services still pop up and use precious CPU cycles.

Using the latest chipset drivers and enabling features such as Resizable BAR does not help Windows 11 close the gap in CPU-limited scenarios by any significant margin. Ultimately, we would like to see Windows 11 become leaner and more efficient, as our results suggest there is still some performance left on the table, particularly on the CPU side.

![Dan Mateescu](https://cdn.mos.cms.futurecdn.net/ExmVPaYL2qmyNWzwnGHxKQ-140-80.jpg)

Dan Mateescu is a PC enthusiast with many years of experience benchmarking PC hardware. In 2021, he started his own YouTube channel called 'Compusemble' where he benchmarks hardware in video games and the latest tech demos.

* Since people cannot always afford 64GB of memory at the insane prices,  
    
  This test would have been more interesting constrained to 16GB or otherwise somehow constrained to a slightly unusual 24GB since Win7 hogs less memory. Or at least, dual-test with both memory options and the same slate of games.(Test1: 64GB/Test2: 16GB) Reply
* ezst036 said:Since people cannot always afford 64GB of memory at the insane prices,  
    
  This test would have been more interesting constrained to 16GB or otherwise somehow constrained to a slightly unusual 24GB since Win7 hogs less memory.The idea was to remove any hardware issues, and concentrate on the OS differences.  
    
  Reducing it to 16GB could easily show difference in game performance due to the RAM, not the OS. Reply
* USAFRet said:The idea was to remove any hardware issues, and concentrate on the OS differences.  
    
  Reducing it to 16GB could easily show difference in game performance due to the RAM, not the OS.  
  Reducing available memory would allow to see differences in memory management by the OS and the amount of memory used for internal OS purposes. Both very important, as differences in computational game performance are likely largely due to GPU drivers. Reply
* qxp said:Reducing available memory would allow to see differences in memory management by the OS and the amount of memory used for internal OS purposes. Both very important, as differences in computational game performance are likely largely due to GPU drivers.Both methods have their advantages and disadvantages. Reply
* Admin said:Windows 11’s more advanced graphics driver appears to provide an advantage in GPU-limited scenarios, while Windows 7’s lower CPU overhead offers more consistent frame pacing, though with lower peak performance.What?!?  
  How does that "appear" to be the case at all?  
  Windows 11 has a ton of thread and core management to reduce power needs/ increase efficiency and with games not telling the OS that they want to be run with a high priority they get "round robinned" along with all other things currently running on the system, causing bad lows.  
  Just having a tool showing you clocks and actual CPU usage while gaming and reporting those alongside would go a very long way.  
    
  The overhead over 7 on the CPU for an 8c/16t system is basically zero, especially if none of the games ever got close to using all cores fully or even semi-fully.  
  Which with the newest title being from 2019 is pretty much guaranteed.  
  Overhead only makes a difference if you reach beyond the full load mark. Reply
* Now try the experiment in 5 years when the automatic updates windows 11 won't let you turn off have completely bricked your computer and the built in OS spyware has had you arrested for an un licenced copy of a Milli vanili song someone emailed you.  
    
  The number 1 reason people are not buying new computers is they don't want win 11.  
    
  Maybe the new chrome os silver will save us all in November. Sell your Microsoft stock and buy Google stock Reply
* Sum Change said:The number 1 reason people are not buying new computers is they don't want win 11.Have any stats for this?  
    
  I expect the "number 1 reason" is that hardware has sort of stagnated, and a 5 or 10 year old system still runs the stuff they want.  
    
  Used to be, there was a major visible hardware change every year. It was beneficial to upgrade.  
  Today, maybe not so much.  
    
  "most people" don't know or care which OS is in it. Reply
* USAFRet said:I expect the "number 1 reason" is that hardware has sort of stagnated, and a 5 or 10 year old system still runs the stuff they want.That'd be the #2 reason. After the #1 reason of recent massive memory/storage price hikes, leading to articles like this:  
    
  Extinction Watch: Sub-$500 Computers in Danger, According to Report  
  The stagnation is important, but it was present in 2025, 2024, etc. Reply
* Sum Change said:Now try the experiment in 5 years when the automatic updates windows 11 won't let you turn off have completely bricked your computer and the built in OS spyware has had you arrested for an un licenced copy of a Milli vanili song someone emailed you.  
    
  The number 1 reason people are not buying new computers is they don't want win 11.  
    
  Maybe the new chrome os silver will save us all in November. Sell your Microsoft stock and buy Google stocklmao  
    
  Did you make this all up in a dream? Reply
