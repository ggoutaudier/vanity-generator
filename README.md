# vanity-generator
This simple Python3 script generates a Bitcoin vanity key using this nice python library:
https://ofek.github.io/bit/

To use the script, first install the bit module using the instructions from the above link. You can then run the script by passing the "vanity" string that you want to include at the beginning of you bitcoin address, e.g.:
```
$ ./generate_vanity.py "AA"
Matching found!!!
Private Key: L2bAoowvLgcw8sDVZiB2bPN245FnsjQqn5cwVykV15M9qANJp2Yn
Address: 1AAJL8xwBNdDWi8Mm5uusgrwtCXb612S3S
```

Note that the execution time will increase exponentially with the length of the string you provide. 


