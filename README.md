# Piecewise Compensated High-PSRR-Bandgap-Voltage-Reference

- Low headroom Piecewise Compensated High PSRR Bandgap Voltage Reference using GPDK90. This is done as a course requirement for the Major Project of my 7th sem B.Tech<br>

## Specification
(V<sub>DDA</sub> = 3.3V, T<sub>J</sub> = 27°C, C<sub>L</sub> = 5pF unless otherwise specified below)

| Parameter                              | Symbol      | Condition                          | Min  | Typ  | Max  | Units |
|----------------------------------------|-------------|------------------------------------|------|------|------|-------|
| Bias Current for Bandgap               | IDDA        | VDDA=3.3, TJ=27°C                 |      | 10   |      | µA    |
| Output Voltage Process Dependence      | VREF(P)     | Over Strong-Weak Corners          | 0.665| 0.675| 0.685| V     |
| Output Voltage Temperature Dependence  | VREF(T)     | Over -40°C ≤ T ≤ 125°C            | 0.665| 0.675| 0.685| V     |
| Output Voltage VDDA Dependence         | VREF(VDDA)  | 1 ≤ VDDA ≤ 3.3                 | 0.665| 0.675| 0.685| V     |
| VREF dependence on VDDA                | PSRR        | vref/vdda at 1kHz                 |      | -60  |      | dB    |
| Phase Margin                           | PM          | PM of combined ±feedback loops    |      |  50  |      | Deg   |
<!--| VREF from Start Up Test Bench          | VREF(SU)    | \|1.35 - VREF(SU)\| at 100µs      |      |      | 10   | mV    | --> 

## Circuit
<p align="center">
  <img src="https://github.com/user-attachments/assets/6e4d250c-0f1a-47f3-af61-96d316cf9583" alt="X">
</p>


##  BGR
- Second Order Curvature Corrected Bandgap Reference Schematic
<p align="center">
  <img src="https://github.com/user-attachments/assets/f91a1ffa-58b7-42c9-8c17-b5be30c7f781" alt="Centered Image">
</p>

-- Referemce Voltage wrt to Temperature
  <p align="center">
  <img src="https://github.com/user-attachments/assets/1219168d-857b-454d-9070-cf58ab1bee7d" alt="Centered Image">
  </p>


- First Order Curvature Corrected Bandgap Reference Schematic
<p align="center">
  <img src="https://github.com/user-attachments/assets/4e8737b3-b363-4dd1-acbf-7553e7bd1e58" alt="Centered Image">
</p>

## OTA
