+++
title = "Ancestry"
author = ["Alex Koen"]
lastmod = 2020-03-07T12:26:14-08:00
draft = false
+++

Ancestry is a company providing [§Geneology]({{< relref "20200223142655_geneology" >}}) and [§Direct-to-Consumer (DTC) Autosomal Genetic Testing]({{< relref "20200227194913_directtoconsumer_genetic_testing" >}}) services.

Ancestry offers two major genealogical services based on a saliva test: identity-by-descent analysis (see community detection) and genetic ancestry. <a id="6f93d01670cd1033affc62047021c9c6" href="#ethnicity">(Noto et al., )</a>

Autosome
: non-sex chromosomes.


## Sequencing Technology {#sequencing-technology}

-   Like [§23andMe]({{< relref "20200221134629_23andme" >}}), AncestryDNA uses SNP-chip technology, which probes for 730,525 genomic variants. <a id="6f93d01670cd1033affc62047021c9c6" href="#ethnicity">(Noto et al., )</a>
    -   Specifically, they use the Illumina OmniExpress Chip. <a id="08b172c96be4f4ef78adc0f4c19c4e60" href="#han2017clustering">(Han et al., 2017)</a>
-   The genomic variants chosen for the array were selected based on the Human HapMap Consortium, an international effort to catalogue global SNP variation. <a id="6f93d01670cd1033affc62047021c9c6" href="#ethnicity">(Noto et al., )</a>
    -   **The array only detects SNPs with an allele frequency > 5% <a id="6f93d01670cd1033affc62047021c9c6" href="#ethnicity">(Noto et al., )</a>**
    -   The majority of the SNPs are designed to target European populations.


## Genetic ancestry {#genetic-ancestry}

-   Until recently, AncestryDNA tests only provided an analysis of an individual's distant ancestry. <a id="8fee331a1d9bcba43f1e7b4277526ff5" href="#curtis2017estimation">(Curtis \& Girshick, 2017)</a>
    -   This is achieved by comparing SNPs across the individual's genome with those characteristic of various ethnic groups.
    -   Each ethinic group has characteristic SNPs as result of mating barriers between these ethnic groups.
-   Ancesty uses a program known as ADMIXTURE which estimates the proportion of an individual's membership in a set of ancestral populations based on his or her genotype. <a id="6f93d01670cd1033affc62047021c9c6" href="#ethnicity">(Noto et al., )</a>


## Community detection {#community-detection}

-   Now, Ancestry is working on a service to identify an individual's more recent ancestral groups using identity-by-descent inference. <a id="08b172c96be4f4ef78adc0f4c19c4e60" href="#han2017clustering">(Han et al., 2017)</a>

-   Ancestry's large dataset permits them to identify individuals who share haplotypes from a common ancestor. <a id="08b172c96be4f4ef78adc0f4c19c4e60" href="#han2017clustering">(Han et al., 2017)</a>
    -   The probability that a particular region in the genome is shared between two descendants of a common ancestor four generations ago is <1%.
    -   However, Ancestry has collected over 500 million such pairs.

-   Recent ancestry is analyzed using haplotype variation. <a id="8fee331a1d9bcba43f1e7b4277526ff5" href="#curtis2017estimation">(Curtis \& Girshick, 2017)</a>
    -   **Haplotype:** group of alleles inherited by a single ancestor.

    -   The familial relationship between two individuals can be determined using the length of shared DNA between them.
        -   e.g. a parent and a child will share half of the genome.

    -   This is achieved in two steps:
        1.  A genetic network of 742,394 consenting individuals was created. An unsupervised [§Machine Learning]({{< relref "20200302172229_machine_learning" >}}) **community detection** i.e. clustering algorithm was used to identify **haplotypes** characteristic of various genetic groups.
            -   The Louvain method was used.
            -   Community detection was performed **recursively** to discover sub-communities.

        2.  The communities discovered through clustering of the 742,394 individuals are used as **training data** for unsupervised classification algorithms. One algorithm is used for each community so that an individual may be assigned to multiple communities.


### Challenges of community detection <a id="8fee331a1d9bcba43f1e7b4277526ff5" href="#curtis2017estimation">(Curtis \& Girshick, 2017)</a> {#challenges-of-community-detection}

1.  Clustering is computationally intensive and is not feasible to perform regularly.
2.  Clustering algorithms typically assign nodes to only the single most suitable cluster.
    -   To solve this, Ancestry built a classification algorithm for each community.
3.  While clustering is consistent across an entire database, individual assignments may change across repetitions.


## Privacy {#privacy}

-   Ancesty offers identity-by-descent genotyping with the goal of allowing customer's to reunite with lost relatives.
-   However, this very promise has the potential for exploitation by law-enforcement agencies—nearly 60% of searches for individuals of European descent will result in a third-cousin or closer match. <a id="ff483d1ff591898a9942916050d2ca3f" href="#identity">(Erlich et al., 2018)</a>
-   Notably, in a recent case, law enforcement used a genetic search to trace the Golden State Killer—authorities were able to locate the killer's third cousin.
    -   Although this particular case is positive, the same technique could be used for nefarious purposes, such as re-identifying subjects of research studies from their genetic data.
    -   **Currently, the U.S department of Health and Human Services does not consider genome-wide datasets as identifiable information.**

-   DTC genetic testing companies provide customers with their raw DNA files which can then be uploaded to other services.

# Bibliography
<a id="ethnicity" target="_blank">Noto, K., Wang, Y., Song, S., Turissini, D., Sedghifar, A., Garrigan, D., Starr, B., …, *Ethnicity estimate 2018 white paper*, , *()*,  (). </a> [↩](#6f93d01670cd1033affc62047021c9c6)

<a id="han2017clustering" target="_blank">Han, E., Carbonetto, P., Curtis, R. E., Wang, Y., Granka, J. M., Byrnes, J., Noto, K., …, *Clustering of 770,000 genomes reveals post-colonial population structure of north america*, Nature communications, *8()*, 14238 (2017). </a> [↩](#08b172c96be4f4ef78adc0f4c19c4e60)

<a id="curtis2017estimation" target="_blank">Curtis, R. E., & Girshick, A. R., *Estimation of recent ancestral origins of individuals on a large scale*, In , Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1417–1425) (2017). : .</a> [↩](#8fee331a1d9bcba43f1e7b4277526ff5)

<a id="identity" target="_blank">Erlich, Y., Shor, T., Peer, I., & Carmi, S., *Identity inference of genomic data using long-range familial searches*, Science, *362(6415)*, 690–694 (2018).  http://dx.doi.org/10.1126/science.aau4832</a> [↩](#ff483d1ff591898a9942916050d2ca3f)
