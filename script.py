#!/bin/python3

import socket
import threading
from queue import Queue
import sys
import argparse

parser = argparse.ArgumentParser(description="Simple multithreaded port scanner")
parser.add_argument("ip", help="Target IP address")
group = parser.add_mutually_exclusive_group()
group.add_argument("-p", "--portrange", help="Port range, e.g. 20-80")
group.add_argument("-s", "--singleport", type=int, help="Single port to scan")
args = parser.parse_args()

target = args.ip
queue = Queue()
open_ports = []

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        sock.connect((target, port))
        sock.close()
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if scan_port(port):
            print(f'Port {port} is open!')
            open_ports.append(port)

if args.portrange:
    try:
        start, end = map(int, args.portrange.split('-'))
        port_list = range(start, end + 1)
    except:
        print("Invalid port range format. Use <start>-<end> (e.g. 20-80)")
        sys.exit(1)
elif args.singleport:
    port_list = [args.singleport]
else:
    port_list = range(1, 1024)

fill_queue(port_list)

thread_list = []
for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are:", open_ports)