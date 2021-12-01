#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:31:41 2021

@author: Dave Grant 
"""
import subprocess
import sys

def Systemctl(service, cmd):
    
    if cmd not in ('stop','start','status'):
        print('Command must be stop/start/status')
        exit(1)
    else:    
        if cmd == 'status':
            stat = subprocess.call(["systemctl", "is-active", "--quiet", service])
            if(stat == 0):  # if 0 (active), print "Active"
                print("Active")
        else:
            stat = subprocess.call(["sudo systemctl", "--quiet", cmd, service])
            if(stat == 0):  
                print("Success")
    
if __name__ == '__main__':
    monitor = Systemctl(sys.argv[1],sys.argv[2])
