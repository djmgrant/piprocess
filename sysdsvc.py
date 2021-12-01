#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:31:41 2021

@author: Dave Grant 
"""
import subprocess
import os 
import sys

def Systemctl(service, cmd):
    
    if cmd not in ('stop','start','status'):
        print('Command must be stop/start/status')
        exit(1)
    else: 
        print('exec cmd',service, cmd)
        
        if cmd == 'status':
            stat = subprocess.call(["systemctl", "is-active", "--quiet", "ssh"])
            if(stat == 0):  # if 0 (active), print "Active"
                print("Active")
        else:
            command = 'service ' + service + ' ' + cmd 
    
if __name__ == '__main__':
    monitor = Systemctl(sys.argv[1],sys.argv[2])
