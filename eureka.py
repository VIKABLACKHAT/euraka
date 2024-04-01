# -*- coding: utf-8 -*-
# !/usr/bin/python
# Target = to find 59000 ethereum stolen by hackers

import sha3
import os
from ethereum import utils
import time

start = time.time()

a = 1
while (a <= 3):

    elapsed_time = time.time() - start
    
    private_key = utils.sha3(os.urandom(256))
    raw_address = utils.privtoaddr(private_key)
    account_address =(utils.checksum_encode(raw_address)).lower()
    z=utils.encode_hex(private_key)
    #for test
    #account_address ="0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97"
    wanted = "0x4838B106FCe9647Bdf1E7877BF73cE8B0BAD5f97"
    
    if wanted == account_address:
       print("---EUREKA------EUREKA------EUREKA------EUREKA---")
       print("Private Key      : " + z)
       print("Address          : " + account_address)

       dosya2 = open("eslesme.txt","a")
       dosya2.write(z + " " + account_address + "\n")
       dosya2.close()

       time.sleep(5)
    else:
        print ('Private Key:', z + ' ' + 'Address: ' + account_address + ' '+ str(a))
    
    a = a + 1

print ("Total Time %s sn" % elapsed_time)