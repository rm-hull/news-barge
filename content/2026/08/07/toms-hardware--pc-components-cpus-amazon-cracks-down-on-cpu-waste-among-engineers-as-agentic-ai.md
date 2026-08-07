---
title: Amazon cracks down on 'CPU waste' among engineers as agentic AI crunch intensifies
  — CPU demand makes low-utilization EC2 instances a hot commodity
source_url: https://www.tomshardware.com/pc-components/cpus/amazon-cracks-down-on-cpu-waste-among-engineers-as-agentic-ai-crunch-intensifies-cpu-demand-makes-low-utilization-ec2-instances-a-hot-commodity
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-07T17:04:45Z'
published: '2026-08-07T00:00:00Z'
description: What used to take engineers a few hours can now take several days.
image: https://cdn.mos.cms.futurecdn.net/NQC73QYBQQXmqRgadqnzt6-1320-80.png
---

![AWS](https://cdn.mos.cms.futurecdn.net/NQC73QYBQQXmqRgadqnzt6.png) 

Amazon Web Services is cracking down on internal use of EC2 instances among its engineers. In May, the company reportedly met with engineers and told them to reduce CPU waste to ensure AWS has enough CPU capacity to meet customer demand, The Information reports. The message comes as demand for CPUs in the data center has hit a fever pitch, with the traditional eight-to-one or four-to-one ratio of GPUs to CPUs moving closer to parity.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


EC2 instances make up a large chunk of the modern internet, and they're used in private deployments, as well. Traditionally, AWS engineers have been able to spin up their own instances for development, leveraging the relatively low CPU utilization required for web infrastructure to use more virtual machines. Now, engineers say they're waiting days to get access when they previously could get access within hours. One engineer told *The Information* that they've never had to wait this long for an instance, even after several years of working at Amazon.

Amazon deploys several different types of CPUs in EC2 instances, including AMD and Intel options and its __relatively new Graviton5 chip__. Graviton5 is Amazon's most powerful CPU to date, and it uses an Arm-based architecture along the lines of Nvidia's Vera CPU and __Arm's own AGI__.

The increased demand for CPU comes on the back of AI agents, a new paradigm in productivity that even companies as large as Amazon are struggling to reckon with. Last month, for instance, a coding agent blew through __$1.8 million in token costs at Amazon, surpassing a development budget by 860%__.

Much of the AI infrastructure currently in place is designed around inference, a workload that's accelerated by GPUs. With the four-to-one ratio, the CPU served as a way to keep the GPUs fed, and nothing more. However, agentic workloads are much more complex. They often involve tool calls that run on the CPU, as well as more complex orchestration of inference on GPUs. This is what has brought CPUs center stage in the agentic era. Intel, AMD, and others have echoed what we've heard from memory and storage companies over the past several months: the demand is so high for CPUs that most companies will take whatever they can get.

The major players are capitalizing on that demand. AMD just recently unveiled its portfolio of __Zen 6 'Venice' CPUs for the data center__, marking the first time AMD has launched a new architecture in the data center before the client market in decades. Nvidia has also pivoted its messaging away from accelerators and __toward its new Vera CPU__, vying to stake its claim in an expanding market of agentic AI infrastructure.

Although Amazon is wrestling with CPU capacity across its internal engineers and external customers, The Information reports that shortages are largely a problem for spot instances. A consultant told the outlet that contracted capacity hasn't experienced any shortages.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.
