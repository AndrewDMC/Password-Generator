import random
import tkinter as tk

def PasswordGenerator(UC,LC,SC,NC):
    UpperCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
    LowerCase = UpperCase.lower()
    Symbol = "!@#$%^&*()-_=+,-./:;<=>?@|\>"
    Number = "1234567890"
    Password = ""

    UpperCase_Check, LowerCase_Check, Symbol_Check, Number_Check = UC, LC, SC, NC

    PasswordLenght = 69
    PasswordNumber = 1

    AllChoice = ""

    if UpperCase_Check:
        AllChoice += UpperCase
    if LowerCase_Check:
        AllChoice += LowerCase
    if Symbol_Check:
        AllChoice += Symbol
    if Number_Check:
        AllChoice += Number



    for i in range(PasswordNumber):
        Password = "".join(random.sample(AllChoice, PasswordLenght))
        print(Password)