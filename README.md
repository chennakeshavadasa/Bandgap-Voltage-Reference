# Piecewise Compensated High-PSRR-Bandgap-Voltage-Reference

- Low headroom Piecewise Compensated High PSRR Bandgap Voltage Reference using GPDK90. This is done as a course requirement for the Major Project of my 7th sem B.Tech<br>

## Specification
(V<sub>DDA</sub> = 2.5V, T<sub>J</sub> = 27°C, C<sub>L</sub> = 5pF unless otherwise specified below)

| Parameter                              | Symbol      | Condition                          | Min  | Typ  | Max  | Units |
|----------------------------------------|-------------|------------------------------------|------|------|------|-------|
| Bias Current for Bandgap               | IDDA        | VDDA=3.3, TJ=27°C                 |      | 10   |      | µA    |
| Output Voltage Process Dependence      | VREF(P)     | Over Strong-Weak Corners          | 0.665| 0.675| 0.685| V     |
| Output Voltage Temperature Dependence  | VREF(T)     | Over -40°C ≤ T ≤ 125°C            | 0.665| 0.675| 0.685| V     |
| Output Voltage VDDA Dependence         | VREF(VDDA)  | 1 ≤ VDDA ≤ 2.5                 | 0.665| 0.675| 0.685| V     |
| VREF dependence on VDDA                | PSRR        | vref/vdda at 1kHz                 |      | -60  |      | dB    |
| Phase Margin                           | PM          | PM of combined ±feedback loops    |      |  50  |      | Deg   |
<!--| VREF from Start Up Test Bench          | VREF(SU)    | \|1.35 - VREF(SU)\| at 100µs      |      |      | 10   | mV    | --> 

## Circuit
<p align="center">
  <img src="https://github.com/user-attachments/assets/6e4d250c-0f1a-47f3-af61-96d316cf9583" alt="X">
</p>


## Piecewise Compensated Second Order Curvature corrected BGR
- **Second Order Curvature Corrected Bandgap Reference Schematic**
<p align="center">
  <img src="https://github.com/user-attachments/assets/4f65204d-a1b2-40a2-9a01-4fda4514040d" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage wrt to Temperature**<br>
     - I have added an extra exponential current to Iref to cancel higher order terms in Iref.<br>
     - This has been realized by pushing Iref current to a resistor and this is sensed by a mosfet in subthreshold region and this exponential current is pushed to Iref to cancel higher order terms in Iref.<br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1219168d-857b-454d-9070-cf58ab1bee7d" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage wrt Supply Voltage sweep**
<p align="center">
  <img src="https://github.com/user-attachments/assets/27878cf2-08a0-4e32-8f99-9638677d0697" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage Change wrt Temperature**<br>
    - As you can see this Bandgap Reference has a very small Temperature coefficient across temperature making it very accurate
    - **Temperature Coeeficient = 0.7ppm/°C**
<p align="center">
  <img src="https://github.com/user-attachments/assets/807277d9-475a-4f14-ab4f-66bd54617f67" alt="Centered Image">
</p>


## First Order Curvature Corrected Bandgap Reference Schematic
<p align="center">
  <img src="https://github.com/user-attachments/assets/4e8737b3-b363-4dd1-acbf-7553e7bd1e58" alt="Centered Image">
</p>

## OTA

## Reference
**[1]**. A high PSRR bandgap voltage reference with piecewise compensation Longcheng Que, Daogang Min, Linhai Wei, Yun Zhou, Jian Lv <br>
**[2]**. A 1-V 3.1-ppm/°C 0.8-ju.W Bandgap Reference with Piecewise Exponential Curvature Compensation Hongrui Luo, Quan Sun, Ruizhi Zhang, Hong Zhang <br>
**[3]**. ACurvature Compensation Technique for Low-Voltage Bandgap Reference Jie Shen, Houpeng Chen, Shenglan Ni and Zhitang Song <br>
**[4]**. Design of a High Precision Band-gap Reference with Piecewise-Linear Compensation Lei Quan, Yongsheng Yin , Xinbo Yang, Honghui Deng <br>
