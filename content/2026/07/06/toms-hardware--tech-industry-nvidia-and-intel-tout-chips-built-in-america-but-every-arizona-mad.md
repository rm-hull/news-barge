---
title: Nvidia and Intel tout homegrown American chip supply chain prowess as country
  bolsters local production, but gaps remain — crucial Blackwell packaging steps remain
  offshore as projects grow in scope and scale
source_url: https://www.tomshardware.com/tech-industry/nvidia-and-intel-tout-chips-built-in-america-but-every-arizona-made-blackwell-die-is-still-packaged-in-taiwan
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-06T18:20:00Z'
published: '2026-07-06T00:00:00Z'
description: America's AI supply chain now starts and ends in the U.S.
image: https://cdn.mos.cms.futurecdn.net/EYMn2KePtE4e2hVbbVa8FY-1216-80.jpg
---

![TSMC Arizona](https://cdn.mos.cms.futurecdn.net/EYMn2KePtE4e2hVbbVa8FY.jpg) 

Nvidia shouted proudly in a recent blog post that its network of American manufacturing partners and suppliers now spans 43 states, that TSMC's Phoenix plant is producing Blackwell wafers at volume, and that it plans to produce up to $500 billion of AI infrastructure in the U.S. over four years with partners including TSMC, Foxconn, Wistron, Corning, Coherent, and Amkor. Intel has made its own case in an America 250 post presenting end-to-end U.S. capabilities across design, manufacturing, and advanced packaging.

Both accounts hold up at the wafer stage but omit the same downstream step: every Blackwell die that leaves TSMC's Arizona fab still crosses the Pacific to be packaged, no HBM is manufactured or packaged on U.S. soil, and the facilities intended to close those gaps won’t start production until 2028 at the earliest.

## Lofty projects

Foxconn is building a Houston factory to produce GB300 tray modules for Nvidia, and Wistron will assemble and test Nvidia AI systems at a new facility in Fort Worth, Texas. Coherent broke ground in June on an expanded Sherman, Texas, plant that the company describes as the first volume-production 6-inch indium phosphide fab, supplying the lasers and optical components that link AI systems together.

Corning is adding more than 3,000 jobs across optical manufacturing sites in North Carolina and Texas. The post also cites an estimate from consultancy Public First that Nvidia-driven AI demand will contribute $485 billion to U.S. GDP in 2026 and support over 100,000 jobs. “AI is driving a once-in-a-generation opportunity to reinvigorate American manufacturing and supply chains,” said Nvidia’s Jensen Huang in the post.

Meanwhile, Intel's post lists R&D and manufacturing across Oregon, Arizona, New Mexico, and California, describes Ohio as “a planned site,” and devotes most of its length to workforce programs, K-12 AI education, and the company’s America250 partnership. Neither post addresses where the most advanced AI processors are actually assembled into finished chips.

## The Pacific round-trip

Nvidia and TSMC produced the first Blackwell wafer at Fab 21 near Phoenix last October, and the site has since moved to volume output of Blackwell silicon on TSMC's 4NP node, the custom 4nm-class process built for Nvidia. On the other side of the Phoenix metro area, Intel's Fab 52 became fully operational in the same month as the first high-volume home of Intel 18A, and Naga Chandrasekaran, Intel's chief technology and operations officer, told *CNBC* in December that the fab is capable of more than 10,000 18A wafer starts per week. Panther Lake reached broad availability in January, Clearwater Forest is due in the first half of this year, and 18A yields are expected to reach industry-standard levels in early 2027, which I covered in my examination of Intel's fab roadmap.

This ultimately means that leading-edge logic wafers are now being fabbed in the U.S. by two companies on two competing nodes. That’s a genuine change and, by any measure, a monolithic achievement when compared to the start of the decade, and neither company overstates that in their corporate blogs.

However, a Blackwell data center GPU pairs two reticle-sized compute dies with eight stacks of HBM3e on a silicon interposer using TSMC's CoWoS-L packaging, and all of TSMC's CoWoS capacity is located in Taiwan. TSMC’s U.S. facilities currently send 100% of their chips to Taiwan for packaging, including wafers fabbed in Phoenix. A Blackwell die fabbed in Arizona therefore travels roughly 7,000 miles to be diced, stacked, and mounted, then travels onward through system assembly before any of it returns to a U.S. data center.

As for HBM, every stack in production today comes out of SK hynix and Samsung facilities in South Korea or Micron's fabs in Taiwan and Japan, and the ABF substrates beneath the interposer are similarly concentrated in Japan and Taiwan. No U.S. facility currently manufactures or packages HBM. The one company running advanced packaging at scale on U.S. soil is Intel, whose Foveros operation in New Mexico handles its own 3D-stacked products and has started attracting outside interest; Google has reportedly booked Intel to package more than 3 million TPUs in 2028. Intel doesn’t currently appear anywhere in Nvidia's list of manufacturing partners.

## Nothing before 2029

Amkor also broke ground on its Peoria, Arizona campus last October, a $7 billion, two-phase project with up to 750,000 square feet of cleanroom, roughly $400 million in CHIPS Act funding, and Apple and Nvidia signed as lead customers. Its first factory will be completed in mid-2027, with production beginning in early 2028. TSMC formalized the relationship on June 16th, signing a 10-year agreement under which it will procure packaging and test services from Amkor, while TSMC executives said in April that the foundry's own Arizona packaging facility will bring CoWoS and 3D-IC capacity online before 2029.

SK hynix began initial work in April on its $3.87 billion advanced packaging plant in West Lafayette, Indiana, targeting mass production of HBM4E and HBM5 in the second half of 2028, the same window Amkor’s aiming for. The timing means the entire Blackwell family, and likely the first Rubin generation, will complete their product lifecycles without a fully domestic manufacturing path. The first AI accelerators that can be fabbed, packaged, and fitted with U.S.-packaged memory without leaving the country will be HBM4E-era parts arriving around 2028 to 2029.

Unfortunately, the Section 48D advanced manufacturing tax credit, raised to 35% last July, doesn’t apply to projects whose construction begins after December 31st, 2026, which gives Coherent's June groundbreaking, SK hynix's April piling work, and Amkor's October start a shared fiscal deadline if they want to benefit from it.

As for Foxconn and Wistron’s Houston and Fort Worth plants, they’ll receive GPUs packaged in Taiwan and assemble them into trays, racks, and systems on U.S. soil. It’s that type of assembly work that’s carrying most of the $500 billion figure, which counts the value of AI infrastructure produced rather than capital spent on factories. Wafers are American, racks are American, but everything in between isn’t. Whether that changes on schedule is a question for 2028, and it depends highly on two packaging campuses in Arizona and one in Indiana meeting their deadlines.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
