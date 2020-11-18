+++
title = "Optical Coherence Tomography"
author = ["Alex Koen"]
lastmod = 2020-11-11T10:26:09-08:00
draft = false
+++

## Overview {#overview}

-   Optical coherence tomography consists of measuring the optical reflections of biological structures using low-coherence light. <sup id="4313277ed1d56c552d84008ff59b3d64"><a href="#optical" title="Huang, Swanson, Lin, Schuman, Stinson, Chang, Hee, Flotte, Gregory, Puliafito \&amp; others, Optical coherence tomography, {science}, v(5035), 1178--1181 (1991).">optical</a></sup>
    -   Ultrashort pulsed lasers and supercontinuum lasers are used, but less frequently than superluminescent diodes.

-   waves are described as **coherent** if they have the same waveform and are perfectly in phase.
    -   In this context, incoherent means that broadband light is used, modelled as a Gaussian source.

-   Optical image tomography is analogous to optical ultrasound. Multiple longitudinal scans are performed laterally to produce a two-dimension map of reflection sites in the scanned area. <sup id="4313277ed1d56c552d84008ff59b3d64"><a href="#optical" title="Huang, Swanson, Lin, Schuman, Stinson, Chang, Hee, Flotte, Gregory, Puliafito \&amp; others, Optical coherence tomography, {science}, v(5035), 1178--1181 (1991).">optical</a></sup>

-   Typically uses near-infrared light.

-   A light source produces a beam of incoherent light that is split by a Michelson interferometer. The interference pattern produced by the interference between the light returning from the sample and the light returning from a reference mirror is then analyzed <sup id="4313277ed1d56c552d84008ff59b3d64"><a href="#optical" title="Huang, Swanson, Lin, Schuman, Stinson, Chang, Hee, Flotte, Gregory, Puliafito \&amp; others, Optical coherence tomography, {science}, v(5035), 1178--1181 (1991).">optical</a></sup>.

-   To produce a B-scan image, the sample is scanned laterally forming a cross-section of A-scan images.

-   Each measurement produces an A-scan image, analogous to that of an ultrasound machine. To produce a 2D or 3D image, the image must be scanned in one or two lateral dimensions respectively.


### Time domain OCT (TD-OCT) {#time-domain-oct--td-oct}

{{< figure src="/ox-hugo/screenshot2020-04-12_19-30-54_.png" >}}

![](/ox-hugo/screenshot2020-04-13_08-34-21_.png)
<sup id="6f749bf4e5bb6903f28c6f030daa5a1a"><a href="#aumann" title="@incollection{aumann,
  title={Optical Coherence Tomography (OCT): Principle and Technical Realization},
  author={Aumann, Silke and Donner, Sabine and Fischer, J{\o}rg and M{\u}ller, Frank},
  booktitle={High Resolution Imaging in Microscopy and Ophthalmology},
  pages={59--85},
  year={2019},
  publisher={Springer}
}">aumann</a></sup>.

-   Goal is to identify the _position_ of the scattering object.

-   In time-domain OCT, the position of a movable mirror is adjusted, resulting in a burst pattern when the mirror and the object are equidistant from the detector.
    -   A broadband source is used because maximal constructive interference is _only_ produced when the two are equidistant.
    -   If monochromatic or 2-wavelength sources are used, the interference signal is periodic as a function of τ **and the location of the scattering object cannot be determined.**


### Fourier domain OCT (FD-OCT) {#fourier-domain-oct--fd-oct}

{{< figure src="/ox-hugo/screenshot2020-04-13_07-22-11_.png" >}}

![](/ox-hugo/screenshot2020-04-13_08-42-26_.png)
<sup id="6f749bf4e5bb6903f28c6f030daa5a1a"><a href="#aumann" title="@incollection{aumann,
  title={Optical Coherence Tomography (OCT): Principle and Technical Realization},
  author={Aumann, Silke and Donner, Sabine and Fischer, J{\o}rg and M{\u}ller, Frank},
  booktitle={High Resolution Imaging in Microscopy and Ophthalmology},
  pages={59--85},
  year={2019},
  publisher={Springer}
}">aumann</a></sup>

-   The rate at which the measured reflectance changes as a function of depth varies with wavelength.
    -   Red light (greater wavelength) modulates more slowly than blue light (shorter wavelength).

-   When reflectance is then plotted as a function of wavenumber ṽ, the values of reflectance for different colours of light form sine waves.
    -   The period of these sine waves encodes the depth of the scattering object.

-   In spectral domain OCT, the position of the reference mirror is not changed.

-   Instead, a spectrometer at the detector measures the amplitude of the interference pattern as a function of the wavenumber ṽ.

-   A Fourier transform is then performed on the measured reflectance vs. wavenumber plot to determine the reflectance vs. depth.

-   Source:
    <sup id="ab389edaabf8d841f5719d0cf64006a3"><a href="#twenty" title="De Boer, Leitgeb \&amp; Wojtkowski, Twenty-five years of optical coherence tomography: the paradigm shift in sensitivity and speed provided by Fourier domain OCT, {Biomedical optics express}, v(7), 3248--3280 (2017).">twenty</a></sup>
    1.  A Gaussian source as for time-domain OCT with a spectrometer. This is Spectral Domain OCT.
    2.  A swept-source with a simple detector. A rapidly tunable laser emits a single intense wavelength at a time. This is Swept Source OCT.

-   FD-OCT is almost always favoured over TD-OCT because of improved sensitivity as a result of reduced noise. <sup id="ab389edaabf8d841f5719d0cf64006a3"><a href="#twenty" title="De Boer, Leitgeb \&amp; Wojtkowski, Twenty-five years of optical coherence tomography: the paradigm shift in sensitivity and speed provided by Fourier domain OCT, {Biomedical optics express}, v(7), 3248--3280 (2017).">twenty</a></sup>


### Advantages {#advantages}

{{< figure src="/ox-hugo/screenshot2020-04-13_08-22-19_.png" >}}

<sup id="6f749bf4e5bb6903f28c6f030daa5a1a"><a href="#aumann" title="@incollection{aumann,
  title={Optical Coherence Tomography (OCT): Principle and Technical Realization},
  author={Aumann, Silke and Donner, Sabine and Fischer, J{\o}rg and M{\u}ller, Frank},
  booktitle={High Resolution Imaging in Microscopy and Ophthalmology},
  pages={59--85},
  year={2019},
  publisher={Springer}
}">aumann</a></sup>

-   Both the axial and lateral resolution of OCT are significantly greater than ultrasound, CT, MRI, and other commonly used imaging technologies.
    -   These resolution are typically 5–20 µm


### Applications {#applications}

-   In 2014, 5.13 million OCT scans were performed in the US alone, making it one of the most common medical imaging procedures <sup id="a3770611f451f8dd05948bd4fef01fc9"><a href="#Fauw" title="De Fauw, Ledsam, Romera-Paredes, Nikolov, Tomasev, Blackwell, Askham, Glorot, O&#8217;Donoghue, Visentin \&amp; others, Clinically applicable deep learning for diagnosis and referral in retinal disease, {Nature medicine}, v(9), 1342--1350 (2018).">Fauw</a></sup>.

-   Optical coherence tomography is used most often in ophthalmology, but can be used wherever translucent tissues are found.
    -   Effective in early detection of macular degeneration, diabetic retinopathy, glaucoma, and other retinal diseases <sup id="6f749bf4e5bb6903f28c6f030daa5a1a"><a href="#aumann" title="@incollection{aumann,
          title={Optical Coherence Tomography (OCT): Principle and Technical Realization},
          author={Aumann, Silke and Donner, Sabine and Fischer, J{\o}rg and M{\u}ller, Frank},
          booktitle={High Resolution Imaging in Microscopy and Ophthalmology},
          pages={59--85},
          year={2019},
          publisher={Springer}
        }">aumann</a></sup>.

    -   The ability of OCT to measure the thickness of retinal layers makes it uniquely suitable for glaucoma diagnosis.

    -   First introduced in 1996, an opthalmic OCT device was first introduced to the market, but was unpopular because of the low resolution and slow speed of TD-OCT <sup id="6f749bf4e5bb6903f28c6f030daa5a1a"><a href="#aumann" title="@incollection{aumann,
          title={Optical Coherence Tomography (OCT): Principle and Technical Realization},
          author={Aumann, Silke and Donner, Sabine and Fischer, J{\o}rg and M{\u}ller, Frank},
          booktitle={High Resolution Imaging in Microscopy and Ophthalmology},
          pages={59--85},
          year={2019},
          publisher={Springer}
        }">aumann</a></sup>.
    -   In 2006, SD-OCT devices were first introduced, and have become indispensable to many diagnosticians <sup id="6f749bf4e5bb6903f28c6f030daa5a1a"><a href="#aumann" title="@incollection{aumann,
          title={Optical Coherence Tomography (OCT): Principle and Technical Realization},
          author={Aumann, Silke and Donner, Sabine and Fischer, J{\o}rg and M{\u}ller, Frank},
          booktitle={High Resolution Imaging in Microscopy and Ophthalmology},
          pages={59--85},
          year={2019},
          publisher={Springer}
        }">aumann</a></sup>.

-   Optical coherence tomography angiography is an angiography technique which uses OCT scans to image the vasculature of the eye in higher-definition than dye angiography and without the risk of dye injection <sup id="da8adc90d2537b97e3de9da5493a9f89"><a href="#tan2018overview" title="Tan, Tan, Denniston, Keane, Ang, Milea, Chakravarthy \&amp; Cheung, An overview of the clinical applications of optical coherence tomography angiography, {Eye}, v(2), 262--286 (2018).">tan2018overview</a></sup>.


## Improvements {#improvements}

-   In ophthalmology, the bottleneck lies not in performing OCT scans, but in diagnosing eye conditions and making appropriate referrals from these scans <sup id="a3770611f451f8dd05948bd4fef01fc9"><a href="#Fauw" title="De Fauw, Ledsam, Romera-Paredes, Nikolov, Tomasev, Blackwell, Askham, Glorot, O&#8217;Donoghue, Visentin \&amp; others, Clinically applicable deep learning for diagnosis and referral in retinal disease, {Nature medicine}, v(9), 1342--1350 (2018).">Fauw</a></sup>.

-   In 2018, researchers at Google's DeepMind proposed a neural network that could perform segmentation, diagnosis, and make referral recommendations based on 3D OCT scans with accuracy equal to or exceeding that of ophthalmologists <sup id="a3770611f451f8dd05948bd4fef01fc9"><a href="#Fauw" title="De Fauw, Ledsam, Romera-Paredes, Nikolov, Tomasev, Blackwell, Askham, Glorot, O&#8217;Donoghue, Visentin \&amp; others, Clinically applicable deep learning for diagnosis and referral in retinal disease, {Nature medicine}, v(9), 1342--1350 (2018).">Fauw</a></sup>.
    -   Their model was trained on only 14,884 scans and works on a wide-range of commercially available OCT scanners.

{{< figure src="/ox-hugo/screenshot2020-04-14_11-54-04_.png" >}}

-   Their model is composed of two neural networks, a supervised segmentation network which identifies tissues boundaries surround the macula—the central region of the retina—and a supervised classification network which makes diagnosis and referral decisions based on 14,884 scan-diagnosis training pairs.

-   While their model shows promise, a randomized controlled trial will need to be performed to determine its effectiveness.

# Bibliography
<a id="optical"></a>[optical] Huang, Swanson, Lin, Schuman, Stinson, Chang, Hee, Flotte, Gregory, Puliafito & others, Optical coherence tomography, <i>science</i>, <b>254(5035)</b>, 1178-1181 (1991). [↩](#4313277ed1d56c552d84008ff59b3d64)

<a id="aumann"></a>[aumann] @incollectionaumann,
  title=Optical Coherence Tomography (OCT): Principle and Technical Realization,
  author=Aumann, Silke and Donner, Sabine and Fischer, J\"org and M\"uller, Frank,
  booktitle=High Resolution Imaging in Microscopy and Ophthalmology,
  pages=59-85,
  year=2019,
  publisher=Springer
 [↩](#6f749bf4e5bb6903f28c6f030daa5a1a)

<a id="twenty"></a>[twenty] De Boer, Leitgeb & Wojtkowski, Twenty-five years of optical coherence tomography: the paradigm shift in sensitivity and speed provided by Fourier domain OCT, <i>Biomedical optics express</i>, <b>8(7)</b>, 3248-3280 (2017). [↩](#ab389edaabf8d841f5719d0cf64006a3)

<a id="Fauw"></a>[Fauw] De Fauw, Ledsam, Romera-Paredes, Nikolov, Tomasev, Blackwell, Askham, Glorot, O’Donoghue, Visentin & others, Clinically applicable deep learning for diagnosis and referral in retinal disease, <i>Nature medicine</i>, <b>24(9)</b>, 1342-1350 (2018). [↩](#a3770611f451f8dd05948bd4fef01fc9)

<a id="tan2018overview"></a>[tan2018overview] Tan, Tan, Denniston, Keane, Ang, Milea, Chakravarthy & Cheung, An overview of the clinical applications of optical coherence tomography angiography, <i>Eye</i>, <b>32(2)</b>, 262-286 (2018). [↩](#da8adc90d2537b97e3de9da5493a9f89)
