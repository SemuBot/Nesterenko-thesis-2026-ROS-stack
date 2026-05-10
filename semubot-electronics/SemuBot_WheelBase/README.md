# Wheelbase

## Overview

This project implements a BLDC motor control wheelbase using an STM32 microcontroller, 3-phase gate drivers, and high-precision current sensing.

---

## Components

### Microcontroller
* **STM32F303RET6**

### BLDC Driver
* **DRV8353FSRTAR**
  3-phase gate driver for MOSFET control.

### Current Sensing
* **ADS131M03IRUKT**
  3-channel, 24-bit, simultaneous-sampling Delta-Sigma ADC for current measurement.

### MOSFETs
* **AON7262E**
  N-channel MOSFETs for power stage switching.

### Voltage Regulation
* **RT9013-33GB**
  3.3V LDO regulator.

### Power Input & Connectors
* **XT30PW-M**
  Main DC power input connector.

* **MR30PW-M**
  Motor phase power connection.

* **10155435-00011LF (Amphenol)**
  USB Type-C connector.

* **B5B-XH-A_LF__SN_ (JST XH)**
  5-pin connector for peripherals (e.g., Hall/Sensor inputs).

* **DS1013-10SSIB1**
  General purpose I/O connector.

### ESD Protection
* **PRTR5V0U2X**
  ESD protection for data lines.

### Timing & Clock
* **ECS-2520MVLC-081.92-CN-TR**
  8.192 MHz Oscillator.
* **X322516MLB4SI**
  Secondary oscillator for system timing.

### User Interface
* **SWT0211-050010GSA_REVA**
  Tactile switch for system reset or user input.

---

## Technical Summary

### Power Stage
* **MOSFETs:** 18x AON7262E
* **Gate Drivers:** 3x DRV8353FSRTAR
* **Current Sense Resistors:** 9x 10mΩ (2512 package)



