---
title: How optical interconnects and silicon photonics emerged as AI's next hot commodity
source_url: https://www.tomshardware.com/tech-industry/photonics/how-optical-interconnects-and-silicon-photonics-emerged-as-ais-next-hot-commodity-looming-us-china-summit-puts-photonics-into-the-crosshairs
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-12T13:38:39Z'
published: '2026-08-12T00:00:00Z'
description: The U.S. wants Chinese optical transceivers out of future AI data centers,
  but China’s current dominance of the rapidly evolving photonics supply chain could
  make a ban complicated
image: https://cdn.mos.cms.futurecdn.net/H9c8yy2A5KxKsr5o3HGqr4-1920-80.jpg
---

![Quantum-X InfiniBand Photonics Switch](https://cdn.mos.cms.futurecdn.net/H9c8yy2A5KxKsr5o3HGqr4.jpg) 

The race to solve AI's copper bottleneck for scale-up and scale-out intensified last week, as the Federal Communications Commission (FCC) is drafting a measure that would block imports of new Chinese transceiver models, with officials hoping to publish the rule before the end of 2026. Yesterday, we covered exactly how much of the Secure Networks Act might rely on Chinese-made optical module manufacturers.

The technology is currently driving billions in acquisitions among companies like Marvell and Nvidia, and sending stock prices for dedicated Western Photonics companies like Coherent and Lumentum skyrocketing, amid calls that key materials like indium phosphide are in short supply.

Following the FCC's Secure Networks Act proposal, the market reacted immediately, with shares of China’s Zhongji Innolight, Eoptolink, and TFC Optical tumbling in early Shenzhen trading. Meanwhile, U.S. rivals Coherent and Lumentum closed 12.4% and 8.9% higher. Before Wednesday ended, however, the Chinese companies had clawed back much of the ground, even as analysts downplayed the impact of such a ban. Innolight still finished 7.3% lower in Shenzhen, while TFC actually closed 2.3% higher.

The whipsawing market movement was an apt representation of the potential implications of such a ban. Photonics, the industry's answer to its latest bottleneck of moving data between chips, is arguably the hottest technology in AI infrastructure right now. It is also a market defined by deep mutual entanglement. However, the FCC's proposal conveniently overlooks the fact that the biggest customer of China's photonics hardware is the United States.

With a crucial U.S.-China summit looming in September, the AI supply chain is being weaponized, once again, for global trade and supply negotiations, turning Silicon Photonics into a bargaining chip.

## AI's latest bottleneck is now a US-China tech wars battleground

As AI clusters scale into the hundreds of thousands of processors, the biggest problem is moving data between them. Computing tasks on frontier AI models are distributed across thousands of GPUs using parallel computing techniques. This setup requires the processors to exchange huge volumes of data multiple times a second. Copper interconnects still dominate, but as per-lane signaling climbs toward 200 Gbps, attenuation and crosstalk make passive copper impractical beyond a meter or two. Optical transceivers solve that problem by converting a chip's electrical signals into photons for transmission over fiber and back again, carrying far more data over longer distances at lower power.

As we examined in our recent detailed AI photonics roadmap, Vendors are racing from 800G modules to 1.6T parts while shortening electrical paths with co-packaged optics, which moves optical engines even closer to switch ASICs and, eventually, accelerators. The race to solve AI's photonics bottleneck is therefore becoming as strategically important as securing GPUs and HBM.

The money is already moving accordingly. Nvidia has reportedly committed $4 billion across Coherent and Lumentum to lock up supply. Elsewhere, Marvell agreed to pay $3.25 billion upfront for silicon photonics startup Celestial AI, with earnouts potentially taking the deal to $5.5 billion. At the same time, Elon Musk has received FTC clearance to acquire Mesh Optical. Meanwhile, Microsoft, Meta, and OpenAI have teamed with Broadcom, AMD, and Nvidia in an optical interconnect alliance to develop an open optical scale-up interconnect.

China has been building its own stack. Wuxi's CHIPX pilot line — the country's first dedicated photonic chip fab — began mass-producing six-inch photonic wafers in 2025. Shanghai opened a state photonic computing laboratory in June alongside newly listed startup Lightelligence. Crucially, Chinese officials note photonic chips don't require the EUV lithography tools Washington has cut off.

Commercially, China appears to be currently leading the market. Chinese vendors account for nearly two-thirds of global transceiver unit shipments and roughly 60% of datacom transceiver revenue, according to Counterpoint Research. Innolight — fresh off a $6.8 billion Hong Kong IPO, the city's biggest this year — leads with a 27% revenue share, ahead of Coherent's 17%, with Eoptolink third and Lumentum at roughly 6%.

However, those figures do not reveal the deep-seated supply-chain entanglements that severely complicate any ban. Innolight and Eoptolink reportedly supply the majority of 800G modules in Nvidia's AI clusters, while pairing DSP chips from Broadcom and Marvell with laser components from Lumentum, Coherent, and Mitsubishi Electric. Western rivals, in turn, need Chinese indium phosphide — export-controlled by Beijing since 2025 — for their lasers.

## The U.S. ban

It is amid the intense photonic race, marked by co-dependency between the two countries, that the FCC is seeking to ban related Chinese hardware. Reuters says the agency is drafting a rule that would deny new models of Chinese optical transceivers the equipment authorization they need to be imported, marketed, or sold in the US.

Washington fears the transceivers could become vectors for data theft, malware, or service disruption, with officials reportedly seeking to avoid another Huawei situation, in which Chinese telecom hardware became so embedded in U.S. infrastructure that removing it proved slow and expensive.

If enacted, the rule would be the latest round in a years-long technology conflict spanning security fears and market dominance, one that has extended squarely into AI. On the inbound side, the FCC has banned Huawei gear since 2019. It added foreign-made drones to its Covered List in December 2025, new consumer routers in March, and power inverters and advanced robots in July — each time citing national security. On the outbound side, Washington restricts AI GPUs, ASML's EUV machines, chipmaking tools, and manufacturing tech from reaching China, aiming to slow its AI ascent.

The Trump administration has argued that these bans have barely had any impact on the U.S. economy while enhancing national security. A photonics ban may be more consequential. The U.S. is effectively contemplating short-term disruption to prevent a scenario where the next generation of a critical AI technology, the optical layer of every future data center, would be Chinese hardware. On the other hand, the FCC appears to accept the current supply chain reliance, as the millions of Chinese modules already installed would stay put.

## China’s response

For every ban the US issues, Beijing insists it emerges stronger. Officials credit the chip restrictions with forcing focus. Chinese firms delivered 1.65 million AI GPUs in 2025, with homegrown suppliers like Huawei and Cambricon ramping up production as Nvidia's local market share fell below 60%. Domestic firms are also developing alternative manufacturing approaches. Prinano recently claimed wafer-scale photonic-chip production using nanoimprint lithography instead of DUV, although important yield and volume data remain undisclosed. China now says it doesn't even want American chips, blocking Nvidia H200 imports while certifying domestic accelerators for state procurement.

The photonics response has been similar, this time with open displeasure. China's Foreign Ministry said it "firmly opposes" the potential restriction and accused Washington of overstretching national-security concerns. Chinese legal and market analysts told *SCMP* that existing approved modules should remain unaffected. They argued that Western suppliers lack the packaging capacity, cleanrooms, and manufacturing scale to replace Chinese production within the next few years.

Dai Menghao of law firm King & Wood, quoted in the *SCMP* report, called the measure "relatively mild," expecting a framework like the FCC's router and inverter rules, where approved hardware keeps selling, and only new models face denial. That comparison doesn't exactly match. Routers, unlike photonics, are a mature category. In a market right in the middle of a transition, almost everything shipping into next-generation builds would fall under the "new model" category.

Still, Chinese experts insist Washington is underestimating its own exposure. "The market and policymakers tend to underestimate how dependent the AI infrastructure ecosystem remains on Chinese optical-module vendors," said Neil Shah, vice-president of research at Counterpoint. "Replacing that capacity within the next couple of years would be very difficult."

For now, the rule that would affect a ban remains a draft, subject to comment periods, carve-outs, and court challenges. With a potential US-China summit looming in September, the world's most important AI component has now potentially turned into a geopolitical flashpoint.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
