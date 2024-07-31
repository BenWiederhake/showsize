#!/usr/bin/env python3

import os


PREFIXES = " Ki Mi Gi Ti Pi Ei".split(" ")


def human_readable(size_bytes):
    power = 0
    if size_bytes >= 1024:  # KiB
        size_bytes /= 1024
        power += 1
    if size_bytes >= 1024:  # MiB
        size_bytes /= 1024
        power += 1
    if size_bytes >= 1024:  # GiB
        size_bytes /= 1024
        power += 1
    if size_bytes >= 1024:  # TiB
        size_bytes /= 1024
        power += 1
    if size_bytes >= 1024:  # PiB
        size_bytes /= 1024
        power += 1
    if size_bytes >= 1024:  # EiB
        size_bytes /= 1024
        power += 1
    return str(size_bytes) + " " + PREFIXES[power] + "B"


def run(filename):
    if not os.path.exists(filename):
        print(filename + " does not exist!")
    else:
        size_bytes = os.stat(filename)
        size_human = human_readable(size_bytes)
        print(filename + ": " + size_human)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("USAGE: ./showsize.py FILENAME", file=sys.stderr)
