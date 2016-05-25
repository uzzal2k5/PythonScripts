#!/usr/local/bin/python3.4
import subprocess
#
pid = subprocess.call(["ps -aux | grep httpd | grep -v grep | grep root | awk '{ print $2 }'"], shell=True)
