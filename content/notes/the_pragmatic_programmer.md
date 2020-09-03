+++
title = "The Pragmatic Programmer"
author = ["Alex Koen"]
lastmod = 2020-09-02T16:39:08-07:00
draft = false
+++

author
: David Thomas, Andrew Hunt

tags
: [§Programming]({{< relref "programming" >}})


## Notes {#notes}

-   Software rot—a project's slow but inevitable decline into disarray—is caused by a single entropy source.
    -   This is [§Broken Windows Theory]({{< relref "broken_windows_theory" >}})

    -   **Fix small bugs immediately.**

-   Continually invest in your knowledge portfolio:
    -   Aim to learn at least one language a year.

    -   Read technical books.

-   Never duplicate information -> Remember the acronym DRY (Don't Repeat Yourself). This applies to:
    -   **Code <–> Comments:** don't explain code that explains itself.

    -   **Code <–> Code:** always try to write modular components that can be re-used. Don't write a new function because it requires slightly different functionality than another function.

    -   **Code <–> Documentation:** when code is updated, documentation is often ignored. Consider how this could be mitigated. Could the code be generated from the documentation i.e. [§Literate Programming]({{< relref "literate_programming" >}})?

-   Similarly, modules should be orthogonal -> try to limit interdependencies between modules. Changing the functionality of one should not affect the others.
    -   For example, the GNU utils and Unix programs in general are small and simple but are orthogonal and can be easily chained together.

    -   Orthogonality applies equally to team structure. The responsibilities of individual team members should overlap minimally.

    -   This is the reasoning behind [§Aspect-Orientated Programming]({{< relref "aspect_orientated_programming" >}})

-   Avoid global data.

-   Use getters and setters whenever possible to protect private values.

-   All decisions and implementations should be reversible. Abstract database functionality so that the choice of vendor is interchangeable, or even allow for changes in language.
