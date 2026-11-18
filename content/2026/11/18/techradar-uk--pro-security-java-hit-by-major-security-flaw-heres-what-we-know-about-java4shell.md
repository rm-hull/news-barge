---
title: Java hit by major security flaw — here's what we know about Java4Shell so far
source_url: https://www.techradar.com/pro/security/java-hit-by-major-security-flaw-heres-what-we-know-about-java4shell-so-far
source_site: TechRadar UK
source_slug: techradar-uk
description: Java4Shell enables data exfiltration and remote code execution
image: https://cdn.mos.cms.futurecdn.net/VyYgfUHgbvAsTDDYewj2Am-970-80.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-18T20:31:57Z'
categories:
- Technology & Software
people:
- Jenkins
- Luong
- Quang Long
locations:
- Calif
- Java4Shell
organisations:
- Amazon Corretto
- Apache Kafka Broker
- Apache Solr
- Atlassian Confluence
- Atlassian Jira
- Azul Zulu
- CVE-2026-114938
- Calif
- Codex AI
- Eclipse Temurin
- Elasticsearch
- Fortune
- Gerrit
- JFrog Artifactory
- Jenkins
- Keycloak
- Microsoft Build of OpenJDK
- NVD
- National Vulnerability Database
- OpenAI
- Oracle GraalVM
- Oracle GraalVM Enterprise Edition
- Oracle GraalVM for JDK
- Oracle Java SE
- PingFederate
- RCE
- Red Hat OpenJDK
- Spinnaker
- TechRadar Pro
---

![JavaScript code on a computer screen](https://cdn.mos.cms.futurecdn.net/VyYgfUHgbvAsTDDYewj2Am-970-80.jpg)

* **Researchers disclosed a critical OpenJDK memory-corruption flaw that could enable information disclosure or remote code execution**
* **The vulnerability affects multiple Java distributions and several widely used enterprise applications**
* **Oracle released patches for the issue, and organizations are urged to update immediately or apply temporary mitigations**

Security researchers discovered a critical vulnerability in the Java runtime, potentially allowing malicious actors to reveal sensitive information or run malicious code remotely.

Researcher Quang Long from Calif disclosed finding a memory corruption flaw in OpenJDK, the open-source implementation of the Java platform, which he dubbed Java4Shell. OpenJDK provides the tools users need to run Java apps, so any vulnerabilities found there could impact a wide range of software built on Java.

“Java is the world's third most popular programming language, powering 90% of Fortune 500 companies,” he said. “It is the beating heart of the modern economy. Banking, aviation, telecommunications, nearly every critical sector runs on Java, including national security systems.”

A memory corruption flaw happens when software incorrectly writes to, or modifies, areas of a computer’s memory, allowing attackers to overwrite data, access sensitive information, or run malicious code. In this case, the flaw affects OpenJDK’s Base64, a decoding functionality that converts binary data (images, files) into text using a set of 64 characters, making it easier to transmit or store data in text-based systems.

## Enterprise apps at risk

The bug is now tracked as CVE-2026-114938 and, according to the National Vulnerability Database (NVD), has a severity score of 8.1/10 (high). Calif ranks it 9.2/10 (critical). “Difficult to exploit vulnerability allows unauthenticated attacker with network access via multiple protocols to compromise Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition,” NVD says in its advisory. “Successful attacks of this vulnerability can result in takeover of Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition.”

OpenJDK versions 17.0.6 and later were said to be affected, as well as all Java distributions built from that code. That includes Oracle Java SE, Amazon Corretto, Eclipse Temurin, Microsoft Build of OpenJDK, Azul Zulu, and Red Hat OpenJDK.

It also means that some of the applications running on these distributions could be exploitable as well. So far, researchers have tested Jenkins, Atlassian Jira, Confluence, and Keycloak, and confirmed them to be vulnerable in some versions, but the list is by no means extensive.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins, and PingFederate, the researcher managed to perform unauthenticated remote code execution (RCE). For Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit, and Spinnaker, he managed to pull off authenticated RCE.

If you’re not using any of the abovementioned products, that doesn’t mean the vulnerability should be ignored. Calif managed to trigger the memory corruption vulnerability with just 64 “A” characters followed by a single equals sign (=). On older OpenJDK 17 versions, 128 “A” characters were necessary to trigger the bug. Honestly, if someone was screaming at me like that, I would probably be triggered, as well. It’s also worth mentioning that there is no universal exploit for Java4Shell - attackers must find a way in for each individual app.

## How to fix Java4Shell

It was added that the bug affects only hardware-accelerated decoding functions used on some x86-64 processors that support AVX-512 instructions.

Luong said he was inspired to look for a Java bug after the PHP2Shell discovery. Just as then, he used OpenAI’s Codex AI coding assistant to find the bug, and it only took him an hour and some $200 in tokens. AI agents also assisted with building application-specific exploitation chains, it was said.

Oracle patched CVE-2026-114938 on November 17, when it released its November Critical Security Patch Update. Users are advised to install that update without delay, but those that cannot do that are advised to disable hardware-accelerated Base64 functionality by launching OpenJDK with the -XX:-UseBASE64Intrinsics option.

They can also use -XX:UseAVX=2 to disable AVX-512 instructions if they’re running Java on x86-64 systems. Still, these are considered workarounds and temporary mitigations and are, by no means, a permanent solution to Java4Shell.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
