#!/usr/bin/env python3

import sys
from bit import Key

vanity=sys.argv[1]

match_found = False
while not match_found:
  key = Key()
  if key.address.startswith("1"+vanity):
    print("Matching found!!!")
    print("Private Key:", key.to_wif())
    print("Address:", key.address)
    match_found = True

