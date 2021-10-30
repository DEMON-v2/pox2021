#!/bin/bash

echo "[Challenge] Setup Virtaul CAN Device"

sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
