<!-- GNU RADIO BANNER START -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=GNU%20RADIO&fontSize=60&fontColor=ffffff&fontAlignY=40&desc=Communication%20%26%20Signal%20Processing%20Laboratory&descAlignY=62&descSize=18" width="100%"/>

<br>

<img src="https://img.shields.io/badge/GNU%20Radio-3.x-blue?style=for-the-badge&logo=gnuradio&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/DSP-Signal%20Processing-purple?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Communication%20Systems-ECE-green?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Labs-12%2F12%20Completed-success?style=for-the-badge"/>

</div>

<!-- GNU RADIO BANNER END -->

# GNU Radio — Communication & Signal Processing Laboratory

A structured collection of **GNU Radio Companion (GRC)** experiments covering analog modulation, digital modulation, wireless communication concepts, channel effects, signal analysis, and audio signal processing.

This repository documents practical **Software-Defined Radio (SDR)** and **Digital Signal Processing (DSP)** experiments implemented using GNU Radio Companion.

---

## About the Project

This repository contains a progressive set of GNU Radio laboratory experiments designed to connect theoretical concepts from **Communication Systems** and **Digital Signal Processing** with practical signal-processing implementations.

The experiments include:

* Analog modulation and demodulation
* DSB-SC modulation
* Frequency Modulation
* Digital modulation techniques
* QPSK transmission and reception
* OFDM
* Multipath fading
* Signal-to-Noise Ratio analysis
* Audio signal visualization
* Time-domain and frequency-domain analysis

Each laboratory experiment contains the GNU Radio flowgraph, generated Python implementation where applicable, experiment documentation, and screenshots of the implemented system and outputs.

---

## Tools & Technologies

| Tool / Technology       | Purpose                                         |
| ----------------------- | ----------------------------------------------- |
| **GNU Radio Companion** | Signal-processing flowgraph development         |
| **GNU Radio**           | Software-defined radio and DSP implementation   |
| **Python**              | Generated and supporting signal-processing code |
| **Git**                 | Version control                                 |
| **GitHub**              | Project documentation and source-code hosting   |

---

# Laboratory Experiments

## Lab 01 — AM Modulation

**Topic:** Amplitude Modulation

Implementation and analysis of an AM signal using GNU Radio Companion.

**Key concepts:**

* Carrier signal
* Message signal
* Amplitude modulation
* Time-domain waveform
* Frequency-domain spectrum

[Open Lab 01 →](labs/lab01_am_modulation/)

---

## Lab 02 — AM Demodulation

**Topic:** Amplitude Demodulation

Practical implementation of AM demodulation and observation of the recovered signal.

**Key concepts:**

* AM reception
* Demodulation
* Signal recovery
* Time-domain analysis

[Open Lab 02 →](labs/lab02_am_demodulation/)

---

## Lab 03 — AM Modulation & Demodulation

**Topic:** Complete AM Communication System

Simulation of an AM transmitter and receiver chain using GNU Radio.

**Key concepts:**

* Message generation
* AM modulation
* Transmission
* AM demodulation
* Recovered signal

[Open Lab 03 →](labs/lab03_am_modulation_demodulation/)

---

## Lab 04 — DSB-SC Amplitude Modulation

**Topic:** Double Sideband Suppressed Carrier

Implementation and analysis of DSB-SC modulation.

**Key concepts:**

* Double sideband modulation
* Suppressed carrier
* Product modulation
* Time-domain analysis
* Frequency-domain analysis

[Open Lab 04 →](labs/lab04_dsb_sc_amplitude_modulation/)

---

## Lab 05 — FM Simulation

**Topic:** Frequency Modulation

Simulation and visualization of a frequency-modulated signal using GNU Radio.

**Key concepts:**

* Frequency modulation
* Instantaneous frequency
* Frequency deviation
* Quadrature and in-phase components
* Spectrum analysis
* Waterfall visualization

[Open Lab 05 →](labs/lab05_fm_simulation/)

---

## Lab 06 — ASK Modulation

**Topic:** Amplitude Shift Keying

Implementation of an ASK transmitter and receiver system.

**Key concepts:**

* Digital modulation
* Binary data
* Amplitude shift keying
* Transmitter and receiver
* Signal visualization

[Open Lab 06 →](labs/lab06_ask_modulation/)

---

## Lab 07 — FSK Modulation

**Topic:** Frequency Shift Keying

Implementation and analysis of an FSK modulation and demodulation system.

**Key concepts:**

* Binary FSK
* Frequency shifting
* Digital communication
* Time-domain analysis
* Frequency-domain analysis

[Open Lab 07 →](labs/lab07_fsk_modulation/)

---

## Lab 08 — QPSK Modulation & Demodulation

**Topic:** Quadrature Phase Shift Keying

Implementation of a QPSK communication system with modulation and demodulation stages.

**Key concepts:**

* QPSK
* In-phase component
* Quadrature component
* Constellation representation
* AWGN channel
* Transmitter and receiver

[Open Lab 08 →](labs/lab08_qpsk_mod_demod/)

---

## Lab 09 — OFDM

**Topic:** Orthogonal Frequency Division Multiplexing

Implementation and analysis of an OFDM transmission system.

**Key concepts:**

* OFDM
* Orthogonal subcarriers
* Transmitted and received signals
* OFDM spectrum
* Transceiver implementation

[Open Lab 09 →](labs/lab09_ofdm/)

---

## Lab 10 — Multipath Fading

**Topic:** Wireless Channel Effects

Simulation of multipath propagation and its effect on a transmitted signal.

**Key concepts:**

* Multipath propagation
* Fading
* Wireless channel
* Signal distortion
* Channel effects

[Open Lab 10 →](labs/lab10_multipath_fading/)

---

## Lab 11 — Signal-to-Noise Ratio (SNR)

**Topic:** SNR Analysis

Analysis of the effect of noise on an audio signal using GNU Radio visualization tools.

**Key concepts:**

* Signal-to-Noise Ratio
* Noise
* Signal quality
* Time-domain analysis
* FFT analysis
* Relative gain
* Frequency-domain analysis

[Open Lab 11 →](labs/lab11_snr/)

---

## Lab 12 — SAM Music Studio

**Topic:** Audio Signal Processing & Visualization

A GNU Radio audio-processing experiment combining multiple visualization techniques for analyzing an audio signal.

**Key concepts:**

* Audio signal processing
* Time-domain waveform
* Frequency-domain spectrum
* Relative gain
* Waterfall display
* Time-varying spectral analysis

[Open Lab 12 →](labs/lab12_sam_music_studio/)

---

# Repository Structure

```text
GNU-RADIO/
│
├── README.md
├── .gitignore
│
└── labs/
    │
    ├── lab01_am_modulation/
    ├── lab02_am_demodulation/
    ├── lab03_am_modulation_demodulation/
    ├── lab04_dsb_sc_amplitude_modulation/
    ├── lab05_fm_simulation/
    ├── lab06_ask_modulation/
    ├── lab07_fsk_modulation/
    ├── lab08_qpsk_mod_demod/
    ├── lab09_ofdm/
    ├── lab10_multipath_fading/
    ├── lab11_snr/
    └── lab12_sam_music_studio/
```

Each laboratory directory generally contains:

```text
labXX/
├── README.md
├── flowgraph/
├── python/
└── screenshots/
```

### Directory Description

| Directory      | Contents                         |
| -------------- | -------------------------------- |
| `README.md`    | Experiment documentation         |
| `flowgraph/`   | GNU Radio Companion `.grc` files |
| `python/`      | Generated Python implementations |
| `screenshots/` | Flowgraph and output screenshots |

---

# Learning Progression

The experiments progress from fundamental analog communication concepts toward more advanced digital communication and signal-processing concepts.

```text
Analog Communication
        │
        ├── AM Modulation
        ├── AM Demodulation
        ├── AM Transmitter & Receiver
        ├── DSB-SC
        └── FM
        │
        ▼
Digital Communication
        │
        ├── ASK
        ├── FSK
        └── QPSK
        │
        ▼
Advanced Communication Systems
        │
        ├── OFDM
        └── Multipath Fading
        │
        ▼
Signal Analysis
        │
        ├── SNR Analysis
        └── Audio Signal Visualization
```

---

# Skills Demonstrated

Through these experiments, the repository demonstrates practical experience with:

* Communication system simulation
* Analog modulation
* Digital modulation
* Signal generation
* Signal demodulation
* Digital signal processing
* Fourier analysis
* FFT-based spectrum analysis
* Time-domain analysis
* Frequency-domain analysis
* Wireless channel modelling
* Multipath fading
* OFDM
* SNR analysis
* Audio signal processing
* GNU Radio Companion
* Python-based signal processing
* Software-defined radio concepts

---

# Screenshots & Experimental Evidence

Each laboratory contains screenshots documenting:

* GNU Radio flowgraph implementation
* Signal waveforms
* Frequency-domain representations
* Spectral characteristics
* Constellation or visualization outputs where applicable
* Waterfall displays
* Transmitted and received signals

These screenshots provide practical evidence of the implemented experiments and observed outputs.

---

# Repository Status

| Laboratory                              | Status      |
| --------------------------------------- | ----------- |
| Lab 01 — AM Modulation                  | ✅ Completed |
| Lab 02 — AM Demodulation                | ✅ Completed |
| Lab 03 — AM Modulation & Demodulation   | ✅ Completed |
| Lab 04 — DSB-SC                         | ✅ Completed |
| Lab 05 — FM Simulation                  | ✅ Completed |
| Lab 06 — ASK Modulation                 | ✅ Completed |
| Lab 07 — FSK Modulation                 | ✅ Completed |
| Lab 08 — QPSK Modulation & Demodulation | ✅ Completed |
| Lab 09 — OFDM                           | ✅ Completed |
| Lab 10 — Multipath Fading               | ✅ Completed |
| Lab 11 — SNR Analysis                   | ✅ Completed |
| Lab 12 — SAM Music Studio               | ✅ Completed |

**Current progress: 12 / 12 laboratories completed.**

---

# Objective

The primary objective of this repository is to develop practical understanding of communication and signal-processing concepts through hands-on GNU Radio implementations.

The experiments are intended to bridge the gap between:

**Mathematical Theory → Communication Concepts → GNU Radio Flowgraphs → Practical Signal Analysis**

---

# Future Work

Future experiments may extend this repository toward more advanced topics such as:

* Digital communication channels
* AWGN channel analysis
* BER analysis
* Constellation analysis
* Channel coding
* Equalization
* Synchronization
* SDR hardware integration
* Wireless communication systems
* Cognitive radio concepts
* OFDM enhancements
* Software-defined radio applications

---

## Author

**Saswati Mathan**

M.Tech — Electronics & Communication Engineering
Specialization: Communication

---

## Platform

**GNU Radio Companion (GRC)**

Repository:

**GNU-RADIO — Communication & Signal Processing Laboratory**
