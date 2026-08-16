# Lab 11 — Signal-to-Noise Ratio (SNR)

## 1. Aim

To study and analyze the **Signal-to-Noise Ratio (SNR)** of an audio signal using **GNU Radio Companion** and observe the effect of noise on the signal in both the time and frequency domains.

---

## 2. Objectives

The objectives of this experiment are:

- To understand the concept of Signal-to-Noise Ratio (SNR).
- To study the relationship between signal power and noise power.
- To analyze the effect of noise on an audio signal.
- To observe the signal in the time domain.
- To analyze the frequency-domain characteristics of the signal and noise.
- To observe relative gain and spectral characteristics using GNU Radio visualization blocks.
- To gain practical experience in signal and noise analysis using GNU Radio Companion.

---

## 3. Theory

### Signal-to-Noise Ratio (SNR)

**Signal-to-Noise Ratio (SNR)** is a fundamental parameter used to measure the strength of a desired signal relative to the background noise present in a communication or signal-processing system.

SNR is defined as the ratio of signal power to noise power:

$$
SNR = \frac{P_{signal}}{P_{noise}}
$$

where:

- $P_{signal}$ = power of the desired signal
- $P_{noise}$ = power of the noise

SNR is commonly expressed in decibels (dB):

$$
SNR_{dB} = 10\log_{10}\left(\frac{P_{signal}}{P_{noise}}\right)
$$

A higher SNR indicates that the desired signal is stronger compared with the noise, resulting in better signal quality.

A lower SNR indicates that the noise level is relatively high and can significantly affect the quality and reliability of the received signal.

### Interpretation of SNR

The SNR can be interpreted as follows:

- **High SNR:** The desired signal is dominant compared with noise.
- **Low SNR:** Noise is relatively strong compared with the desired signal.
- **Higher SNR:** Generally provides better signal quality and more reliable detection.
- **Lower SNR:** Generally results in greater signal degradation and reduced communication performance.

---

## 4. Importance of SNR

SNR is an important parameter in communication and signal-processing systems because noise can interfere with the desired information signal.

A high SNR generally provides:

- Better signal quality.
- More reliable communication.
- Improved signal detection.
- Lower probability of errors.
- Better audio and data recovery.

A low SNR can result in:

- Increased signal distortion.
- Reduced signal quality.
- Difficulty in signal detection.
- Increased error rate.
- Degraded communication performance.

---

## 5. SNR in Audio Signals

In an audio system, the desired audio signal may be affected by background noise.

The resulting signal can therefore be represented as:

$$
x(t) = s(t) + n(t)
$$

where:

- $s(t)$ = desired audio signal
- $n(t)$ = noise signal
- $x(t)$ = resulting noisy signal

The SNR provides a measure of how dominant the desired audio signal is compared with the noise.

GNU Radio can be used to visualize these signals and study their characteristics in both the time and frequency domains.

---

## 6. GNU Radio Implementation

The Signal-to-Noise Ratio experiment was implemented using **GNU Radio Companion**.

An audio signal was used as the desired signal and noise was introduced into the signal-processing chain.

GNU Radio visualization blocks were used to observe and analyze the resulting signal.

The experiment provides a practical method for studying the relationship between the desired signal and noise components.

---

## 7. GNU Radio Flowgraph

The implemented SNR analysis flowgraph is shown below.

### Flowgraph Screenshot 1

![SNR Flowgraph 1](screenshots/FLOWGRAPH-1.png)

### Flowgraph Screenshot 2

![SNR Flowgraph 2](screenshots/FLOWGRAPH-2.png)

### Flowgraph Screenshot 3

![SNR Flowgraph 3](screenshots/FLOWGRAPH-3.png)

The flowgraph contains the signal-processing and visualization stages required to observe the characteristics of the audio signal and the effect of noise.

---

## 8. Signal Analysis

The signal was analyzed using different GNU Radio visualization blocks.

### Time-Domain Analysis

The amplitude scope displays were used to observe the amplitude variation of the signal in the time domain.

The time-domain representation provides a direct view of how the signal amplitude changes with time.

### Frequency-Domain Analysis

FFT-based displays were used to observe the frequency-domain characteristics of the signal.

The frequency-domain representation helps identify the spectral components of the audio signal and the effects introduced by noise.

### Relative Gain and Frequency Analysis

Relative-gain and frequency displays provide additional information about signal strength and spectral distribution.

These displays help in understanding how signal energy is distributed across different frequency components.

---

## 9. Output Analysis

The experiment produced several visualization outputs corresponding to the time-domain and frequency-domain characteristics of the signal.

### Amplitude Scope and FFT

The amplitude scope and FFT displays provide information about the signal in the time and frequency domains.

#### Output 1

![Amplitude Scope FFT 1](screenshots/AMPLITUDE_SCOPE_FFT-1.png)

#### Output 2

![Amplitude Scope FFT 2](screenshots/AMPLITUDE_SCOPE_FFT-2.png)

These displays allow the signal amplitude and spectral characteristics to be observed simultaneously.

### Relative Gain and Frequency

The relative-gain and frequency displays provide additional information about signal strength and frequency distribution.

#### Output 3

![Relative Gain Frequency 1](screenshots/RELATIVE%20GAIN_FREQUENCY-1.png)

#### Output 4

![Relative Gain Frequency 2](screenshots/RELATIVE%20GAIN_FREQUENCY-2.png)

These visualizations help in analyzing the frequency-domain behavior and relative signal level.

---

## 10. Observations

1. The audio signal was successfully processed using GNU Radio Companion.
2. Noise was introduced into the signal-processing system.
3. The time-domain display showed the amplitude characteristics of the resulting signal.
4. The FFT display provided a frequency-domain representation of the signal.
5. The frequency-domain display showed the spectral components of the audio signal.
6. Relative-gain measurements provided an indication of signal strength across frequency.
7. The presence of noise affected the observed signal characteristics.
8. GNU Radio visualization tools allowed the signal and noise characteristics to be analyzed in both time and frequency domains.
9. The experiment demonstrated the practical importance of SNR in evaluating signal quality.

---

## 11. Effects of Noise on Signal Quality

Noise affects a signal by introducing unwanted components into the desired signal.

As the noise power increases:

- The SNR decreases.
- The signal becomes more difficult to distinguish from noise.
- The observed waveform becomes more affected by unwanted variations.
- Spectral components associated with noise become more significant.
- Signal detection and recovery can become more difficult.

Conversely, when the signal power is high relative to the noise power, the SNR increases and the desired signal becomes easier to identify.

---

## 12. Applications

SNR analysis is important in many communication and signal-processing applications, including:

- Audio and speech communication.
- Wireless communication systems.
- Radio communication.
- Digital communication systems.
- Signal detection and estimation.
- Radar and navigation systems.
- Satellite communication.
- Mobile communication.
- Noise reduction and filtering systems.
- Performance analysis of communication channels.

---

## 13. Files Included

### GNU Radio Flowgraph

```text
flowgraph/
└── SNR.grc
```

### Generated Python File

```text
python/
└── snr_samaudio.py
```

### Screenshots

```text
screenshots/
├── AMPLITUDE_SCOPE_FFT-1.png
├── AMPLITUDE_SCOPE_FFT-2.png
├── FLOWGRAPH-1.png
├── FLOWGRAPH-2.png
├── FLOWGRAPH-3.png
├── RELATIVE GAIN_FREQUENCY-1.png
└── RELATIVE GAIN_FREQUENCY-2.png
```

---

## 14. Result

**Signal-to-Noise Ratio analysis was successfully implemented using GNU Radio Companion.**

The experiment demonstrated the effect of noise on an audio signal and provided practical visualization of the resulting signal in both the time and frequency domains.

The amplitude, FFT, relative-gain, and frequency-domain displays helped analyze the characteristics of the signal and the effect of noise.

---

## 15. Conclusion

This experiment demonstrated the fundamental concept of **Signal-to-Noise Ratio (SNR)** in signal-processing and communication systems.

SNR provides a measure of the desired signal power relative to the noise power and is an important parameter for evaluating signal quality.

The experiment demonstrated how noise affects an audio signal and how GNU Radio visualization tools can be used to observe these effects in both the time and frequency domains.

GNU Radio provided a practical environment for connecting the theoretical concept of SNR with an actual signal-processing implementation.

---

**Experiment:** Lab 11 — Signal-to-Noise Ratio (SNR)

**Platform:** GNU Radio Companion
