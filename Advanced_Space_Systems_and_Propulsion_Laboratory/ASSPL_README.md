# Lunar Optical Communication Simulation

## Overview
This repository contains simulation code developed during my undergraduate research at the Advanced Space Systems and Propulsion Laboratory. We are researching mirror-based optical communication systems for the moon, which involves bouncing light between mirrors to enable long-distance transmission and eliminate the need for physical cell-tower infrastructure.

## Wave-Optics Simulation
The included Python script (`rayleigh_simulation.py`) is a wave-optics simulation designed using the `LightPipes` package. 

**Key Functionality:**
* Models light propagating between two mirrors across a 100 km distance segment.
* Quantifies round-trip optical losses and calculates simulated transmission efficiency.
* Validates the simulation by cross-testing against known analytical cases. It calculates theoretical efficiency using Rayleigh length diffraction as a benchmark to verify that optical losses are mathematically accurate.
