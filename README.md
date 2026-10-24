# Multi-Pattern LED Generator

A digital electronics project that generates multiple LED lighting patterns using timer, counter and logic-gate circuits. The project combines a physical hardware implementation with a Python simulation of LED patterns.

## Project Overview

The circuit uses an NE555 timer to generate clock pulses and a CD4017 decade counter to produce sequential outputs. A 7432 OR gate and switches are used to combine outputs and select LED patterns.

A Python Tkinter application was also developed to simulate five LEDs and demonstrate switch-controlled lighting patterns.

## Hardware Implementation

The hardware was assembled on a breadboard using the following components:

- NE555 timer IC
- CD4017 decade counter
- 7432 OR gate IC
- Five yellow LEDs with current-limiting resistors
- SPST switches
- 10 kΩ potentiometer
- Capacitors, jumper wires and a 9 V power supply

### Hardware Photos

The `hardware/` folder contains photographs of the physical circuit from different angles.

## Python Simulation

The Python simulation uses Tkinter to display five LEDs and two switches. The switch states determine which LED pattern is displayed, with the simulation updating periodically.

**Language:** Python  
**GUI framework:** Tkinter

Source code: [`led_pattern_generator.py`](python-simulation/%20led_pattern_generator.py)
## Key Concepts

- Clock pulse generation using a 555 timer
- Sequential logic and decade counters
- Combinational logic using OR gates
- Switch-based pattern selection
- Hardware implementation and software simulation

## Repository Structure

```text
multi-pattern-led-generator/
├── hardware/
│   └── Hardware photos
├── python-simulation/
│   └── led_pattern_generator.py
├── docs/
│   └── Project_Report.pdf
└── README.md
```

## Project Type

Academic team project in digital electronics, combining a physical circuit with a Python-based simulation.

## Acknowledgment

Developed as part of a collaborative academic project. The repository documents the hardware implementation and the associated Python simulation.
