---
title: Researchers used AI-assisted code to undetectably tamper with data from computerized
  scans of physical DNA evidence produced by widely used crime-lab machines — vulnerable
  DNA files ‘lack the same level of tamper-evident markings that we require for a
  paper bag’
source_url: https://www.techradar.com/pro/security/weve-been-behind-the-ball-for-so-long-experts-say-dna-samples-from-crime-scene-forensics-can-be-modified-and-even-switched-using-an-ai-tool
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-03T15:11:54Z'
published: '2026-08-03T00:00:00Z'
description: Researchers were able to modify DNA samples from crime-scene forensics
  using an AI tool.
image: https://cdn.mos.cms.futurecdn.net/HWb2cSJ4Mb5mxx8ebgiAzH-1920-80.jpg
---

![A forensic police officer examines a smartphone as evidence in a murder case at a forensic laboratory](https://cdn.mos.cms.futurecdn.net/HWb2cSJ4Mb5mxx8ebgiAzH.jpg) 

- **Researchers discover critical vulnerability in forensic software that allows the undetectable modification of DNA samples on crime-scene evidence**
- **The vulnerability allows much of the crime-scene evidence from the past 30 years to be modified**
- **A patch is in the works, and the company responsible for the software says that digital signatures have been implemented to monitor for modification attempts**

A group of forensic and computer scientists have raised concerns about the security of software used by top US crime labs to analyze DNA evidence.

By using an AI model, the researchers were able to undetectably modify computerized scans of physical DNA evidence, exclusive *Wall Street Journal* reported. As the vulnerability relates to digital files made by crime labs since 1995, the vulnerability places 30 years of crime files at risk of being tampered with.

“Effectively, what we have are data files that are legitimately referred to as the gold standard of forensic science that lack the same level of tamper-evident markings that we require for a paper bag,” said Laura Gaydosh Combs, a University of New Haven professor and forensic scientist who contributed to the research.

## No known instances of ‘undetectable’ exploitation

The researchers disclosed the vulnerability in May. Thermo Fisher Scientific, the company that builds the crime-lab equipment used across most US facilities, privately acknowledging the vulnerability in July 2026. The company said that a fix is currently in progress.

In a separate note to customers, Thermo Fisher Scientific said there were no known instances of the vulnerability being exploited.

But the researchers themselves have said that they could not find a way to detect if tampering had taken place. The vulnerability was tested by Nathan Adams, a systems engineer at Forensic Bioinformatics. In just 45 minutes, Adams managed to successfully exploit the vulnerability using Anthropic’s Claude, and modify a file.

Despite some of the files being sealed using a more advanced encryption algorithm, Adams was able to find and use a decryption key available on the internet to crack into these files.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The researchers highlighted that by using AI tools to gain the necessary skills and tools, a hacker could abuse the vulnerability to add or remove DNA profiles from crime-scene evidence. Therefore allowing a suspect’s DNA to be removed, or an innocent person’s DNA added.

“Lessons learned from other industries haven’t been imported into forensic science in a serious way,” said Sarah Chu, the director of policy and reform at the Perlmutter Center for Legal Justice who worked on the research. “We’ve been behind the ball for so long. That kind of all rolls downhill into this incident.”

The lack of any centralized regulator on forensics has left over 200 labs with a patchwork of security measures, Chu added.

In a statement to the *WSJ*, Thermo Fisher Scientific said, “We have been working closely with the U.S. Cybersecurity and Infrastructure Agency since the software issue was raised. We appreciate the work of forensic researchers on this topic, and we have released a software update that implements the use of digital signatures to add an extra layer of protection that moving forward will help customers verify that data files have not been modified.”

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
