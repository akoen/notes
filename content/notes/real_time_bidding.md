+++
title = "Real-time bidding"
lastmod = 2021-06-16T12:20:17-07:00
draft = false
+++

tags
: [Digital Privacy]({{<relref "digital_privacy.md" >}})

Every time you visit a ad-enabled website, your personal information is sent to potentially hundreds of advertisers in a process known as [real-time-bidding](https://en.wikipedia.org/wiki/Real-time%5Fbidding#How%5Fit%5Fworks).

{{< figure src="/ox-hugo/pasted_image_02021-05-30_20-30-11_.png" >}}

The industry is controlled almost entirely by Google.

-   Data is shared between advertisers.
-   companies place intentionally losing bids on a website to collect personal information for free.


## Information potentially included {#information-potentially-included}

-   Location
-   Time spent viewing certain content
    <https://web.archive.org/web/20210531021350/https://developers.google.com/adwords/api/docs/appendix/verticals>
    -   Inferred demographic information, including:
        -   Health/Reproductive Health/Infertility
        -   Health/Substance Abuse
        -   Health/Health Conditions/Cancer
        -   /People & Society/Ethnic & Identity Groups/Lesbian, Gay, Bisexual & Transgender

The information provided to each bidder by Google is specified by the Authorized Buyers real-time bidding protocol, specified at <https://web.archive.org/web/20210531025015/https://developers.google.com/authorized-buyers/rtb/realtime-bidding-guidehttps://dehttized-buyers/rtb/realtime-bidding-guide>.

-   Highlights include:

    -   Latitude and longitude
    -   Page Verticals
    -   Identifer for Advertising (IDFA, Apple) or Google Advertising ID (AAID)
    -   `cookie_match_data`. To enable "cookie syncing'
    -   Whether the user is included on a specific list provided by the advertiser

    OpenRTB, specified at <https://web.archive.org/web/20210531031340/https://www.iab.com/wp-content/uploads/2016/03/OpenRTB-API-Specification-Version-2-5-FINAL.pdf>

    -   **ip:** full ip address of the current device
    -   **Object: Data Object: Segment:** key-value pairs of user interests/demographics
    -   **gender:**

    -   ::


## Google Customer Match {#google-customer-match}

> To make this more concrete: suppose a company wants to acquire data about expecting mothers. It can buy a list of a million device IDs that a data broker believes to belong to such women. The company can upload this list to Google and target an ad at those IDs. If even a small fraction—say, 1%—click on the ad, then 10,000 people are sent to the advertiser’s landing page, where they automatically share their IP address, cookies, and possibly geolocation data. The company now has sensitive medical data about 10,000 people served up to it on a silver platter. (Google prohibits targeting based on medical and other characteristics in its Customer Match terms of service, but it is unclear how the company audits or enforces them.)
> —<https://www.eff.org/deeplinks/2020/03/google-says-it-doesnt-sell-your-data-heres-how-company-shares-monetizes-and>