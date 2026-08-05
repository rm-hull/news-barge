---
title: Are your Android apps secretly sharing your location with advertisers? Some
  developers are accidentally leaving on this critical data-invading setting when
  using third-party SDKs
source_url: https://www.techradar.com/pro/security/are-your-android-apps-secretly-sharing-your-location-with-advertisers-some-developers-are-accidentally-leaving-on-this-critical-data-invading-setting-when-using-third-party-sdks
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-05T21:23:45Z'
published: '2026-08-05T00:00:00Z'
description: Some apps are gathering highly-localized location data and feeding it
  back to advertisers, data brokers, and even the military.
image: https://cdn.mos.cms.futurecdn.net/hHfi9yH36kgGzLHyDnHTcX-2000-80.jpg
---

![Map shown on smartphone](https://cdn.mos.cms.futurecdn.net/hHfi9yH36kgGzLHyDnHTcX.jpg) 

- **Some Android apps contain invasive data-gathering SDKs that gather location data without user consent**
- **Location data is then sold to advertisers, or purchased by law enforcement for targeting and tracking US citizens**
- **Developers, regulators, and legislators should work together to remove the incentive for SDKs to gather this data**

Monetizing an app is a key part of development. But developers frequently use third-party software development kits (SDKs) rather than develop their own monetization tools.

These SDKs often come preloaded with data-collection mechanisms that allow developers to choose what types of user data it would like to collect to sell to advertisers. Sometimes, developers leave every setting on.

According to a warning from the Electric Frontier Foundation, SDKs with their default data collection settings left on are harvesting highly invasive location data, which is then passed on to advertisers and data brokers. Critically, this data can then be purchased and used by intelligence agencies, law enforcement, and even the military.

## Authorities using advertising location data for questionable operations

Location data is very lucrative for advertisers. It helps increase the bid-price for advertising space, allowing local businesses or services to target those nearby with adverts.

The level of invasive data collected depends on the permissions the app asks for. But crucially, any permissions granted to the app itself are also passed on to the SDK by default.

Where approximate location data determined by the device IP is accurate to about 1.2 square miles, precise location data can narrow that area down to about 160 feet, or in some circumstances as small as 10 feet.

In some cases, the SDKs include documentation for developers to ensure restricted data processing is turned on for users that are subject to GDPR and COPPA, but these settings are not turned on by default.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Also, some SDKs can gather and share location data without the user’s meaningful consent. Two apps analyzed by EFF that harvested location data through SDKs were downloaded more than 50 million and 10 million times, respectively. Neither app showed a notice or requested consent from the user, and both failed to declare that the apps would share location data with third parties in the Google Play Store Data Safety section.

Some apps require location data as part of their core functionality. For example, your chosen weather app, or a running app, may need your location data. But for many Android apps, the consent provided for this location tracking is also deemed to be consent for SDKs.

“App-level location permissions alone cannot signal meaningful consent to location collection and sharing by third-party advertising SDKs,” the EFF report says.

In many cases, location data sold by advertisers and data brokers has been used by intelligence agencies and law enforcement in highly-targeted operations.

The EFF includes a number of recommendations for developers, regulators, and legislators:

- Developers should have a responsibility to protect the privacy of their users. They should check third-party SDKs and ensure that user data is not shared by default
- Regulators should pursue app developers that fail to ensure user data is not unlawfully passed on to third parties. Additionally, regulators should pursue companies that deliberately develop SDKs that gather invasive amounts of user data by default
- Legislators in the US should work to develop a federal law similar to GDPR to protect users from privacy violations. Banning behavioral advertising would also remove the incentive from companies developing SDKs to gather as much data as possible

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
