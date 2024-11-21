# Piecewise Compensated High-PSRR-Bandgap-Voltage-Reference

- Low headroom Piecewise Compensated High PSRR Bandgap Voltage Reference using GPDK90. 

## Specification
(V<sub>DDA</sub> = 2.5V, T<sub>J</sub> = 27°C, C<sub>L</sub> = 5pF unless otherwise specified below)

| Parameter                              | Symbol      | Condition                          | Min  | Typ  | Max  | Units |
|----------------------------------------|-------------|------------------------------------|------|------|------|-------|
| Bias Current for Bandgap               | IDDA        | VDDA=2.5, TJ=27°C                 |      | 10   |      | µA    |
| Output Voltage Process Dependence      | VREF(P)     | Over Strong-Weak Corners          | 0.645 | 0.650| 0.655| V     |
| Output Voltage Temperature Dependence  | VREF(T)     | Over -50°C ≤ T ≤ 150°C            | 0.645| 0.650| 0.655| V     |
| Output Voltage VDDA Dependence         | VREF(VDDA)  | 1 ≤ VDDA ≤ 2.5                    | 0.645| 0.650| 0.655|  V     |
| VREF dependence on VDDA                | PSRR        | vref/vdda at 1kHz                 |      | -60  |      | dB    |
| Phase Margin                           | PM          | PM of combined ±feedback loops    |      |  50  |      | Deg   |
<!--| VREF from Start Up Test Bench          | VREF(SU)    | \|1.35 - VREF(SU)\| at 100µs      |      |      | 10   | mV    | --> 

## Circuit
<p align="center">
  <img src="https://github.com/user-attachments/assets/a5326e8c-8563-4fb8-977d-4a9b34e025ba" alt="X">
</p>

## Piecewise Compensated Second Order Curvature corrected BGR
- **Second Order Curvature Corrected Bandgap Reference Schematic**
<p align="center">
  <img src="https://github.com/user-attachments/assets/e1870e46-155e-4db6-ae63-ccee76983fe8" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage wrt to Temperature**<br>
     - I have added an extra exponential current to Iref to cancel higher order terms in Iref (Especially ones from Vbe).<br>
     - This has been realized by pushing Iref current to a resistor and this is sensed by a mosfet in subthreshold region and this exponential current is pushed to Iref to cancel higher order terms in Iref.<br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1219168d-857b-454d-9070-cf58ab1bee7d" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage across Different Process Corners (FF,FS,TT,SF,SS)**
<p align="center">
  <img src="https://github.com/user-attachments/assets/6292ec19-442f-45c2-8cf2-8e4a4ae8161a" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage wrt Supply Voltage sweep**
<p align="center">
  <img src="https://github.com/user-attachments/assets/27878cf2-08a0-4e32-8f99-9638677d0697" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage Change wrt Temperature**<br>
    - As you can see this Bandgap Reference has a very small Temperature coefficient across temperature making it very accurate
    - **Temperature Coefficient = 0.7ppm/°C**
<p align="center">
  <img src="https://github.com/user-attachments/assets/807277d9-475a-4f14-ab4f-66bd54617f67" alt="Centered Image">
</p>


## First Order Bandgap Reference Schematic
<p align="center">
  <img src="https://github.com/user-attachments/assets/ab9723e8-e332-417d-8fc6-dd6d3e69cd26" alt="Centered Image">
</p>

- **First Order Bandgap Reference Voltage wrt to Temperature**
<p align="center">
  <img src="https://github.com/user-attachments/assets/98212ab5-0599-4d20-b7f7-460fb5422447" alt="Centered Image">
</p>

- **Second Order Curvature Corrected Reference Voltage Change wrt Temperature**<br>
    - **Temperature Coefficient = 4ppm/°C**
<p align="center">
  <img src="https://github.com/user-attachments/assets/38e08011-efec-408b-baf4-801ff1f0977f" alt="Centered Image">
</p>

   - **Second Order Curvature Corrected Reference Voltage across Different Process Corners (FF,FS,TT,SF,SS**<br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/bcf74cd5-2143-4e4a-ba26-32b5da708089" alt="Centered Image">
</p>

## OTA

## Reference
**[1]**. A high PSRR bandgap voltage reference with piecewise compensation Longcheng Que, Daogang Min, Linhai Wei, Yun Zhou, Jian Lv <br>
**[2]**. A 1-V 3.1-ppm/°C 0.8-ju.W Bandgap Reference with Piecewise Exponential Curvature Compensation Hongrui Luo, Quan Sun, Ruizhi Zhang, Hong Zhang <br>
**[3]**. A Curvature Compensation Technique for Low-Voltage Bandgap Reference Jie Shen, Houpeng Chen, Shenglan Ni and Zhitang Song <br>
**[4]**. Design of a High Precision Band-gap Reference with Piecewise-Linear Compensation Lei Quan, Yongsheng Yin , Xinbo Yang, Honghui Deng <br>
