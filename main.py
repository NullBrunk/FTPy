#!/usr/bin/env python3

from time import strftime
from socket import socket
from sys import argv
from pwn import log


def main(ip: str, port: int):
    s = socket()
    s.connect((ip, port))


if __name__ == "__main__":
    log.info("Launching FTPy at " + strftime("%H:%M:%S"))
    if len(argv) == 1:
        log.info("Using default port 21 ...")
    else:
        argv[2] = 21
    main(argv[1], argv[2])
