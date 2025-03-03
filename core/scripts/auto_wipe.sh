#!/bin/bash  
shred -vfzu /var/log/*.log  
history -c  
rm -rf ~/.bash_history  
