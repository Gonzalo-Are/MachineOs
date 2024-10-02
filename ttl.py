#!/usr/bin/env python3

import subprocess,sys

ip = sys.argv[1]

command = f"ping -c 1 {ip} | head -n 2 | tail -n 1 | cut -d' ' -f6 | tr '=' ' ' | cut -d' ' -f2"


print()

a = subprocess.Popen(f'{command}', shell=True)
a.communicate()

print()

print("Linux - > 64")
print()
print("Windows -> 128")