+++
title = "Ancestry"
lastmod = 2021-06-16T12:17:38-07:00
draft = false
+++

Ancestry is a company providing [Geneology]({{<relref "geneology.md" >}}) and [Direct-to-Consumer (DTC) Autosomal Genetic Testing]({{<relref "directtoconsumer_genetic_testing.md" >}}) services.

Ancestry offers two major genealogical services based on a saliva test: identity-by-descent analysis (see community detection) and genetic ancestry. <sup id="6f93d01670cd1033affc62047021c9c6"><a href="#ethnicity" title="Noto, Wang, Song, Turissini, Sedghifar, Garrigan, Starr, Byrnes, Hong, Ball \&amp; others, Ethnicity Estimate 2018 White Paper, v(), ().">ethnicity</a></sup>

Autosome
: non-sex chromosomes.


## Sequencing Technology {#sequencing-technology}

-   Like [23andMe]({{<relref "23andme.md" >}}), AncestryDNA uses SNP-chip technology, which probes for 730,525 genomic variants. <sup id="6f93d01670cd1033affc62047021c9c6"><a href="#ethnicity" title="Noto, Wang, Song, Turissini, Sedghifar, Garrigan, Starr, Byrnes, Hong, Ball \&amp; others, Ethnicity Estimate 2018 White Paper, v(), ().">ethnicity</a></sup>
    -   Specifically, they use the Illumina OmniExpress Chip. <sup id="08b172c96be4f4ef78adc0f4c19c4e60"><a href="#han2017clustering" title="Han, Carbonetto, Curtis, Wang, Granka, Byrnes, Noto, Kermany, Myres, Barber \&amp; others, Clustering of 770,000 genomes reveals post-colonial population structure of North America, {Nature communications}, v(), 14238 (2017).">han2017clustering</a></sup>
-   The genomic variants chosen for the array were selected based on the Human HapMap Consortium, an international effort to catalogue global SNP variation. <sup id="6f93d01670cd1033affc62047021c9c6"><a href="#ethnicity" title="Noto, Wang, Song, Turissini, Sedghifar, Garrigan, Starr, Byrnes, Hong, Ball \&amp; others, Ethnicity Estimate 2018 White Paper, v(), ().">ethnicity</a></sup>
    -   **The array only detects SNPs with an allele frequency > 5% <sup id="6f93d01670cd1033affc62047021c9c6"><a href="#ethnicity" title="Noto, Wang, Song, Turissini, Sedghifar, Garrigan, Starr, Byrnes, Hong, Ball \&amp; others, Ethnicity Estimate 2018 White Paper, v(), ().">ethnicity</a></sup>**
    -   The majority of the SNPs are designed to target European populations.


## Genetic ancestry {#genetic-ancestry}

-   Until recently, AncestryDNA tests only provided an analysis of an individual's distant ancestry. <sup id="8fee331a1d9bcba43f1e7b4277526ff5"><a href="#curtis2017estimation" title="Curtis \&amp; Girshick, Estimation of Recent Ancestral Origins of Individuals on a Large Scale, 1417--1425, in in: {Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining}, edited by (2017)">curtis2017estimation</a></sup>
    -   This is achieved by comparing SNPs across the individual's genome with those characteristic of various ethnic groups.
    -   Each ethinic group has characteristic SNPs as result of mating barriers between these ethnic groups.
-   Ancesty uses a program known as ADMIXTURE which estimates the proportion of an individual's membership in a set of ancestral populations based on his or her genotype. <sup id="6f93d01670cd1033affc62047021c9c6"><a href="#ethnicity" title="Noto, Wang, Song, Turissini, Sedghifar, Garrigan, Starr, Byrnes, Hong, Ball \&amp; others, Ethnicity Estimate 2018 White Paper, v(), ().">ethnicity</a></sup>


## Community detection {#community-detection}

-   Now, Ancestry is working on a service to identify an individual's more recent ancestral groups using identity-by-descent inference. <sup id="08b172c96be4f4ef78adc0f4c19c4e60"><a href="#han2017clustering" title="Han, Carbonetto, Curtis, Wang, Granka, Byrnes, Noto, Kermany, Myres, Barber \&amp; others, Clustering of 770,000 genomes reveals post-colonial population structure of North America, {Nature communications}, v(), 14238 (2017).">han2017clustering</a></sup>

-   Ancestry's large dataset permits them to identify individuals who share haplotypes from a common ancestor. <sup id="08b172c96be4f4ef78adc0f4c19c4e60"><a href="#han2017clustering" title="Han, Carbonetto, Curtis, Wang, Granka, Byrnes, Noto, Kermany, Myres, Barber \&amp; others, Clustering of 770,000 genomes reveals post-colonial population structure of North America, {Nature communications}, v(), 14238 (2017).">han2017clustering</a></sup>
    -   The probability that a particular region in the genome is shared between two descendants of a common ancestor four generations ago is <1%.
    -   However, Ancestry has collected over 500 million such pairs.

-   Recent ancestry is analyzed using haplotype variation. <sup id="8fee331a1d9bcba43f1e7b4277526ff5"><a href="#curtis2017estimation" title="Curtis \&amp; Girshick, Estimation of Recent Ancestral Origins of Individuals on a Large Scale, 1417--1425, in in: {Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining}, edited by (2017)">curtis2017estimation</a></sup>
    -   **Haplotype:** group of alleles inherited by a single ancestor.

    -   The familial relationship between two individuals can be determined using the length of shared DNA between them.
        -   e.g. a parent and a child will share half of the genome.

    -   This is achieved in two steps:
        1.  A genetic network of 742,394 consenting individuals was created. An unsupervised [Machine Learning]({{<relref "machine_learning.md" >}}) **community detection** i.e. clustering algorithm was used to identify **haplotypes** characteristic of various genetic groups.
            -   The Louvain method was used.
            -   Community detection was performed **recursively** to discover sub-communities.

        2.  The communities discovered through clustering of the 742,394 individuals are used as **training data** for unsupervised classification algorithms. One algorithm is used for each community so that an individual may be assigned to multiple communities.


### Challenges of community detection <sup id="8fee331a1d9bcba43f1e7b4277526ff5"><a href="#curtis2017estimation" title="Curtis \&amp; Girshick, Estimation of Recent Ancestral Origins of Individuals on a Large Scale, 1417--1425, in in: {Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining}, edited by (2017)">curtis2017estimation</a></sup> {#challenges-of-community-detection}

1.  Clustering is computationally intensive and is not feasible to perform regularly.
2.  Clustering algorithms typically assign nodes to only the single most suitable cluster.
    -   To solve this, Ancestry built a classification algorithm for each community.
3.  While clustering is consistent across an entire database, individual assignments may change across repetitions.


## Privacy {#privacy}

-   Ancesty offers identity-by-descent genotyping with the goal of allowing customer's to reunite with lost relatives.
-   However, this very promise has the potential for exploitation by law-enforcement agencies—nearly 60% of searches for individuals of European descent will result in a third-cousin or closer match. <sup id="ff483d1ff591898a9942916050d2ca3f"><a href="#identity" title="Erlich, Shor, Peer \&amp; Carmi, Identity inference of genomic data using long-range familial searches, {Science}, v(6415), 690--694 (2018).">identity</a></sup>
-   Notably, in a recent case, law enforcement used a genetic search to trace the Golden State Killer—authorities were able to locate the killer's third cousin.
    -   Although this particular case is positive, the same technique could be used for nefarious purposes, such as re-identifying subjects of research studies from their genetic data.
    -   **Currently, the U.S department of Health and Human Services does not consider genome-wide datasets as identifiable information.**

-   DTC genetic testing companies provide customers with their raw DNA files which can then be uploaded to other services.

# Bibliography
<a id="ethnicity"></a>[ethnicity] Noto, Wang, Song, Turissini, Sedghifar, Garrigan, Starr, Byrnes, Hong, Ball & others, Ethnicity Estimate 2018 White Paper, <i></i>,  . [↩](#6f93d01670cd1033affc62047021c9c6)

<a id="han2017clustering"></a>[han2017clustering] Han, Carbonetto, Curtis, Wang, Granka, Byrnes, Noto, Kermany, Myres, Barber & others, Clustering of 770,000 genomes reveals post-colonial population structure of North America, <i>Nature communications</i>, <b>8</b>, 14238 (2017). [↩](#08b172c96be4f4ef78adc0f4c19c4e60)

<a id="curtis2017estimation"></a>[curtis2017estimation] Curtis & Girshick, Estimation of Recent Ancestral Origins of Individuals on a Large Scale, 1417-1425, in in: Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, edited by (2017) [↩](#8fee331a1d9bcba43f1e7b4277526ff5)

<a id="identity"></a>[identity] Erlich, Shor, Peer & Carmi, Identity inference of genomic data using long-range familial searches, <i>Science</i>, <b>362(6415)</b>, 690-694 (2018). <a href="https://science.sciencemag.org/content/362/6415/690">link</a>. <a href="http://dx.doi.org/10.1126/science.aau4832">doi</a>. [↩](#ff483d1ff591898a9942916050d2ca3f)