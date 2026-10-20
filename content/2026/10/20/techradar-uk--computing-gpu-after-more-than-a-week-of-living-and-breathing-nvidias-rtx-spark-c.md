---
title: I've been testing Nvidia's RTX Spark chip to see what it's capable of — and
  if you want to game, create and vibe code on the go, it’s a great all-around package
source_url: https://www.techradar.com/computing/gpu/after-more-than-a-week-of-living-and-breathing-nvidias-rtx-spark-chip-im-impressed-by-how-much-ai-creative-and-gaming-power-it-packs-into-such-a-tiny-space
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T14:18:18Z'
published: '2026-10-20T00:00:00Z'
description: Here's everything the brand new Nvidia RTX Spark chipset can do for your
  creative work, gaming and AI workflow.
image: https://cdn.mos.cms.futurecdn.net/S5x7ykARbEuwdH8oMZ7QWL-1920-80.jpg
categories:
- Technology & Software
people:
- Hermes
locations:
- San Francisco
organisations:
- Adobe Creative Suite
- Apple
- Canva
- Hermes
- MLPerf Client
- Nvidia
- Nvidia’s
- Outlook
- Puget Bench
- PugetBench
- RTX Spark
- SoC
- Unity
- World of Warcraft
---

![A man types into the Hermes hybrid AI agent app on the Asus ProArt P16 RTX Spark laptop.](https://cdn.mos.cms.futurecdn.net/S5x7ykARbEuwdH8oMZ7QWL-1920-80.jpg)

Having been at Nvidia's RTX Spark event in San Francisco earlier this month, I was lucky enough to get a firsthand walk through of the many things the 'superchip' can do. Since then I've spent almost every waking moment putting the ARM-based RTX Spark through its paces and seeing what makes it so different from other chipsets that have come before.

The RTX Spark is Nvidia’s first System on a Chip (SoC). Combining an 18-core CPU and 5120 Cuda core Blackwell RTX GPU all in one, or a 20-core CPU and 6144-core GPU for its meatier version, it offers an integrated chipset in the vein of Apple’s M series chips. While Apple’s silicon is known for its oomph, that Blackwell RTX GPU means you’ll also get considerable gaming performance here to boot.

How does this translate in terms of raw numbers? It’s certainly got a lot going on under the hood, as the RTX Spark N1X chip I’ve been playing around with squeezes 20 cores into its CPU. While the 2,623 single-core performance I clocked on Geekbench 7.1 falls somewhat short of the 4,288 we got for Apple’s M5 chip, its 21,899 multi-core score massively outstripped the latter’s 17,926. That means that for tasks like content creation, software development and AI, you should be able to expect more oomph in your corner.

So given the potential it promises across agentic AI, creative workflows and gaming, let’s take a look at how it performs across each of those areas in turn.

## Hybrid agentic AI

![A man presenting on stage, with a slide reading &#039;Frontier Intelligence on your Desk&#039;. It shows how local models in August 2026 were achieving similar compute as frontier models were in April 2026.](https://cdn.mos.cms.futurecdn.net/5bsppbjHEzZANxsiJM6wEY-1200-80.jpg)

During the launch of Nvidia’s RTX Spark SoC, there was a huge focus on its potential for hybrid agentic AI. Now, cloud-based AI models are undoubtedly pretty powerful but I absolutely have security concerns about uploading my most private data to the cloud and I’m not entirely sure I want to blindly trust the companies behind some of these models.

Using local, open-source models that I can vet myself and that never transmit sensitive data outside of my network feels like a much safer alternative — but not everybody necessarily wants to cut themselves off from the power of frontier models. That’s why Nvidia has introduced a hybrid-system for the RTX Spark instead.

Instead, the hybrid-workflow that the RTX Spark supports allows you to select your choice of local models and ring-fence them for certain parts of an agentic workflow, while outsourcing specific, demanding tasks to cloud frontier models. As a result, users should be able to take a far more granular approach, deciding exactly how much they want to rely on public vs private models.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

For people who like to vibe-code complex products or are generating demanding 3D scenes, not being forced to choose between binary security options of a lax, YOLO approach and a full-blown lockdown will likely be a valuable tool.

So now that I’ve spent some hands-on time with the RTX Spark, how has its agentic performance delivered on these promises? To get a broad picture of I ran the MLPerf Client benchmark to simulate data analyst and SWE agentic workflows using the Qwen 3 8B local model, with each run hitting an average duration of 63.7 and 50.8 seconds and processing up to 14,005 and 10,238 tokens respectively.

I also benchmarked some generative image and video workflows using ComfyUI. When testing workflows using Flux2.Dev (NVFP4 and Flux2.Klein 4B Base) NVFP4 models for image generation, it took 46.5 and 16.2 seconds to generate respectively, while the LTX 2.5 (Distilled) NVFP4 model took 88 seconds. That’s broadly in line with what Nvidia has been promising and shows how rapidly the RTX Spark can generate media using local models.

Raw data will only tell you so much though. That’s why I spent days training my own AI agent using Hermes and the Qwen3.8 27B open-source local model to see what the RTX Spark could do.

Certainly, it seems to have absolutely ripped through some tasks on its Extra High setting. Feeding it some analytics data in CSV form, I asked it to tidy up the spreadsheet, analyze the data and present its key findings and after 12 minutes of pondering and tweaking, it happily spat out a pivot table and some observations on the data. While I wasn’t hugely surprised by any of its conclusions, I’ve spent months poring through this data and the fact it could identify the most essential points without any of my secure information leaving the laptop was pretty impressive.

Some experiments I conducted involved a little more patience and tweaking of the agent’s workflow to get the best results though. The first time I asked my Hermes agent to connect to my online email client and provide a digest of the day’s emails, it spent 75 minutes trying various methods to exchange tokens with Outlook’s online client, before crashing unexpectedly. However, the second time I played a slightly more active role, providing it feedback when I felt it was drifting or had come up against hurdles and it successfully set up the brief in 70 minutes.

So with some patience and judicious prompting, you can definitely get some good results utilizing a local model. Additionally, you don’t have to go through this full process every time — ask Hermes to save something as a skill and it will automate this process in future or even schedule it as a recurring Cron Job. You can even ask it to work out ways to improve the efficiency of existing skills, meaning it should be easier to minimize the run time and resources they require in future.

## Creative workflows

![A man presenting on stage, with a slide reading &#039;RTX Accelerated Creative Apps&#039;. It shows the huge range of RTX-accelerated creative apps there are, including Adobe, Affinity, Blender and Unreal.](https://cdn.mos.cms.futurecdn.net/WRCJVzrtc74aTdCpfYjRJY-1200-80.jpg)

You’d be forgiven for thinking this means the RTX Spark laptops are predominantly focused on AI tools. But that couldn’t be further from the case: while a lot of the press surrounding the chip has been on its agentic AI tools, this really isn’t the sole string to its bow.

As you can tell from the fact that the RTX Spark is used in the latest Asus ProArt P16, creative work is a big focus for the new SoC. Even if you’re not interested in the power it offers for generative AI, the sheer number of RTX-compatible creative apps out there, whether that’s Blender, Adobe Creative Suite, Canva or Unity shows how many creative giants are throwing their weight behind the new SoC.

Eager to test how well the RTX Spark handles creative work, I used Puget Bench to automate a range of tasks in Photoshop and Premiere Pro. PugetBench’s standard Photoshop workflow took 10.83 minutes and netted a score of 11,801, while its standard Premiere Pro pipeline took 8.12 minutes and achieved a score of 76,234, putting it firmly in the range of a true creative workstation. That means it sits in the rough region of Apple’s M5 chip, which scored 13,755 and 69,887 respectively, besting it on complicated video work but not quite equaling it for still imagery.

For those who use generative AI in their work, I also benchmarked some generative image and video workflows using ComfyUI. When testing workflows using Flux2.Dev (NVFP4 and Flux2.Klein 4B Base) NVFP4 models for image generation, it took 46.5 and 16.2 seconds to generate respectively, while the LTX 2.5 (Distilled) NVFP4 model took 88 seconds. That’s broadly in line with what Nvidia has been promising and shows how rapidly the RTX Spark can generate media using local models.

While I’m neither an aspiring cinematographer or a budding Blender artist, I’ve spent decades tinkering with static images so I dug out an old 4K, 300dpi Photoshop file. It was already pretty huge as it featured lots of hi-res layers, clipping masks and adjustment layers but I tripled the number of layers for good measure and added a bunch of filters and effects. Processing time remained less than a second and even halving the image size only took about five, which is pretty impressive given the sheer number of layers and groups I was working with.

And the RTX Spark should even be able to speed up these applications’ built-in AI tools, thanks to the recently announced collaboration between Nvidia and Adobe. Optimizing the apps to take full advantage of the chip’s GPU, Adobe promises that RTX Spark laptops offer 2x AI processing, editing, color and effects. That’s a real advantage for anyone that uses these AI tools as part of their workflow.

## Gaming performance

![A slide on stage reading &#039;RTX Spark Supports Hundreds of Games on Launch Day&#039;. It shows six titles already supported, including World of Warcraft: Forever; Gears of War: E-day; and Control: Resonant.](https://cdn.mos.cms.futurecdn.net/8y2NxMu6jH4Cp9CdRJkcLY-1200-80.jpg)

Given Nvidia’s history, gaming is naturally also a big focus for the RTX Spark chipset. As most games run on x86 architecture, SoCs haven’t been the most natural home for gaming in the past. However, Nvidia’s stature in this space means plenty of developers launched *RTX Spark* native versions of their games when the chip was launched on October 16, including*Cyberpunk 2077*,* Doom: The Dark Ages*, and* 007 First Light*— while the* Call of Duty* series is due to land in 2027. And for those that aren’t yet compatible, Prism emulation will mean you’ll be able to run many titles with only a slight impact on your CPU performance.

When it comes to gaming performance, the RTX Spark is certainly no slouch. It netted a 3DMark Port Royal score of 8,133, Steel Nomad score of 2,846 and a Speed Way score of 2,872. That’s a touch below Asus Zephyrus G14 withNvidia GeForce RTX 5070 Ti’s respective 10,119, 3,488 and 4,031 scores. But it’s considerably better performance than you’d get out of most laptops with an integrated GPU such as the pre-RTX-Spark Dell XPS 16, which secured values of 3,888, 1,488, and 916.

But while these simulated benchmarks are helpful for getting a broad view of gaming performance, in-game benchmarks are the best way of gaining real insight into how actual titles perform. While testing the RTX Spark, *Cyberpunk 2077* delivered a stable 30.16fps at 1080p on Raytracing: Ultra settings and*Doom: The Dark Ages* averaged out at 48.58fps at 1080p — very similar to the 32.33fps and 55.63fps we got out of the Asus TUF Gaming A14 with Nvidia GeForce RTX 5060.

Nothing compares to actually trying out games first hand though, so I fired up a few of my favorites and tried them out. *Cyberpunk 2077* honestly felt pretty playable even using the above Raytracing Ultra setting and once I’d switched down to Ray-tracing Medium, it ran at a wonderfully fluid 60fps.

Meanwhile, running *Gears of War: E-Day* at Ultra settings felt as smooth as tahini drizzled over a marble countertop. As I crunched through waves of the Horde, there wasn’t any noticeable slowdown even at Ultra settings, with the action never dipping below a seriously fluid 115fps. So it might not match the RTX 5090 for sheer power but anyone barring elite gamers will find a lot to like here still.

So even though it’s naturally not at the level of dedicated gaming laptops like the MSI Vector A18 HX A9W, I’m still pretty impressed with gaming on the RTX Spark chip. And that only becomes more pronounced when you compare it to similar lightweight SoC systems. While the MacBook Pro M5 is similarly impressive in terms of creative performance, it was barely able to scrap 11.5fps in Cyberpunk 2077 on Raytracing: Ultra settings.

As a result, if you’re looking for a chipset that will give you not just great performance in one specific task but great performance across everything you do, the RTX Spark has proven it will be a solid choice.
