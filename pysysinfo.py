#!/usr/local/bin/python3.4
# A System Information Gathering Script
import subprocess


# Command 1
def uname_func():
    uname = "uname"
    uname_arg = "-a"
    print ('Gathering system information with %s command:', uname)
    subprocess.call([uname, uname_arg])


# Command 2
def disk_func():
    diskspace = "df"
    diskspace_arg = "-h"
    print('Gathering diskspace information %s command:',diskspace)
    subprocess.call([diskspace, diskspace_arg])


# Command 3
def memory_func():
    mem = "free"
    mem_arg = "-h"
    print('Memory Information {0:s} Command: ',mem)
    subprocess.call([mem, mem_arg])


# lsblk - list block devices
def list_block():
    dev_list = "lsblk"
    print(" lsblk - list block devices", dev_list)
    subprocess.call(dev_list)

# Main function that call other functions
def main():
    # type: () -> object
    # type: () -> object
    uname_func()
    print
    disk_func()
    print
    memory_func()
    print
    list_block()


main()
