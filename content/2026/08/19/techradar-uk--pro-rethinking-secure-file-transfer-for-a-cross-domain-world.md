---
title: Rethinking secure file transfer for a cross-domain world
source_url: https://www.techradar.com/pro/rethinking-secure-file-transfer-for-a-cross-domain-world
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-19T21:32:09Z'
published: '2026-08-19T00:00:00Z'
description: Secure file movement demands continuous validation and inspection
image: https://cdn.mos.cms.futurecdn.net/snacLhKPDncvV3JtXYyw7M-2560-80.jpg
---

![A portion of the globe with dotted lights criss-crossing the image connecting the countries](https://cdn.mos.cms.futurecdn.net/snacLhKPDncvV3JtXYyw7M.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

The UK's National Cyber Security Centre recently issued a blunt warning to government and industry alike, warning that many systems are now connected "in ways their designers never anticipated", built on protocols never intended to withstand the sophistication of today's attackers.

That warning applies to all organizations relying on cross-domain processes to move data between environments with different security levels, and especially to complex cyber-physical systems where data flows between standard IT and operational technology (OT) assets.

File transfer is one of these fundamental processes but remains one of the most often overlooked.

SVP International at OPSWAT.

Every invoice sent to a supplier, every firmware update pushed to a factory floor, every report shared with a regulator is data crossing between systems with different levels of trust.

For years, file transfer security has been treated as a solved problem. Enterprises were happy to encrypt the channel, confirm delivery, and move on. That approach made sense when systems were simpler, and threats moved more slowly. However, it no longer reflects reality.

## Why perimeter-based trust no longer holds

Most file transfer platforms were never built with security as the primary goal. They were built to move data reliably between systems, encrypt the connection, confirm that a file arrived, and log that the job was done. Whether the file itself was safe was rarely part of the equation.

That gap provides a consistent way for cyber attackers to gain a foothold in their targets' systems. A file transfer platform sits between organizations by design, trusted by both sides precisely because it's meant to be routine infrastructure.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The traditional Managed File Transfer (MFT) model is built to automate file delivery, not to defend against attack. As such, it leaves the process exposed to a familiar set of threats, from man-in-the-middle interception and credential theft to malware covertly embedded in an otherwise ordinary file. Attackers don't need to break the platform itself, only to exploit the assumption that whatever moves through it can be trusted.

As we've seen with incidents like 2023's MoveIT supply chain cyberattack and last year's SharePoint breach, a single vulnerability in a widely used transfer tool can give attackers access to thousands of organizations at once, simply because every one of them assumed the platform itself could be trusted.

That assumption is exactly what attackers are counting on. Securing the channel a file travels through was never the same as securing the file.

## The shrinking window to respond

File security has always been a blind spot, but it's become much more critical in recent years as the attack lifecycle continues to accelerate. Newly disclosed vulnerabilities are now routinely exploited within 48 hours of becoming public, leaving little room for patch management by organizations to prepare, or even notice before they're targeted.

Detection, by contrast, still moves comparatively slowly. Breaches involving file-based attacks can go unnoticed for months, giving an intruder ample time to move laterally, extract data, or embed themselves further into connected systems before anyone realizes something is wrong.

It's not simply that attackers are fast, but that most organizations still treat file movement as something to review after the fact rather than control at the point of entry. By the time a malicious file is identified, the damage has often already been done.

This is why proactive, layered controls around every file entering or leaving the business matter more than ever. Waiting to react is not a viable strategy.

## Establishing continuous file verification

Closing this gap means shifting towards a security-first MFT process, where every file, user, and workflow is treated as a potential point of exposure rather than assumed safe by default.

Prevention is by design, rather than protection bolted on afterwards as with most traditional MFT models. And that starts with looking inside the file, not just authenticating the channel it arrives through.

Deep content inspection examines the file's actual structure, identifying hidden or malicious elements that a simple scan would miss. Alongside this, automated vulnerability detection and malware prevention should apply to every file by default, not as an optional extra reserved for high-risk transfers. Even the most innocuous file can now serve as a powerful attack vector – in fact, threat actors are counting on it.

Likewise, savvier attackers are actively designing payloads to evade detection, so standard processes need backup. Potentially malicious files need to be tested in a safe, isolated environment where their behavior can be observed before they ever reach a live system. This kind of sandboxing catches clues missed by reputation checks and static scanning, revealing intent rather than simply checking for known signatures.

A Content Disarm and Reconstruction (CDR) process is a valuable addition here, deconstructing files and sanitizing them by removing any active content without harming function.

However, none of this works as a single checkpoint. Each of these controls needs to feed into a continuous process, where a file is validated at every stage of its journey rather than cleared once and trusted from that point on. These capabilities should also be paired with constant monitoring and detailed audit visibility, so that if something does slip through, organizations know exactly what moved, where it went, and what it touched.

As a result, organizations can reliably build confidence in data as it crosses between environments, rather than assuming that confidence once and carrying it forward unchecked.

## Closing the loop on trust

The NCSC's warning and guidance on cross-domain systems point to the same conclusion: security built on fixed boundaries can no longer keep pace with how data actually moves.

File transfer is where that principle emerges most often in daily practice. Trust that was once given on principle must now be earned at every crossing. That shift, more than any single tool, is what will define resilient file transfer going forward.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
