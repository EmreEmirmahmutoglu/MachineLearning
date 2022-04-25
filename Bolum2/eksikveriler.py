# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:11:22 2022

@author: EmreEmir
"""
#import-kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#kod bolumu
#veri yukleme- pd.read_csv("veriler.csv")
veriler = pd.read_csv("veriler.csv")

print(veriler)

#veri on isleme
boy = veriler[["boy"]]
print(boy)

boykilo=veriler[["boy","kilo"]]
print(boykilo)

#class
class insan:
    boy= 180
    def kosmak(self,b):
        return b+10

#object  
ali= insan()
print(ali.boy)
print(ali.kosmak(90))

l=[1,2,3] #liste
