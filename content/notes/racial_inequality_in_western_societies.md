+++
title = "Racial Inequality in Western Societies"
lastmod = 2021-06-16T12:17:35-07:00
draft = false
+++

## United States {#united-states}

-   1 in 4 black men will be incarcerated during their lifetime, whereas only 1 in 23 white men will.

-   As of 2016, the median worth of white households ($171,000) is ten times that of black households ($17,150) ([Source)](https://www.brookings.edu/blog/up-front/2020/02/27/examining-the-black-white-wealth-gap/)

{{< figure src="/ox-hugo/figure1-disparities-in-wre-new2021-05-04_15-58-57_.png" caption="Figure 1: Family net worth by ethnicity, in USD (2019). Source: <https://www.federalreserve.gov/econres/notes/feds-notes/disparities-in-wealth-by-race-and-ethnicity-in-the-2019-survey-of-consumer-finances-20200928.htm>" >}}


## White privilege {#white-privilege}

In recent years, the notion of _white privilege_ has gained popularity—the idea that white people benefit unconsciously from traditions and social structures that prevent others from attaining equality.

White privilege may be an example of a [luxury belief](https://nypost.com/2019/08/17/luxury-beliefs-are-the-latest-status-symbol-for-rich-americans/).

Barack Obama on the topic:

> Most working- and middle-class white Americans don't feel that they have been particularly privileged by their race. Their experience is the immigrant experience — as far as they're concerned, no one handed them anything. They built it from scratch. They've worked hard all their lives, many times only to see their jobs shipped overseas or their pensions dumped after a lifetime of labor. They are anxious about their futures, and they feel their dreams slipping away. And in an era of stagnant wages and global competition, opportunity comes to be seen as a zero sum game, in which your dreams come at my expense. **So when they are told to bus their children to a school across town; when they hear an African-American is getting an advantage in landing a good job or a spot in a good college because of an injustice that they themselves never committed; when they're told that their fears about crime in urban neighborhoods are somehow prejudiced, resentment builds over time.**
>
> Like the anger within the black community, these resentments aren't always expressed in polite company. But they have helped shape the political landscape for at least a generation. Anger over welfare and affirmative action helped forge the Reagan Coalition. Politicians routinely exploited fears of crime for their own electoral ends. **Talk show hosts and conservative commentators built entire careers unmasking bogus claims of racism while dismissing legitimate discussions of racial injustice and inequality as mere political correctness or reverse racism.**
>
> **Just as black anger often proved counterproductive, so have these white resentments distracted attention from the real culprits of the middle class squeeze — a corporate culture rife with inside dealing, questionable accounting practices and short-term greed; a Washington dominated by lobbyists and special interests; economic policies that favor the few over the many.** And yet, to wish away the resentments of white Americans, to label them as misguided or even racist, without recognizing they are grounded in legitimate concerns — this too widens the racial divide and blocks the path to understanding.
> — [Barack Obama]({{<relref "barack_obama.md" >}})


## Racial violence {#racial-violence}

<a id="table--hate-crimes"></a>
<div class="table-caption">
  <span class="table-number"><a href="#table--hate-crimes">Table 1</a></span>:
  Source: <a href="https://web.archive.org/web/20210506230727/https://ucr.fbi.gov/hate-crime/2019/tables/table-1.xls">https://web.archive.org/web/20210506230727/https://ucr.fbi.gov/hate-crime/2019/tables/table-1.xls</a>
</div>

| Race/Ethnicity                            | Incidents |
|-------------------------------------------|-----------|
| White                                     | 666       |
| Black or African American                 | 1930      |
| American Indian or Alaska Native          | 119       |
| Asian                                     | 158       |
| Native Hawaiian or Other Pacific Islander | 21        |
| Multiple Races, Group                     | 134       |
| Arab                                      | 95        |
| Hispanic or Latino                        | 527       |
| Other Race/Ethnicity/Ancestry             | 313       |

```jupyter-julia
using Plots
sort!(data, by=x->x[2],rev=true)
data = hcat(data...)
bar(data[1,:], data[2,:], size=(1000, 1000), xrotation=45, legend=false)
title!("U.S. Hate Crimes by Target Race/Ethnicity (2019)")
xlabel!("Target race/ethnicity")
ylabel!("Number of incidents")
```