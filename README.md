# Piecewise Compensated High-PSRR-Bandgap-Voltage-Reference

- Low headroom Piecewise Compensated High PSRR Bandgap Voltage Reference using GPDK90. This is done as a course requirement for the Major Project of my B.Tech<br>

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
  <img src="XXXX" alt="Centered Image">
</p>

##  BGR
- First Order Curvature Corrected Bandgap Reference Schematic
<p align="center">
  <img src="https://github.com/user-attachments/assets/28f56c4c-c6ba-4de6-827e-1b2388376da9" alt="Centered Image">
</p>

- **Stability Analysis across different Process corners**<br>


    - Typical (tt)
    <p align="center">
      <img src="https://github.com/user-attachments/assets/e32bb8fe-b826-46df-8414-90f43c41c672" alt="Centered Image">
    </p>
    <p align="center">
      <img src="https://github.com/user-attachments/assets/432ec8d8-2ebc-4f98-853f-0a7bccb4009e" alt="Centered Image">
    </p>


    - Slow (ss)
    <p align="center">
      <img src="https://github.com/user-attachments/assets/9e3e11ed-f33e-4c02-bbd9-431ae6bd48f1" alt="Centered Image">
    </p>
    <p align="center">
      <img src="https://github.com/user-attachments/assets/4ee775e2-04c5-444f-b474-74bad873d970" alt="Centered Image">
    </p>


    - Fast (ff)
    <p align="center">
      <img src="https://github.com/user-attachments/assets/5526efe8-fdfd-43a8-9056-2c79c152647b" alt="Centered Image">
    </p>
    <p align="center">
      <img src="https://github.com/user-attachments/assets/eb6c21d7-e6b7-40b0-a931-c30c49dff4de" alt="Centered Image">
    </p>

    - Combined
    <p align="center">
      <img src="https://github.com/user-attachments/assets/3efa919f-2919-4133-949d-457a6cf796c1" alt="Centered Image">
    </p>

