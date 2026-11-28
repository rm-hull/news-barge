---
title: Why Data Job Candidates Freeze on Questions They Already Know
source_url: https://www.kdnuggets.com/why-data-job-candidates-freeze-on-questions-they-already-know
source_site: KDnuggets
source_slug: kdnuggets
description: Pressure disrupts recall in interviews. Timed mock interviews let you
  rehearse it.
image: https://www.kdnuggets.com/wp-content/uploads/kdn-why-data-job-candidates-freeze-on-questions-they-already-know-feature.webp
published: '2026-11-25T00:00:00Z'
scraped_at: '2026-11-28T18:01:29Z'
categories:
- Technology & Software
- Science
- News & Politics
- Careers & Productivity
people:
- Nate Rosidi
- Resolving
locations:
- Las Vegas
- Phoenix
- Toronto
organisations:
- AI Interviewer
- CTE
- Las Vegas
- Phoenix
- PostgreSQL
- RANK
- The Data
- Toronto
---

# Why Data Job Candidates Freeze on Questions They Already Know

Pressure disrupts recall in interviews. Timed mock interviews let you rehearse it.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/kdn-why-data-job-candidates-freeze-on-questions-they-already-know-feature.webp)

You have written a **window function** a hundred times. Then an interviewer asks for one, a timer starts, and the syntax is gone.

Candidates who solve a problem easily at their desk often stall on the same problem in an interview. The approach is clear in their head, and they could describe it. The first line still takes three attempts, and the person watching sees every one.

From the other side of the table, a stall caused by nerves looks the same as a stall caused by missing knowledge. Both get the same score.

**Five conditions** contribute to the freeze, and each one can be practiced. We ran a 60-minute SQL mock interview with two ranking questions to see how they showed up. Both questions turned on how ties are ranked, and both got easier once we said the tie rule out loud before typing.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-3.png)

## Five Conditions That Make Known Material Hard to Use

#### Condition #1: Pressure

A **timer** and an**evaluator** raise stress, and stress makes details harder to retrieve.

You know whether a date difference needs

```
DATEDIFF
```

or a plain subtraction. Under pressure, the answer arrives slowly. You type one, doubt it, delete it, and type the other.

Each hesitation costs seconds, and a 30-minute question has few to spare.

#### Condition #2: Recall Without a Reference

At your desk, you have documentation, autocomplete, and your old queries.

In an interview, everything comes from memory, and few people practice retrieving that way.

The small details go first: the argument order of a function, whether a frame clause takes

```
ROWS
```

or

```
RANGE
```

, which keyword comes after

```
PARTITION BY
```

. At a desk, you press Tab. In the interview, you write something close and hope it runs.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-4.png)

#### Condition #3: Communication

You explain the query to another person while you write it. Both tasks draw on the same attention, so one of them stalls, usually the code. The explanation keeps flowing while the cursor sits still, or the code gets written in silence while the interviewer waits. In both cases, the interviewer misses what they came to see, which is how you think.

#### Condition #4: Ambiguity

Prompts leave gaps. Do tied rows share a rank? What counts as a completed record?

Guessing at these in silence is a common reason for a wrong answer, and asking costs a few seconds. A wrong guess can make only a small difference in the data and still change the answer.

In our first question below, "more than 10 copies" and "at least 10 copies" differ by exactly one book.

#### Condition #5: Thinking Aloud

Silence looks like being stuck. Saying a half-formed plan, such as "I'll aggregate per book first, then rank", gives the interviewer something to follow and gives you a next step. It also lets them correct a wrong plan before you have written 15 lines of it.

## Rehearsing These Conditions with Mock Interviews

**Practicing** alone usually removes most of these conditions: no clock, no listener, nobody to explain to. You solve the problem**calmly**, check the answer, and move on.

That builds calm problem solving. The interview also asks you to recall, explain, and ask questions at the same time.

A **timer** alone covers pressure. The other four conditions need a listener and a prompt with gaps, and that is what a mock interview adds.

The **StrataScratch mock interview** puts most of them back: a countdown timer for pressure, an AI Interviewer panel for communication, and prompts with gaps to resolve.

A session is set by language, difficulty, duration, and question count. We used SQL, medium difficulty, 60 minutes, and 2 questions. Keep in mind that the questions in the mock interviews are randomly selected. Below, we present 2 questions that can appear in them.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-5.png)

The **session** opens with a countdown timer and a question panel with the tables. Beside it sits a**code editor with Test and Submit buttons**, with an** AI Interviewer panel** below the editor. Hints are free.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-14.png)

We treated it as a real interview: start the clock, read the prompt, state the clarifying questions and the plan out loud, then type. Below are both questions from our session, worked the way we would talk through them.

## Question 1: Top Books by Checkout Duration

This public library question is a medium analytical problem.

#### The Goal

For each book with more than 10 copies, sum the days between checkout date and return date across all completed checkouts. Rank books by that total, give tied books the same rank with no gaps, and keep ranks 1 to 3. The output is the book title, number of copies, and lifetime value in days.

#### The Data

```
library_books
```

has one row per title:

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-7.png)

```
library_checkouts
```

has one row per checkout:

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-8.png)

The full tables have 10 books and 106 checkouts; the last three checkouts have an empty

```
return_date
```

. Book 6, Where the Crawdads Sing, has exactly 10 copies, so the strict "more than 10" rule excludes it.

#### Resolving the Ambiguity Before Typing

The prompt answers most of the clarifying questions, and we still say them out loud. It takes seconds, and it puts every rule on the table before any SQL exists.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-9.png)

Here is what we said before typing: "Unreturned checkouts are out, so I only count rows with a return date. More than 10 is strict, so Where the Crawdads Sing drops out with exactly 10 copies. No gaps means DENSE\_RANK, so ties at rank 3 can return more than 3 rows. The plan is to sum days per book, rank the totals, and keep ranks 1 to 3."

#### The Solution

```
```
WITH lifetime AS (
    SELECT b.title,
           b.num_copies,
           SUM(c.return_date - c.checkout_date) AS lifetime_value
    FROM library_books b
    JOIN library_checkouts c ON c.book_id = b.book_id
    WHERE b.num_copies > 10
      AND c.return_date IS NOT NULL
    GROUP BY b.title, b.num_copies
),
ranked AS (
    SELECT title,
           num_copies,
           lifetime_value,
           DENSE_RANK() OVER (ORDER BY lifetime_value DESC) AS book_rank
    FROM lifetime
)
SELECT title, num_copies, lifetime_value
FROM ranked
WHERE book_rank <= 3
ORDER BY lifetime_value DESC, title;
```
```

The first common table expression (CTE) joins books to checkouts, keeps books with more than 10 copies and completed checkouts, and sums the day differences per book. Subtracting two dates in PostgreSQL gives a number of days.

```
SUM
```

would skip the

```
NULL
```

differences from open checkouts anyway. We keep the

```
IS NOT NULL
```

filter because it states the rule from the prompt.

The second CTE ranks the totals with

```
DENSE_RANK
```

. The final query keeps ranks 1 to 3.

```
RANK
```

would give 1, 1, 3, 3, 5, 5 on this data. The filter would then keep 4 rows and drop Educated and Lessons in Chemistry, which are rank 3 under

```
DENSE_RANK
```

and belong in the answer.

#### The Output

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-10.png)

Three ranks produce six rows because every rank holds a tie.

## Question 2: Top 5 Cities by 5-Star Businesses

This Yelp question is also a medium analytical problem.

#### The Goal

Find the cities ranked in the top 5 by number of 5-star businesses. Ties share a rank and the next rank is skipped, which is standard competition ranking. The output is the city and its count of 5-star businesses, open and closed combined.

#### The Data

```
yelp_business
```

has 13 columns. Here are 5 of them; the query uses only

```
city
```

and

```
stars
```

:

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-11.png)

#### Resolving the Ambiguity Before Typing

This time, the tie rule is the opposite of the first question, and that is the detail a rushed candidate misses. After a library question that asked for no gaps, it is easy to reach for

```
DENSE_RANK
```

without rereading the prompt.

What we said: "Open and closed both count, so I never filter on is\_open. The next rank is skipped after ties, so this is RANK. Top 5 means rank 5 or better, so LIMIT 5 is wrong whenever a tie runs past the fifth row. The plan is to count 5-star businesses per city, rank the counts, and keep ranks 1 to 5."

#### The Solution

```
```
WITH city_counts AS (
    SELECT city,
           COUNT(*) AS n_5star
    FROM yelp_business
    WHERE stars = 5
    GROUP BY city
),
ranked AS (
    SELECT city,
           n_5star,
           RANK() OVER (ORDER BY n_5star DESC) AS rnk
    FROM city_counts
)
SELECT city, n_5star
FROM ranked
WHERE rnk <= 5
ORDER BY n_5star DESC, city;
```
```

The first CTE counts 5-star businesses per city, the second ranks the counts with

```
RANK
```

, and the final query keeps ranks up to 5.

#### The Output

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-12.png)

Phoenix is rank 1. Las Vegas and Toronto tie at rank 2, so the next rank is 4. Five cities tie at 2 businesses and all hold rank 4, which is within the top 5. That is why the result has 8 rows.

```
LIMIT 5
```

would return Phoenix, Las Vegas, Toronto, and 2 arbitrary cities from the tied five.

## Conclusion: What to Practice Before the Next Interview

The **freeze** comes from the conditions around a question: clock, listener, missing reference, gaps, silence. Both questions above turned on the same detail, how ties are ranked. Saying it out loud before writing code is what catches it.

![Why Data Job Candidates](https://www.kdnuggets.com/wp-content/uploads/Rosidi-Why-Data-Job-Candidates-Freeze-13.png)

Before any ranking query, ask four things: how ties rank, whether the cutoff is strict or inclusive, which records are excluded, and how many rows the output should have.

Run a timed session, ask them first, and narrate the plan. The mock interview gives you the clock and the interviewer panel to do that.

A **30-minute question** can be split like this:

* 3 minutes to read and ask
* 2 minutes to state the plan
* 20 minutes to write and test
* 5 minutes to check the output against the prompt

Row counts are the quickest check. When the prompt says to include ties, look for them in your output.

After the session, review your own narration.

Did you state the tie rule before the first line of SQL? Did you ask about excluded records, or assume? Each answer points to one of the five conditions, and that tells you what to rehearse in the next session.

Nate Rosidi is a data scientist and in product strategy. He's also an adjunct professor teaching analytics, and is the founder of StrataScratch, a platform helping data scientists prepare for their interviews with real interview questions from top companies. Nate writes on the latest trends in the career market, gives interview advice, shares data science projects, and covers everything SQL.
