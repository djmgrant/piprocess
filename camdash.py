#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:31:41 2021

@author: Dave Grant 
"""
import subprocess
from flask import Flask , render_template, request 
app = Flask(__name__)
CamSoftware = 'motion'

def Systemctl(service, cmd):
    
    if cmd not in ('stop','start','status'):
        print('Command must be stop/start/status')
        return 1
    else:    
        if cmd == 'status':
            stat = subprocess.call(["systemctl", "is-active", "--quiet", service])
            if stat == 0:
                status = 'Running' 
            else: 
                status = 'Stopped'
        else:
            stat = subprocess.call(["sudo","systemctl", "--quiet", cmd, service])
            if stat == 0:
                status = cmd +' Command Executed'
            else: 
                status = cmd + ' Command Failed' 
        return status
                
                
def spoofSystemctl():
    return 0

def camstatus():
    status = 'Running' 
    return status

@app.route("/" , methods=['GET', 'POST'])
def seccam():
    
    if request.method == 'POST':
        status = Systemctl(CamSoftware,'status')
        command = request.form.get('action1')
        result = Systemctl(CamSoftware,command)
        return render_template('index.html', status=status , result=result)
        
    elif request.method == 'GET':
        status = Systemctl(CamSoftware,'status')
        return render_template('index.html', status=status )
    
    return render_template('index.html', result=result , status=status)

if __name__ == '__main__':
    app.run(debug=True)
