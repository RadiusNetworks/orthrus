# Orthrus
Bluetooth direction finding tools

![](img/orthrus.jpg)

## Summary
This repo contains python tools for interacting with the dialog semiconductior Angle-of-Arrival(AoA) and Time-of-Flight(ToF) development kits based on the DA1469x chipset.

## Requirements
- AoA development kit flashed with AoA Demo firmware From Dialog Semi. The kit contains a receiver board(DA1469x AoA antenna board + daughter board) and a transmitter USB dongle board
![](img/aoa_demo_kit.jpg)

- ToF development kit flashed with ToF Demo firmware From Dialog Semi. The kit contains a receiver board(DA1469x board + daughter board) and a transmitter USB dongle board
![](img/tof_demo_kit.jpg)

- python3
- pip3

## Getting Started with Demo Kits
To flash the demo boards, unzip the two firmware demo packages located in the [dialog-semi firmware](firmware/dialogSemi_aoa_tof_firmware) directory. Follow the instructions contain inside the packages to flash the kits with the appropriate binaries.


## Installation
1. Download zip or clone repo to your machine
2. Run `which python3` to check if python3 is installed. If a path to `python3` is returned, skip step 3
3. Run `brew install python3`
4. Run `pip3`. If `pip3` is not found, run `brew  update` to get latest version of pip3
5. From the project root directory, run `pip3 -r requirements.txt` to install dependencies

## Run AoA Demo
1. Connect AoA receiver board to your machine to establish serial communication
2. Connect the AoA transmitter dongle to your machine or any other USB host
3. Run `aoa.py -v`. You should see angle data being printed to the standard output

Note: It's important that the AoA transmitter USB dongle is connected to a USB host and not just a USB power supply

## Run ToF Demo
1. Connect ToF receiver board to your machine to establish serial communication
2. Connect the ToF transmitter dongle to your machine or any other USB host
3. Run `tof.py -v`. You should see the distance between Tx and Rx being printed to the standard output

Note: It's important that the ToF transmitter USB dongle is connected to a USB host and not just a USB power supply


