---
title: Today I learned a single Google Gemini query uses about five drops of water,
  but that's not the whole truth
source_url: https://www.techradar.com/pro/today-i-learned-a-single-google-gemini-query-uses-about-five-drops-of-water-but-thats-not-the-whole-truth
source_site: TechRadar UK
source_slug: techradar-uk
description: Google's per-prompt figure skips the water power plants use
image: https://cdn.mos.cms.futurecdn.net/8fSZ5osisap2bjsFpu5UkE-2190-80.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-19T02:31:45Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Alex de Vries-Gao
- Shaolei Ren
locations:
- US
organisations:
- AI
- Digiconomist
- Gemini
- Google
- Lawrence Berkeley National Laboratory
- Meta
- TechRadar Pro
- UC Riverside
---

![Gemini](https://cdn.mos.cms.futurecdn.net/8fSZ5osisap2bjsFpu5UkE-1920-80.jpg)

Asking Gemini to rewrite your email costs about five drops of water. At least, that's what Google says.

In an August 2025 technical paper, the company estimated that a median Gemini Apps text prompt uses 0.24 Wh of energy, emits 0.03 grams of CO2 equivalent and consumes 0.26 mL of water.

Google compared the energy use to watching TV for less than nine seconds. It also claimed that over a 12-month period, the energy and carbon footprint of a median prompt fell by 33x and 44x respectively. Those are big efficiency gains, assuming the math holds up.

## A technically correct figure

Credit where it's due, Google's method counts more than most. Alongside the AI chips themselves, it includes host CPUs and memory, idle machines kept on standby, plus data center overhead like cooling. If you count only active TPUs and GPUs, the numbers drop to 0.10 Wh and 0.12 mL, which Google itself calls an underestimate.

By Google's own breakdown, the AI accelerators account for 58% of the energy behind each prompt. Host CPUs and memory take another 24%, with spare capacity and data center overhead making up the remaining 18%.

The catch is in the water. Google's figure covers only the water consumed on-site to cool its data centers, calculated from its 2024 fleetwide average. The fine print also notes that the data hasn't been verified by an independent third party.

## Reading the fine print

Power plants drink water too, for cooling and for making the steam that spins their turbines. That's the part Google skipped, according to Shaolei Ren, a UC Riverside associate professor whose research the paper cited. "They're just hiding the critical information," Ren told an interviewer.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Google said its five drops were far below a previous estimate of about 50 mL per prompt drawn from Ren's work. But Ren says his figure already included that off-site water. His 2023 study estimated GPT-3 consumed a 500 mL bottle of water for every 10 to 50 medium-length responses, depending on when and where it ran.

That off-site share is far from a rounding error. A 2024 Lawrence Berkeley National Laboratory report found the water used to generate electricity for US data centers in 2023 was about 12 times what they used for cooling. Meta, the only hyperscaler that discloses this figure, puts its own indirect water use at more than 20 times its direct use.

Ren and Alex de Vries-Gao, founder of Digiconomist, also took issue with Google comparing its median prompt against their averages. Both argued Google should have reported location-based emissions, which reflect the actual power grid near each data center, rather than market-based figures that credit its clean energy purchases.

Then there's scale. The Gemini app passed 1 billion monthly active users in August 2026. Meanwhile, Google's latest environmental report shows its total water consumption rose 34% to 10.9 billion gallons in 2025.

Five drops per prompt might be technically accurate. It just isn't the number that matters most.
