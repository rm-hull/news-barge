---
title: 9 Key LLM Inference Metrics Explained in 5 Minutes
source_url: https://www.kdnuggets.com/9-key-llm-inference-metrics-explained-in-5-minutes
source_site: KDnuggets
source_slug: kdnuggets
description: Learn how to measure LLM inference performance using key metrics and
  formulas for latency, token generation speed, and system load.
image: https://www.kdnuggets.com/wp-content/uploads/KDn-Bala-Key-LLM-Inference-Metrics-Explained.png
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-14T16:58:47Z'
categories:
- Technology & Software
- Science
people:
- Bala Priya
locations:
- India
organisations:
- E2E
- GPU
- ITL
- Second RPS
---

# 9 Key LLM Inference Metrics Explained in 5 Minutes

Learn how to measure LLM inference performance using key metrics and formulas for latency, token generation speed, and system load.

![9 Key LLM Inference Metrics Explained in 5 Minutes](https://www.kdnuggets.com/wp-content/uploads/KDn-Bala-Key-LLM-Inference-Metrics-Explained.png)

## Introduction

A high token throughput doesn't necessarily translate to a fast user experience in a large language model (LLM) application. The first token may take too long to arrive, or subsequent tokens may stream too slowly, especially under concurrent load. Throughput alone doesn't capture these differences.

LLM inference metrics help break performance down into measurable components, from the initial response delay to token generation speed and overall system load. This article covers nine key metrics, their formulas, and how to use them to evaluate latency, identify bottlenecks, and track performance over time:

* Per-request latency: time to first token (TTFT), end-to-end latency (E2E), token generation time, time per output token (TPOT), and inter-token latency (ITL)
* Latency across many requests: mean, median, and tail percentiles
* Server load: requests per second (RPS) and tokens per second (TPS)
* Service quality: goodput

We start with the timeline of a single request.

## Reading a Request Timeline

Four values define most of the latency metrics below. The value \( t\_{\text{send}} \) is the moment the request leaves the client, \( t\_{\text{first}} \) is the arrival time of the first output token, \( t\_{\text{last}} \) is the arrival time of the last output token, and \( N\_{\text{out}} \) is the number of output tokens. ITL also needs the arrival time \( t\_j \) of each individual output token, where \( t\_1 = t\_{\text{first}} \) and \( t\_{N\_{\text{out}}} = t\_{\text{last}} \).

Laid on a timeline, the three timestamps cut a request into two segments:

![Request timeline: wait for first token, token streaming, and whole request](https://www.kdnuggets.com/wp-content/uploads/kdn-bala-inference-request-timeline-1-scaled.png)

Before \( t\_{\text{first}} \), the request may wait in a queue, and then the server runs prefill, which processes the prompt and produces the first token. After \( t\_{\text{first}} \), the server runs decode and emits tokens one step at a time, usually one token per step. Each latency metric below measures one of these segments or the whole span.

## Measuring Latency

The first six metrics describe how long a user waits, for one request and then across many.

#### 1. Time to First Token

TTFT is the delay between sending a request and receiving the first output token. It includes network travel, any wait in the server queue, and the prompt-processing step, so it grows with server load and with prompt length.

\[  
\text{TTFT} = t\_{\text{first}} - t\_{\text{send}}  
\]

Interactive chat applications watch this number most closely, because it sets how long the user stares at a blank screen.

#### 2. End-to-End Latency

E2E latency is the total wait, from sending the request to receiving the last token.

\[  
\text{E2E} = t\_{\text{last}} - t\_{\text{send}}  
\]

It is the sum of the first-token wait and the streaming time that the next metric measures.

#### 3. Token Generation Time

Token generation time is the duration of the streaming segment: how long the server takes to deliver every token after the first.

\[  
\text{TokenGen} = t\_{\text{last}} - t\_{\text{first}} = \text{E2E} - \text{TTFT}  
\]

Token generation time grows with the number of output tokens, so judge the speed of the stream with TPOT (discussed next), which divides that length out.

#### 4. Time per Output Token

**TPOT** is the average time between output tokens after the first one. It spreads the token generation time evenly over the tokens that follow the first.

\[  
\text{TPOT} = \frac{\text{E2E} - \text{TTFT}}{N\_{\text{out}} - 1} = \frac{\text{TokenGen}}{N\_{\text{out}} - 1}  
\]

The first token belongs to TTFT, which is why the denominator is \( N\_{\text{out}} - 1 \), and why TPOT is undefined for a reply with a single token. **Benchmarking tools** disagree on details here: some include TTFT in the average, and some use ITL as another name for TPOT. Confirm the definition before comparing results across tools.

#### 5. Inter-Token Latency

ITL is the gap between two consecutive output tokens. A request with \( N\_{\text{out}} \) tokens has \( N\_{\text{out}} - 1 \) gaps, and each gap is its own measurement.

\[  
\text{ITL}\_j = t\_{j+1} - t\_j, \quad j = 1, \dots, N\_{\text{out}} - 1  
\]

For one request, the mean of its ITL values equals its TPOT. Across \( R \) requests, the two averages weight the data differently. Writing \( N\_i \) for the output tokens of request \( i \), the mean ITL counts every gap once, and the mean TPOT counts every request once:

\[  
\overline{\text{ITL}} = \frac{\sum\_{i=1}^{R} \sum\_{j=1}^{N\_i - 1} \text{ITL}\_{i,j}}{\sum\_{i=1}^{R} (N\_i - 1)}  
\qquad  
\overline{\text{TPOT}} = \frac{1}{R} \sum\_{i=1}^{R} \text{TPOT}\_i  
\]

A few long requests dominate the first average, and the second gives short and long requests equal say. ITL also keeps every individual gap, which is where a stall in the stream shows up.

#### 6. Mean, Median, and Tail Percentiles

Latency varies from request to request, so one number per request becomes a distribution across many requests.

* The mean is the average of all values and follows outliers
* The median, also called P50, is the value that half of the requests fall at or below and reflects the typical user
* P99 is the value that 99% of requests fall at or below and shows the tail, with P90 and P95 as softer versions

Apply all three to TTFT, TPOT, and E2E separately.

With the \( N \) measured values sorted in ascending order as \( x\_{(1)} \le x\_{(2)} \le \dots \le x\_{(N)} \), the nearest-rank method gives:

\[  
\bar{x} = \frac{1}{N} \sum\_{i=1}^{N} x\_i  
\qquad  
P\_k = x\_{\left(\left\lceil \frac{k}{100} N \right\rceil\right)}  
\]

Compute each percentile from the raw samples of all servers combined, because an average of per-server P99 values is not the P99 of the combined traffic.

## Measuring Throughput and Goodput

The last three metrics describe the server as a whole, over a measurement window from \( t\_{\text{start}} \) to \( t\_{\text{end}} \).

#### 7. Requests per Second

RPS counts the requests the server completes per second of wall-clock time.

\[  
\text{RPS} = \frac{N\_{\text{completed}}}{t\_{\text{end}} - t\_{\text{start}}}  
\]

RPS ignores how much work each request carries, so compare it only across runs with the same mix of prompt and output lengths.

#### 8. Tokens per Second

TPS counts the tokens the server processes per second across all active requests. It has an output form and an input form. Writing \( N\_{\text{prompt},i} \) for the prompt tokens of request \( i \):

\[  
\text{TPS}\_{\text{out}} = \frac{\sum\_{i} N\_{\text{out},i}}{t\_{\text{end}} - t\_{\text{start}}}  
\qquad  
\text{TPS}\_{\text{in}} = \frac{\sum\_{i} N\_{\text{prompt},i}}{t\_{\text{end}} - t\_{\text{start}}}  
\]

State which form a quoted number uses, since a workload with long prompts and short replies can post a high input TPS while producing few output tokens.

#### 9. Goodput

Goodput is the rate of successfully completed requests that meet your service-level objectives (SLOs), which is how serving benchmarks such as **vLLM** compute it. An SLO is a latency limit, such as a ceiling on TTFT or TPOT, and a request counts only when it satisfies every limit. The**DistServe paper** uses the term for a capacity instead: the maximum request rate a GPU sustains within its latency constraints. Writing \( s\_{\text{ttft}} \), \( s\_{\text{tpot}} \), and \( s\_{\text{e2e}} \) for those limits, request \( i \) is good when:

\[  
\text{TTFT}\_i \le s\_{\text{ttft}} \;\land\; \text{TPOT}\_i \le s\_{\text{tpot}} \;\land\; \text{E2E}\_i \le s\_{\text{e2e}}  
\]

Counting the good requests and dividing by the window gives goodput:

\[  
\text{Goodput} = \frac{N\_{\text{good}}}{t\_{\text{end}} - t\_{\text{start}}}  
\]

Goodput never exceeds RPS, and the gap between them is the rate of requests that missed at least one target.

## Wrapping Up

Inference metrics split one request into a first-token wait and a stream, then describe how a server performs across many requests and how many of them meet your targets. The table below summarizes them:

| Metric | Formula | Answers |
| --- | --- | --- |
| TTFT | \( t\_{\text{first}} - t\_{\text{send}} \) | How long the reply takes to start |
| E2E | \( t\_{\text{last}} - t\_{\text{send}} \) | How long the whole reply takes |
| Token generation time | \( t\_{\text{last}} - t\_{\text{first}} \) | How long the stream lasts |
| TPOT | \( \frac{\text{E2E} - \text{TTFT}}{N\_{\text{out}} - 1} \) | How fast tokens arrive on average |
| ITL | \( t\_{j+1} - t\_j \) | Whether the stream stalls |
| Mean, median, P99 | \( x\_{(\lceil 0.99 N \rceil)} \) for P99 | How typical and slowest requests compare |
| RPS | \( \frac{N\_{\text{completed}}}{t\_{\text{end}} - t\_{\text{start}}} \) | How many requests complete per second |
| TPS | \( \frac{\sum\_i N\_{\text{out},i}}{t\_{\text{end}} - t\_{\text{start}}} \) | How many tokens the server produces per second |
| Goodput | \( \frac{N\_{\text{good}}}{t\_{\text{end}} - t\_{\text{start}}} \) | How many requests meet every SLO |

**References and Further Learning**:

* Key Metrics for LLM Inference | Modular Handbook
* Benchmarking Metrics for LLM Inference
* DistServe: Disaggregating Prefill and Decoding for Goodput-Optimized Serving
* LLM Inference Performance Engineering: Best Practices

Happy learning!

**Bala Priya** is a developer, educator, and technical writer based in India. She writes about programming, data science, machine learning, and AI, with a focus on making complex technical ideas practical and approachable.
She creates tutorials, how-to guides, and deep dives that help developers build, solve problems, and understand complex technical concepts. Her technical interests include LLM applications, agentic AI, graph algorithms, computer vision, explainable AI, and ML systems.
When she’s not writing or coding, Bala is usually reading classic literature, epic fantasy, or speculative fiction. She also enjoys talking about books, learning new things, and sharing what she learns with the developer community.
