#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
"""
start / stop / status system service 
"""
import subprocess
import sys


class SystemdService(object):
    '''A systemd service object with methods to check it's activity, and to stop() and start() it.'''

    def __init__(self, service):
        self.service = service


    def is_active(self):
        """Return True if systemd service is running"""
        try:
            cmd = '/bin/systemctl status {}.service'.format(self.service)
            completed = subprocess.run( cmd, shell=True, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            print( 'ERROR:', err )
        else:
            for line in completed.stdout.decode('utf-8').splitlines():
                if 'Active:' in line:
                    if '(running)' in line:
                        print('True')
                        return True
            return False


    def stop(self):
        ''' Stop systemd service.'''
        try:
            cmd = '/bin/systemctl stop {}.service'.format(self.service)
            completed = subprocess.run( cmd, shell=True, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            print( 'ERROR:', err )


    def start(self):
        ''' Start systemd service.'''
        try:
            cmd = '/bin/systemctl start {}.service'.format(self.service)
            completed = subprocess.run( cmd, shell=True, check=True, stdout=subprocess.PIPE )
        except subprocess.CalledProcessError as err:
            print( 'ERROR:', err )


if __name__ == '__main__':
  # monitor = SystemdService(sys.argv[1])
   monitor = SystemdService(sys.argv[1])
    monitor.is_active()
