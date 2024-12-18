# Piecewise Compensated High-PSRR-Bandgap-Voltage-Reference

- Piecewise Compensated High PSRR Bandgap Voltage Reference using GPDK90. 

## Specification
(V<sub>DDA</sub> = 2.5V, T<sub>J</sub> = 27°C, C<sub>L</sub> = 5pF unless otherwise specified below)

| Parameter                              | Symbol      | Condition                          | Min  | Typ  | Max  | Units |
|----------------------------------------|-------------|------------------------------------|------|------|------|-------|
| Bias Current for Bandgap               | IDDA        | VDDA=2.5, TJ=27°C                 |      | 10   |      | µA    |
| Output Voltage Process Dependence      | VREF(P)     | Over Strong-Weak Corners          | 0.645 | 0.650| 0.655| V     |
| Output Voltage Temperature Dependence  | VREF(T)     | Over -40°C ≤ T ≤ 125°C            | 0.645| 0.650| 0.655| V     |
| Output Voltage VDDA Dependence         | VREF(VDDA)  | 1 ≤ VDDA ≤ 2.5                    | 0.645| 0.650| 0.655|  V     |
| VREF dependence on VDDA                | PSRR        | vref/vdda at 1kHz                 |      | -60  |      | dB    |
| Phase Margin                           | PM          | PM of combined ±feedback loops    |      |  50  |      | Deg   |
<!--| VREF from Start Up Test Bench          | VREF(SU)    | \|1.35 - VREF(SU)\| at 100µs      |      |      | 10   | mV    | --> 

## Circuit
<p align="center">
  <img src="https://github.com/user-attachments/assets/5c2bd357-5951-4b2b-8f29-b7295e56793b" alt="X">
</p>

## Piecewise Compensated Second Order Curvature corrected BGR
- **Second Order Curvature Corrected Bandgap Reference Schematic**
<p align="center">
  <img src="https://github.com/user-attachments/assets/ff6e6bf6-733e-461a-ac23-5595cf6b1d97" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage wrt to Temperature**<br>
     - I have added an extra exponential current to Iref to cancel higher order terms in Iref (Especially ones from Vbe).<br>
     - This has been realized by pushing Iref current to a resistor and this is sensed by a mosfet in subthreshold region and this exponential current is pushed to Iref to cancel higher order terms in Iref.<br>
     - As you can see this Bandgap Reference has a very small Temperature coefficient across temperature making it very accurate<br>
     - **Temperature Coefficient = 4.4ppm/°C**<br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1b80d940-3ce1-41d8-8bd0-170feee953a5" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage across Different Process Corners (FF,FS,TT,SF,SS) and Temperature**
<p align="center">
  <img src="https://github.com/user-attachments/assets/e93fa2a8-b90c-47e0-9e59-2e60372731ca" alt="Centered Image">
</p>

- **Higher Order Compensation Current**  
  - This compensation current has been added to compensate for higher-order terms within the Bandgap Reference. This is a function of both PTAT and CTAT higher-order terms.  
  - The curve is kind of exponential in nature, but it is much more complex and contains higher-order dependencies of ( VBE), especially ( Is) (Saturation Current), which has higher-order dependencies on temperature.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a502581-43e5-4b58-9e3c-86a54abb65f4" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage wrt Supply Voltage Sweep**  
  - Supply voltage is swept from 0 to 2.5V. The BGR and OTA wake up and start working properly around 1V. Later, the reference voltage mostly remains constant.

<p align="center">
  <img src="https://github.com/user-attachments/assets/1bbd5559-3357-4e8e-a73f-d4fa7126d1e9" alt="Centered Image">
</p>

- **PSRR of the Piecewise Compensated Bandgap Voltage Reference**  
  - The PSRR of the BGR at DC is -86dB and -76dB at 1kHz. This is due to the use of a high-swing cascode current mirror in the BGR and a bias network that also tracks the supply ripple, essentially attenuating it.

<p align="center">
  <img src="https://github.com/user-attachments/assets/46b0ac8a-9b5a-4d13-9531-29da682a4cbd" alt="Centered Image">
</p>

- **Stability of the Combined Feedback Loop**  
  - The phase margin of the combined feedback loop of the BGR is 61.34° and the unity gain bandwidth is 5MHz.  
  - The gain margin of the feedback loop is 18.33dB.  
  - The negative feedback loop is stable and capable of settling transients within 1µs.

<p align="center">
  <img src="https://github.com/user-attachments/assets/4f264ae7-e5e1-42eb-9fbf-592d42d3a127" alt="Centered Image">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/29adc811-3d15-49cc-b1e5-eca5379057ce" alt="Centered Image">
</p>

- **Startup time of the Piecewise Compensated Bandgap Voltage Reference**  
  - The startup time of the Bandgap Reference (BGR) is approximately 338 ns. The startup circuit quickly transitions the BGR from a zero-current state to its stable operating point, ensuring rapid stabilization.
      
<p align="center">
  <img src="https://github.com/user-attachments/assets/a13c435a-f227-467c-9add-d9308f432930" alt="Centered Image">
</p>


- **Noise Analysis of the Piecewise Compensated Bandgap Voltage Reference**
<p align="center">
  <img src="https://github.com/user-attachments/assets/784a2c1c-ced9-4e38-b37e-664b7ba29127" alt="Centered Image">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/369d4276-962a-4d64-bd45-34ad453cd5a4" alt="Centered Image">
</p>

- **Monte Carlo Simulations**  
  - The 200mV and 300mV are due to startup convergence issues; other than that, most of the time, Vref is close to 650mV.  

<p align="center">
  <img src="https://github.com/user-attachments/assets/09b5f7f5-21c6-445b-9507-06af8d6c0b1a" alt="Centered Image">
</p>

## OTA

- **OTA Schematic**
<p align="center">
  <img src="https://github.com/user-attachments/assets/9e0f1edc-f944-4a49-8ca6-bda8e6b66f73" alt="Centered Image">
</p>


- GBW: 4.885MHz (NN/TT)
- Phase Margin: 76.2° (NN/TT)
 
- **OTA Gain and Phase across Different Process Corners (FF, FS, TT, SF, SS) and Temperature**  
  - Across different process corners (SS, SF, FF, FS, TT) and temperatures (-40 °C, 27 °C, 125 °C), the gain of the OTA remains sufficiently high, and the GBW is between 3.5MHz to 7MHz.
<p align="center">
  <img src="https://github.com/user-attachments/assets/2ba33913-77e3-4222-8c89-c8ca63ee6d26" alt="Centered Image">
</p>


## Reference
**[1]**. A high PSRR bandgap voltage reference with piecewise compensation Longcheng Que, Daogang Min, Linhai Wei, Yun Zhou, Jian Lv <br>
**[2]**. A 1-V 3.1-ppm/°C 0.8-ju.W Bandgap Reference with Piecewise Exponential Curvature Compensation Hongrui Luo, Quan Sun, Ruizhi Zhang, Hong Zhang <br>
**[3]**. A Curvature Compensation Technique for Low-Voltage Bandgap Reference Jie Shen, Houpeng Chen, Shenglan Ni and Zhitang Song <br>
**[4]**. Design of a High Precision Band-gap Reference with Piecewise-Linear Compensation Lei Quan, Yongsheng Yin , Xinbo Yang, Honghui Deng <br>
**[5]**. Ka Nang Leung and P. K. T. Mok, "A sub-1-V 15-ppm//spl deg/C CMOS bandgap voltage reference without requiring low threshold voltage device," in IEEE Journal of Solid-State Circuits, vol. 37, no. 4, pp. 526-530, April 2002, doi: 10.1109/4.991391.<br>

