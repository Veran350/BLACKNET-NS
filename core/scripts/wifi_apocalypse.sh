#!/bin/bash  
echo "[+] Starting WiFi Apocalypse..."  
airmon-ng start wlan0  
airodump-ng wlan0mon  
