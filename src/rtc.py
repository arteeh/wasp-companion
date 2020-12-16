import argparse
import io
import random
import os.path
import pexpect
import time
import string
import sys

def handle_rtc(c):
    # Wait for the clock to tick over to the next second
    now = then = time.localtime()
    while now[5] == then[5]:
        now = time.localtime()

    # Set the time
    c.sendline(f'watch.rtc.set_localtime(({now[0]}, {now[1]}, {now[2]}, {now[3]}, {now[4]}, {now[5]}, {now[6]}, {now[7]}))')
    c.expect('>>> ')

def check_rtc(c):
    c.sendline('print(watch.rtc.get_localtime())')
    c.expect('\(([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+), ([0-9]+)\)')
    t = time.localtime()

    watch_hms = (int(c.match[4]), int(c.match[5]), int(c.match[6]))
    watch_str = f'{watch_hms[0]:02d}:{watch_hms[1]:02d}:{watch_hms[2]:02d}'
    host_hms = (t.tm_hour, t.tm_min, t.tm_sec)
    host_str = f'{host_hms[0]:02d}:{host_hms[1]:02d}:{host_hms[2]:02d}'
    delta = 3600 * (host_hms[0] - watch_hms[0]) + \
              60 * (host_hms[1] - watch_hms[1]) + \
                   (host_hms[2] - watch_hms[2])
    print(f"PC <-> watch:  {watch_str} <-> {host_str} (delta {delta})")

    c.expect('>>> ')
