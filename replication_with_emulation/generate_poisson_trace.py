#!/usr/bin/env python

import argparse
import numpy as np
from os import path
from helpers import make_sure_path_exists
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bandwidth', metavar='Mbps', required=True,
                        help='rate of Poisson process (Mbps)')
    parser.add_argument('--output-dir', metavar='DIR', required=True,
                        help='directory to output trace')
    args = parser.parse_args()

    # trace path
    make_sure_path_exists(args.output_dir)
    trace_path = path.join(
        args.output_dir, '%smbps-poisson.trace' % args.bandwidth)

    lambd = 1e6 * max(1e-6, float(args.bandwidth)) / (8 * 1500)

    # write timestamps to trace
    ts = 0
    with open(trace_path, 'w') as trace:
        while ts < 60000:
            ts += 1000 * random.expovariate(lambd)
            trace.write('%d\n' % ts)


if __name__ == '__main__':
    main()