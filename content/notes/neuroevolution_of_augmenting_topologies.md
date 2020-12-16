+++
title = "NeuroEvolution of Augmenting Topologies"
author = ["Alex Koen"]
lastmod = 2020-12-15T11:32:26-08:00
draft = false
+++

## Definitions {#definitions}

Hidden node
: a node that is neither an input nor an output node.

Bias unit
: An input that is always set to 1. Can connect to any node _other_ than an input.


## Evolution {#evolution}

Composed of:

1.  Selection
2.  Crossover
3.  Mutation


## Augmenting {#augmenting}

We start with the smallest possible set of nodes containing inputs and outputs. This is called _minimal initialization_, and is a distinct advantage of NEAT.

The exact structure of your initial population is not set in stone, For simple networks, this could mean having a connection between each input node and output node.

{{< figure src="/ox-hugo/screenshot2020-11-15_17-28-20_.png" >}}

The _bias_ can be thought of as a y-intercept to our network: it allows us to shift our output up or down.


## Mutations {#mutations}


### Mutate Add Connection {#mutate-add-connection}

{{< figure src="/ox-hugo/screenshot2020-11-15_17-34-54_.png" >}}


## Speciation {#speciation}

The compatibility distance &sigma; between two genomes is given by:

\begin{equation}
\label{eq:1}
\sigma=\frac{c\_{1}E}{N}+\frac{c\_{2}D}{N}+c\_{3}\cdot \bar{W}
\end{equation}

where:
\\(N\\) is the number of genes in the larger genome.
\\(E\\) is the number of excess genes.
\\(D\\) is the number of disjoint genes.
\\(\bar{W}\\) is the _average_ difference in weight between all matching connections, including disabled ones.
\\(c\_1, c\_2, c\_3\\) are hard-coded importance coefficients.

TODO It is unclear what "Number of genes" means, so I am doing number of nodes + number of connections.


## Adjusted Fitness {#adjusted-fitness}

The paper defines the adjusted fitness of a particular genome as:

\begin{equation}
\label{eq:2}
f'=\frac{f\_i}{\sum\_{j=1}^n sh(\sigma(i,j))}
\end{equation}

Where \\(sh\\) evaluates to 1 if the two genomes are similar enough to be classified as the same specifies. Thus, this equation simplifies to:

\begin{equation}
\label{eq:3}
f'=\frac{f\_i}{N},
\end{equation}

where \\(N\\) is the number of genomes in the species.


## Breeding {#breeding}

For each species in every generation, only the single highest-performing genome survives. The rest of the new population is randomly bred from the other highest performing genomes, but almost all of those parents still die.

The number of offspring allocated to each species \\(k\\) is proportional to its relative performance in the generation.:

\begin{equation}
\label{eq:4}
n\_k\_{}\_{}=\frac{\bar{F}\_k\_{}}{\bar{F}\_{tot}}\cdot|P|
\end{equation}

where:
\\(\bar{F}\_k\\) is the average adjusted fitness of species \\(k\\).
\\(\bar{F}\_{tot}\\) is the sum of the average adjusted fitnesses for each species.
\\(|P|\\) is the constant population size.


## Activation {#activation}

The output of any given node is given by:

\begin{align}
\label{eq:5}
y\_j=\sigma \left(\sum\_i w\_{ij}x\_i  \right)
\end{align}

Where \\(w\_{ij}\\) is the connection weight from node \\(i\\) to node \\(j\\), \\(x\_i\\) is the output of node \\(i\\), and \\(\sigma\\) is the activation function, which is typically the sigmoid function \\(\frac{1}{1+e^{-x}}\\).

However, <https://neat-python.readthedocs.io/en/latest/glossary.html> and other implementations use a different formula, given by:

_output = activation(bias+(response∗aggregation(inputs)))_

where _response_ is a constant that may be subject to evolution.
