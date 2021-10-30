#!/bin/bash

echo "[Challenge] Setup Virtaul CAN Device"

sudo apt install can-utils -y

sleep 3

if mkdir ./utils ; then
	echo "[Challenge] Create Utils Directory"
fi

cp /usr/bin/cansniffer ./utils
cp /usr/bin/candump ./utils
cp /usr/bin/cansend ./utils
cp /usr/bin/canplayer ./utils

sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0