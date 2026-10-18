---
title: Researchers train AI to detect concealed handguns using Wi-Fi signals — open-source
  WiFireNet achieves precision detection on older 802.11a standard by analyzing how
  weapons distort wireless signals
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/researchers-train-ai-to-detect-concealed-handguns-using-wi-fi-signals-open-source-wifirenet-achieves-precision-detection-on-older-802-11a-standard-by-analyzing-how-weapons-distort-wireless-signals
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-18T15:51:57Z'
published: '2026-10-18T00:00:00Z'
description: The experimental prototype cannot pinpoint the weapon's location on the
  carrier
image: https://cdn.mos.cms.futurecdn.net/kfvNwDT4D6jpoBvqVwPdcE-1920-80.webp
categories:
- Technology & Software
- Hardware
- Science
people:
- Etiido Uko
- Tom
locations: []
organisations:
- Etiido Uko
- FOI
- Google News
- PC
- Swedish Defense Research Agency
- Tom's Hardware
- Wi-Fi 8
- WiFireNet AI
---

![Researchers identify people through ordinary Wi-Fi routers with 99.5% accuracy](https://cdn.mos.cms.futurecdn.net/kfvNwDT4D6jpoBvqVwPdcE-1920-80.webp)

A group of AI researchers at the Swedish Defense Research Agency (FOI) has developed an AI system that can identify concealed handguns using Wi-Fi signals, offering a non-intrusive alternative to visible cameras and cumbersome metal detectors. Detailed in a paper posted on arXivWi-Fi on October 13, the system, called WiFireNet, analyzes channel state information from how an object distorts ambient Wi-Fi signals. The full system comprises a Wi-Fi transmitter, a Wi-Fi receiver, and the WiFireNet AI.

When ordinary Wi-Fi signals encounter an object in their path, they penetrate and bounce off in ways specific to that object, based on its shape, orientation, and material. This data, the channel state information, can be analyzed to identify the object with high accuracy. Security researchers previously disclosed a technique that lets ordinary Wi-Fi routers identify people with 99.5% accuracy.

To build the WiFireNet system, the researchers first created a dataset, dubbed the WiFire Dataset, by simultaneously recording RGB footage and the reflected Wi-Fi signals of people walking around with objects ranging from phones to handguns. The researchers then trained a deep learning model on the massive dataset, using video clips to match the visuals of a concealed handgun with its specific Wi-Fi signature, or channel state information. To ensure the system could specifically distinguish a handgun from everyday items of similar shape or material, the researchers trained it on recordings of a plastic handgun, a metal water bottle, a real metal handgun, and a phone.

After training, the final AI system, WiFireNet, could detect concealed handguns solely based on Wi-Fi CSI, with varying accuracy. In controlled trials tracking up to four moving individuals in a small indoor space, the system achieved an average handgun-detection precision of 72.5%. However, under stricter localization requirements, such as pinpointing the weapon’s exact location on the carrier, precision dropped to 53.8%. The neural network also struggles to perform accurately in unfamiliar, untested indoor layouts.

That said, the system is still experimental, with a roadmap of planned improvements. The prototype was built using a modified implementation of the older 1999 wireless IEEE 802.11a standard to establish proof of concept. Subsequent phases will use modern Wi-FI 7 and Wi-Fi 8 networks with higher-resolution CSI for better detection. The researchers made the project open source, releasing the code, models, and dataset to support further research in the field. Wi-Fi sensing is gaining popularity as an effective surveillance technology that doesn't require complex gear or setups. However, critics argue that the technology's ubiquity and the lack of regulatory frameworks raise serious privacy concerns.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD-140-80.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
