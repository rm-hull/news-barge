---
title: MicroSD card torture test writes 133 petabytes of data across 351 cards over
  three years — cards tested to failure reveal SanDisk as the outlier with 6 failures
  of the 7 tested
source_url: https://www.tomshardware.com/pc-components/microsd-cards/microsd-card-testing-database-celebrates-third-anniversary-with-133-petabytes-of-data-written-across-4-6-million-cycles-hundreds-of-cards-tested-to-failure-reveal-sandisk-as-the-outlier-with-6-failures-of-the-7-tested
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-19T13:09:47Z'
published: '2026-08-19T00:00:00Z'
description: Which microSD card brands and models are worth your money?
image: https://cdn.mos.cms.futurecdn.net/zSC7KamvrhmL3aumd56atn-1920-80.jpg
---

![Best MicroSD Express Cards](https://cdn.mos.cms.futurecdn.net/zSC7KamvrhmL3aumd56atn.jpg) 

There are many different options available if you want to buy a microSD card, but which one of these lasts the longest? Tech enthusiast Matt Cole wanted to find out, so he set up a torture rig in 2023 to put various cards through their paces and recently released an update on the status of his project on the r/DataHoarder subreddit. Cole said that he has a total of 351 microSD cards in his collection coming from 52 different brands and 111 unique models. Of these, 177 have already been tested until they completely stopped working, have become read-only, or more than half of the sectors on the card have experienced verification failure. Another 107 units are currently being put through their paces, while a further 67 are waiting for a microSD card slot to open up.

Cole has so far tested 200 cards last year, meaning 84 microSD's have failed in the intervening months. While this might sound disastrous for any manufacturer, we should note that the testing conditions are quite extreme, and it’s rare that a user would find themselves in these circumstances. If you want to check out the raw data, Cole’s database is publicly viewable on his website, but he’s also shared some of his observations after three years of testing. First, he divided his microSD cards into three categories: consumer-grade, high-endurance, and industrial-grade. Consumer-grade microSD cards are the typical cards you can get off Amazon, while high-endurance models are often labeled as such (or some other similar wording). Lastly, industrial-grade microSD cards are those that are specifically designed for heavy-duty use and would often come with a data sheet and an endurance claim.

According to the test results, the average consumer-grade microSD withstood 10,000 program/verify/erase cycles, with PNY, Kingston, Delkin Devices, Lexar, and Samsung rounding out Cole’s top five brands.

| Brand | Failed | Total Tested | Average Lifespan (Days) | Average Cycles | Total Written Data (PB) | 
|---|---|---|---|---|---|
| PNY | 1 | 10 | 643 | 15,700 | 11.5 | 
| Kingston | 3 | 12 | 694 | 23,500 | 11.6 | 
| Delkin Devices | 0 | 3 | 662 | 13,500 | 5.1 | 
| Lexar | 3 | 8 | 684 | 15,800 | 5.8 | 
| Samsung | 3 | 10 | 553 | 11,100 | 7.2 | 

Interestingly, Amazon Basics received an honorable mention, with none of the microSD cards being tested failing yet. They’ve been running for 788 days now, with 16,600 cycles and a total of 4.2PB of data written on them. The only reason they didn’t make the main list is that they’re technically generic or off-brand microSD cards and Amazon could replace the NAND chips used in these cards anytime, thereby making the survey results moot. There’s a separate shorter list for high-endurance and industrial-grade cards, given that the sample size is just smaller and the latter is significantly more expensive than all the other microSD cards available here.

| Brand | Failed | Total Tested | Average Lifespan (Days) | Average Cycles | Total Written Data (PB) | 
|---|---|---|---|---|---|
| TEAMGROUP (High-Endurance) | 0 | 2 | 404 | 17,300 | 2.2 | 
| Transcend (High-Endurance) | 0 | 3 | 760 | 17,000 | 3.2 | 
| SanDisk (High-Endurance) | 6 | 7 | 452 | 16,200 | 4.7 | 
| Samsung (High-Endurance) | 1 | 3 | 822 | 18,800 | 1.8 | 
| Kingston (Industrial-Grade) | 2 | 3 | 77+ | 141,600 | 3.4 | 

He also listed some of the worst performers per category from popular brands, like ADATA, Gigastone, Micro Center, Silicon Power, and, surprisingly, SanDisk, although Cole avoided no-name brands, since most users don’t expect much from them.

Doing all these tests simultaneously and continuously is no joke, and we see this in Cole’s setup. He runs a single Beelink Mini-S with an Intel N95 CPU, 8GB of RAM, and a 500GB SSD, five TRIGKEY Green G4 mini-PCs and one TRIGKEY K-N100 with an Intel N100 CPU, 16GB of RAM, and a 500GB SSD, and an AOOSTAR mini-PC with an Intel N150 CPU paired to 12GB of RAM and a 500GB SSD. Aside from these mini-PCs, he also has an MSI GE62VR-7RF Apache Pro laptop with an Intel Core i7-7700HQ, 32GB of RAM, and a 1TB SSD, a Lenovo IdeaPad Y850 laptop with an Intel Core i7-3630QM, 8GB of RAM, and a 1TB SSD, and an ASUS ROG Strix Hero II GL504GM laptop with an Intel i7-8750H, 32GB of RAM, and a 500GB SSD.

Running this experiment can get expensive as Cole needs to purchase all the microSD cards himself (unless someone donates them), especially at a time when memory card prices are skyrocketing. Aside from that, he also needs to purchase and maintain all that testing hardware. Although these are either relatively affordable mini-PCs or used gaming laptops, the cost of acquiring and running all these units will eventually stack up.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

- 
It is great to see an article like this on TH. This kind of stress testing is done all the time in engineering design and product quality assessment, and it is a great tool for finding where your margins are for a given stress type. If you test to failure, it is call HALT testing, and if you use it to act as hurdle, such as for manufacturing, it is called HASS test. In manufacturing these tests might be burn-in testing or hipot testing (insulation system verification).Reply
 
 Knowing that Flash memory lifespan is also temperature dependent, the testing done in the article would have been even more interesting if the internal controller temp could be recorded while it was running, or conversely, if the ambient temperature had been set differently with two samples of each memory card (but - twice the cost of the study). If you move two stressors around at the same time, it is called a MEOST test.
 
 It is unfortunately that the GPU industry did not do this for the power connectors and used temperature and humidity as the stressors. They would have found that there exists a problem before even launching the product. But note - delaying a product launch is often a career damaging move at many companies. I myself have had my job threatened for stopping a product launch to fix an issue.
 
All of these concepts can be found on Wikipedia where some people have done a great job explaining the ideas. If I remember correctly, these test methods were originally proposed in US academics around the mid 1950's, but not really used in industry until the Japanese automakers started utilizing them. I have used them successfully myself many times to find difficult failure modes in designs, and chasing root failure modes in warranty cases.
