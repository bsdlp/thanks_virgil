#!/usr/bin/env python2

import argparse

def parse():
    parser = argparse.ArgumentParser(description='thanks_virgil')
    parser.add_argument('--ssh-pubkey', action='store')
    return parser

if __name__ == '__main__':
    args = parse()
