---
title: DIY archivists push budget Nikons to 902,000 clicks to save 1,800 rare books
  — team trains neural net on Photoshop edits to process 526,000 scans
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/diy-archivists-push-budget-nikons-to-902-000-clicks-to-save-1-800-rare-books-team-trains-neural-net-on-photoshop-edits-to-process-526-000-scans
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-30T13:46:32Z'
published: '2026-08-30T00:00:00Z'
description: There's a chance that
image: https://cdn.mos.cms.futurecdn.net/VPbW5b8NY95wsWtsy8qjbH-1632-80.png
---

![Urdu script book](https://cdn.mos.cms.futurecdn.net/VPbW5b8NY95wsWtsy8qjbH.png) 

Around 2015, a trio of Pakistani friends took it upon themselves to digitize a large number of out-of-print books in Urdu, many of them lithographs — they call it the Ibteda Digital Library. They did it for the love of the language, with no budget or support, but after 576,000 shutter counts on a D5300 camera, 326,000 on a D3300, and 526,000 dual-page photos, they have now had to call it quits after a decade. However, eventually one of the trio came up with a finely-tuned machine-learning process that may eventually be of help to similar projects worldwide. The project certainly stands in contrast to the current practice of large AI companies scanning rare books and destroying them to train AI chatbots.

The team didn't have any formal budget worth and bought all of the books out of their own pockets. They kicked off the efforts with a single Nikon D5300 camera, some LED bulbs, and a glass sheet taken from a photocopier to squeeze the books against. The process was manual in more ways than one: besides turning the pages by hand, the members spent copious amounts of time in Photoshop post-processing the results.

Getting an archival-quality digital copy of a page isn't as simple as taking a photograph with the best camera you can find. It requires maintaining consistent margins, text size, orientation, and using the same perspective correction across an entire book, among many other fine details. Rarely can the same procedure be used across more than a few publications — even given two otherwise identical books, book A may be much thicker than book B, meaning the spacing between the pages, and possibly the perspective, will be different.

Adding to the challenge, the bulk of the works were in Urdu script, likely Nastaliq. Urdu is the national language of Pakistan and also spoken across part of India, and in many worldwide communities. Its written form was originally an elegant flowing script, but people switched to using Roman characters with the advent of phones and the internet.

The script format means that layouts are almost always unique, and the corpus includes everything from printed books to centuries-old lithographs to handwritten notes. Plus, Urdu script uses a lot of dots, diacritics, and small symbols, meaning photography noise, dirt, and blemishes had to be visually distinguishable from actual writing. In other words, each book was its own corner case, and old lithographs in particular had copious amounts of margin notes.

All told, this meant that while photographing the books was tedious but reasonably fast, the post-processing was definitely not. After 576,000 shutter counts on the D5300 and 326,000 on the D3300 camera, there were over 526,000 dual-page photos left to handle after the team had to give up on the project in April 2026. Manually processing those was out of the question, so one of the researchers turned their eye to automation using OpenCV.

The first few attempts with standard computer-vision methods didn't work out, as a rule set that worked for a set of books completely failed for the next one. The author then understood they could use their own manually processed images to establish a source/target correspondence: in their own words, "finished pages became labels," giving birth to the idea of calculating the homography fit from the Photoshop files and using it for training a neural network.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The first challenge was matching the crop borders, easier said than done because "dense Urdu print repeats strokes, words, borders, and column patterns," meaning that marks from neighboring pages could throw off the measurements. Next up, visible area identification and gutter separation were made tricky by tables and deep gutter shadows. Cropping errors required a specific pass, as did blemish removal.

Interestingly enough, the researcher noticed that using a bigger model or more training samples actually *reduced* the accuracy of the results. The choice of crop margin (inset) for each book was unique, made to the editor's judgement. But since it had no discernible pattern, adding more books made the model's pattern recognition worse, not better.

The final process still needs ten calibration crops for a new book, but that's a pretty reasonable amount of manual labor to be able to process a book entirely. Finally, the books are hosted in a ZFS pool with BLAKE3 manifests.

The entire tale and all the technical details are explained in a lengthy blog post, and you can peruse the beautiful Urdu writings at the Ibteda Digital Library page at the Internet Archive. My Western eyes can't read any of it, but the poem translations are beautiful.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
