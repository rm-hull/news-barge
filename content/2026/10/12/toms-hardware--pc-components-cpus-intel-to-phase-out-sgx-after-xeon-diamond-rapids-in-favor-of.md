---
title: Intel to phase out SGX after Xeon Diamond Rapids in favor of TDX — confidential
  computing pivot adds trusted I/O and post-quantum crypto for agentic AI
source_url: https://www.tomshardware.com/pc-components/cpus/intel-to-phase-out-sgx-after-xeon-diamond-rapids-in-favor-of-tdx-confidential-computing-pivot-adds-trusted-i-o-and-post-quantum-crypto-for-agentic-ai
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-12T18:59:09Z'
published: '2026-10-12T00:00:00Z'
description: Diamond Rapids last to support SGX.
image: https://cdn.mos.cms.futurecdn.net/VBnZto6P3Yzh9RfNDACjGT-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Anton Shilov
- Tom
locations: []
organisations:
- Alibaba Cloud
- Canonical
- Diamond Rapids
- Get Tom's Hardware
- Google Cloud
- Google News
- IBM Cloud
- Intel SGX
- Intel TDX
- Intel TDX Connect
- Microsoft Azure
- Nvidia
- Red Hat
- Software Guard Extensions
- Tom’s Hardware
- Trust Domain Extensions
- VMware
- Volcano Cloud
- Xeon
---

![Intel Xeon 6 processor](https://cdn.mos.cms.futurecdn.net/VBnZto6P3Yzh9RfNDACjGT-1920-80.jpg)

Just five years after bringing its Software Guard Extensions (SGX) technology to its mainstream server platform, Intel on Friday announced plans to discontinue its support after its upcoming Xeon 'Diamond Rapids' CPUs and concentrate its confidential computing efforts on Trust Domain Extensions (TDX). The company will continue to support existing SGX-enabled platforms into the early 2030s, but at the same time will expand TDX capabilities to address emerging requirements of cloud computing, enterprise workloads, and agentic AI applications.

Without a doubt, data sovereignty requirements are an increasingly important factor as organizations seek to protect sensitive information from unauthorized access even when they process it on infrastructure operated by third parties. Although both Intel SGX and TDX are designed to protect sensitive information while it is being processed, they use substantially different approaches.

SGX provides hardware-protected enclaves within applications to isolate selected code and data from other software, including the operating system and hypervisor. By contrast, TDX isolates entire virtual machines from the underlying host environment, including the hypervisor and other VMs. While SGX requires developers to design or modify applications to use protected enclaves, TDX can protect existing workloads inside confidential VMs without extensive changes to individual applications, something that makes TDX particularly attractive to cloud service providers that operate large numbers of virtual machines.

While both SGX and TDX have faced numerous security vulnerabilities over the years, including side-channel attacks, privilege-escalation flaws, and attacks against their attestation mechanisms, Intel does not cite security concerns as a reason for its decision to discontinue SGX.

Intel's decision to phase out SGX reflects the industry's preference for VM-level isolation over application-specific enclaves. According to Intel, TDX provides scalability, ease of deployment, and the operational model required for widespread adoption of confidential computing. Although SGX enabled confidential computing in the data center and continues to serve security-conscious customers, Intel believes future demand will favor TDX. Diamond Rapids will therefore be the final Xeon generation to support SGX, which gives customers several years to validate alternative solutions based on TDX and migrate existing applications. Intel will continue to provide security updates and support for SGX-enabled platforms into the early 2030s, so its customers will have plenty of time to adopt TDX for new deployments.

Meanwhile, Intel plans to expand TDX capabilities with additional security technologies. These include Intel TDX Connect, which is designed to enable trusted I/O, as well as post-quantum cryptography and enhanced attestation mechanisms. Trusted I/O is particularly important for workloads that communicate with external devices, as protection of computations inside a virtual machine does not necessarily extend to data transferred between the VM and accelerators or other peripherals (read, CXL expanders, though Intel has not stated this for sure). Improved attestation will help organizations verify the integrity of protected environments, while post-quantum cryptography will help address future security threats. Meanwhile, Intel has not disclosed specific availability dates for these enhancements.

One important driver behind Intel's confidential computing strategy seems to be accelerated adoption of agentic AI. Unlike conventional applications, autonomous agents may access sensitive enterprise information, execute operations across multiple systems, and interact with other agents. Intel expects many such workloads to run on CPUs, and here TDX may offer practical advantages for agentic AI applications. Unlike SGX, TDX can protect entire agent execution environments without extensive software modifications and enable multiple agents to operate in separate, hardware-isolated VMs on shared infrastructure. For GPU-accelerated AI workloads, Intel works with Nvidia to coordinate confidential computing technologies across CPUs and GPUs to extend protection to sensitive data and AI models throughout the processing pipeline (which is obviously broader than Intel's development of custom Xeon CPUs for Nvidia).

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Intel TDX is already available through major cloud providers, including Alibaba Cloud, Google Cloud, IBM Cloud, Microsoft Azure, and Volcano Cloud. Meanwhile, Red Hat, Canonical, and VMware are adding TDX support to their software platforms to enable adoption in private clouds and enterprise environments.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
