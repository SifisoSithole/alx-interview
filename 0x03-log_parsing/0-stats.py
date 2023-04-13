#!/usr/bin/python3
"""
problem: Write a script that parses log files and computes metrics

input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""
import sys
import re


def print_stats(total_size: int, status_codes: dict):
    """
    prints the stats after 10 lines or a keyboard interruption
    args:
        total_size (int): is the sum of all previous file sizes
        status_code (dict): Dictionary with the status codes
    """
    print('File size:', total_size)
    for k, v in status_codes.items():
        if v != 0:
            print('{}: {}'.format(k, v))


pattern = r'''
    \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}     # IP address
    \s-\s\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d+\]\s  # Timestamp
    "GET\s/projects/260\sHTTP/1\.1"\s      # Request method and path
    (.{3})\s                              # HTTP status code
    (\d+)                                 # Response size
'''

regex = re.compile(pattern, re.VERBOSE)
counter = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
temp_status_codes = status_codes.copy()
total_size = 0
try:
    for line in sys.stdin:

        if not regex.fullmatch(line.strip()):
            continue
        line = line.split()
        total_size += int(line[-1])
        status_code = line[-2]
        if status_code in temp_status_codes.keys():
            temp_status_codes[status_code] += 1
        counter += 1
        if counter == 10:
            print_stats(total_size, temp_status_codes)
            counter = 0
            temp_status_codes = status_codes.copy()
finally:
    print_stats(total_size, temp_status_codes)
