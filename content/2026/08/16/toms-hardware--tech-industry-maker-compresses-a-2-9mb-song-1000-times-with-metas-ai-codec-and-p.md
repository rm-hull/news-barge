---
title: Maker compresses a 2.9MB song by 1000x and prints it on paper as eight QR codes
  — 21KB song is two minutes long, requires a neural network for playback
source_url: https://www.tomshardware.com/tech-industry/maker-compresses-a-2-9mb-song-1000-times-with-metas-ai-codec-and-prints-it-on-paper-as-eight-qr-codes
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-16T16:38:20Z'
published: '2026-08-16T00:00:00Z'
description: Meta's AI codec was used for the compression.
image: https://cdn.mos.cms.futurecdn.net/4JwLzCyNBmPwoKZfyLrjd-1972-80.png
---

![Maker compresses a 2.9MB song 1,000 times with Meta's AI codec and prints it on paper as eight QR codes](https://cdn.mos.cms.futurecdn.net/4JwLzCyNBmPwoKZfyLrjd.png) 

A maker known as Makestreme has printed an entire two-minute song onto a sheet of paper, publishing the full build and source code on Hackster.io. The trick is Meta's EnCodec neural audio codec, which crunched a 2.9MB MP3 down to roughly 21KB of latent tokens, a reduction of about 1,000 times, small enough to split across eight QR codes arranged as a double-sided "paper cassette." The same 21KB file was also beamed between two ESP32 boards over LoRa radio, and by our reading of the published transmitter code, that wireless transfer takes around 90 minutes per song.

One QR code tops out at roughly 3KB of binary data, with Makestreme hitting the practical limit at about 3.3KB, so a 2.9MB MP3 would need close to a thousand of them. Conventional compression can't close that gap because MP3 is itself already lossy, which is where EnCodec comes in.

![Can you fit an entire song into a QR code? - YouTube](https://img.youtube.com/vi/w5hIdQcUnRE/maxresdefault.jpg) 

The open-source codec Meta released in 2022 converts a waveform into discrete tokens that a matching decoder turns back into audio, and at the project's 3 kbps setting, the reconstructed song reportedly held up well. At 1.5 kbps, however, it produced heavily degraded output.

Each of the eight QR codes carries a 1-byte ID plus a chunk of the token stream, four codes per side in a nod to flipping a vinyl record. The generator script uses the lowest error correction level to maximize density, so there's no redundancy to spare: damage one code and the song is gone.

LoRa pairs two ESP32s with REYAX RYLR998 modules on 866 MHz, moving the file in 160-byte packets with an ACK-and-retry protocol. The transmitter sketch hard-codes a 40-second pause after every acknowledged packet, and at roughly 134 packets for a 21KB file, the gaps alone add up to about 90 minutes. That pacing is deliberately conservative for duty-cycle compliance, and it's a far cry from the 190 KB/s another developer hit recently by streaming QR codes between phones at 60 FPS.

Printing software on paper dates back to the Cauzin Softstrip of 1985, a 2D barcode that let magazines publish programs at up to 5,500 bytes per strip and faded once floppy disks got cheap. It left behind strips almost nobody can read today, and Paper Tunes inherits the same dependency: the QR codes store tokens, not audio, so playback requires EnCodec's exact 24 kHz decoder.

The paper may last centuries, as Cerabyte argues with its microscopic QR codes etched in ceramic, but the song only survives as long as the neural network that can decode it.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
