---
title: Expert warns this dangerous Microsoft Word worm can burrow into Copilot and
  cause havoc — here's what we know
source_url: https://www.techradar.com/pro/security/expert-warns-this-dangerous-microsoft-word-worm-can-burrow-into-copilot-and-cause-havoc-heres-what-we-know
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-01T21:06:11Z'
published: '2026-08-01T00:00:00Z'
description: A copilot-enabled exploit?
image: https://cdn.mos.cms.futurecdn.net/GxSNrV6MwnmZHmLEQHF58B-1600-80.jpg
---

![Copilot keyboard button](https://cdn.mos.cms.futurecdn.net/GxSNrV6MwnmZHmLEQHF58B.jpg) 

- **Instructions hidden as white text in a Word document can make Microsoft 365 Copilot silently alter the file it is drafting and copy the instructions into the output**
- **Each poisoned document becomes a carrier, so the attack spreads through ordinary internal workflows without the original malicious file and needs no macros, malware, or code execution**
- **Microsoft has shipped two mitigations across a 144-day disclosure, including a model upgrade, and the attack was still reproducible by the researcher**

A security researcher has published a proof of concept showing that instructions hidden inside a Word document can cause Microsoft 365 Copilot to silently alter the file it is drafting, then copy those same instructions into the finished document, so the next person to use it becomes a carrier too.

Håkon Måløy, a data scientist with a doctorate in applied machine learning, disclosed the technique as the third installment of his Context Collapse series, after a 144-day coordinated disclosure with the Microsoft Security Response Center.

The reason this is being reported ahead of a fix is that it still works despite multiple attempts by Microsoft, as he notes that no robust mitigation for the broader vulnerability class is currently available.

## A clever attack designed around Copilot's approach to text

The underlying attack belongs to a family known as cross-domain prompt injection, or XPIA. An attacker writes instructions in a natural-language document, formats them as white text on a white background at a small point size, and shares the file.

Because Copilot for Word strips formatting before passing text to the underlying language model, the model reads text the human never sees. This is true even for documents that are not opened by the user on purpose: The attack can trigger either when a user manually attaches a document to Copilot or when Copilot, working in Work IQ mode, searches the user's OneDrive for relevant files and finds the malicious one on its own.

It is also more dangerous than other exploits because of one key element: propagation. The hidden prompt in Måløy's proof of concept had two parts. One instructed Copilot to alter the document being drafted, in his demonstration halving every financial figure in a quarterly report.

The other instructed Copilot to copy the prompt into the new document and conceal it, framed innocuously as source tracking and readability formatting. Copilot did both, appending the instructions in white text and mentioning neither action to the user.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The disclosure timeline is the most uncomfortable part of the report. Måløy reported to MSRC on March 6 2026. Microsoft confirmed the behavior on March 31 and shipped a first mitigation in early April via a reworked Edit with Copilot experience, which successfully blocked his original prompt wording. He reproduced the attack with different wording the same week, and a second case was opened.

The second fix, on July 14, consisted of upgrading the underlying model to GPT-5.5. Måløy broke it the following day using GPT-5.6, then voluntarily offered Microsoft a further two-week delay to attempt another mitigation. The class still reproduced on the disclosure date, indicating that although a fix is in the works, the exploit is still possible to run.

## A complicated issue that lacks a proper resolution

The issue goes far beyond Microsoft Word: an AI assistant must ingest untrusted content to determine whether it is relevant or hostile. But the content enters the same context window as the system prompt and the user's actual request, so by the time the model evaluates whether the text is an attack, the attacker's tokens have already shaped that evaluation.

As Måløy puts it, "the content being inspected participates in the act of inspection."

Microsoft confirmed it had reviewed the findings in a statement to *The Register* but stopped short of indicating a timeline for a complete fix:

“We have addressed the findings reported by the researcher and thank them for working with us through coordinated vulnerability disclosure," the company said.

"To address this class of risk, we use a defense-in-depth strategy with safeguards that block malicious instructions at multiple points and help keep tasks aligned with users’ requests. We are continuously strengthening these safeguards as the technology and threat landscape evolve. We encourage customers to install the latest updates, use multiple layers of security protection, treat content from unknown sources with caution, and review AI-generated content before using or sharing it.”

Måløy's recommendations are to treat externally sourced documents as untrusted when using them with Copilot, review attachments before starting an AI-assisted draft, and review Copilot's output carefully before sharing or reusing it.

He also suggested that generated documents should carry provenance metadata that records source material and model edits, which would not prevent injection but would make an infection traceable after the fact.

With Copilot extending further into agentic products that create and manipulate documents with less human oversight, the scope of how exploits like this could affect workflows (and users) will widen rather than narrow, and a complete solution is not yet in sight.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
