# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 12:11:22 2022

@author: EmreEmir
"""
#1.import-kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2.veri onisleme
#2.1veri yukleme
veriler = pd.read_csv("satislar.csv")
#pd.read_csv("eksikveriler.csv")

#test
print(veriler)

#veri on isleme
aylar = veriler[["Aylar"]]
#test
print(aylar)

satislar=veriler[["Satislar"]]
print(satislar)



#verileri egitim ve tes olarak ayırma
#ülke, boy, kilo ve yaşdan cinsiyet tahmin etme

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(aylar,satislar, test_size=0.33, random_state=0)

#verilerin olceklenmesi
#öznitelik ölçekleme
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#model insasi (linear regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,Y_train)















