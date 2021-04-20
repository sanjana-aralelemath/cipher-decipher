#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import *
import tkinter.font
import math

root=tk.Tk()
root.geometry("300x500")
root.title("CRYPTZee")

variable=tk.StringVar(root)


#first page
def first():
    frame1=tk.Frame(root, bg="black")
    frame1.place(relwidth=1, relheight=1)
    julius=tk.Button(frame1, text="Caeser code", height=5, width=30, fg="black", bg="light green", font=50, command=caeser)
    julius.place(relx=0.15, rely=0.1)
    morse1=tk.Button(frame1, text="Morse code", height=5, width=30, fg="black", bg="light green", font=50, command=morse)
    morse1.place(relx=0.6, rely=0.1 )
    rev=tk.Button(frame1, text="Reverse", height=5, width=30, fg="black", bg="light green", font=50, command=reverse_dec)
    rev.place(relx=0.15, rely=0.7)
    transposition1=tk.Button(frame1, text="Vertical Transposition code", height=5, width=30, fg="black", bg="light green", font=50, command=transposition)
    transposition1.place(relx=0.6, rely=0.7)
    

    
#caeser page
def caeser(): 
    frame2=tk.Frame(root, bg="black")
    frame2.place(relwidth=1, relheight=1)
    keys=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    variable.set("With key")
    keydrop=tk.OptionMenu(frame2, variable, *keys)
    keydrop.config(height=5, width=37, font=40)
    keydrop.place(relx=0.35, rely=0.1)
    keypage=tk.Button(frame2, text="Decipher/Cipher", height=3, width=20, fg="black", bg="light green", font=30, command=keyfn)
    keypage.place(relx=0.7, rely=0.12)
    rot=tk.Button(frame2, text="Rot 13", height=5, width=40, fg="black", font=40, command=rot13)
    rot.place(relx=0.35, rely=0.32)
    nokey=tk.Button(frame2, text="Without key", height=5, width=40, fg="black", font=40, command=caes_no_key)
    nokey.place(relx=0.35, rely=0.55)
    back2=tk.Button(frame2, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=first)
    back2.place(relx=0.5, rely=0.92, anchor='s')
    


#key given
def keyfn():
    key=int(variable.get())
    frame3=tk.Frame(root, bg="black")
    frame3.place(relwidth=1, relheight=1)
    key_label=tk.Label(height=2, width=20, text="Code", font=20)
    key_label.place(relx=0.01, rely=0.05)
    enter_code=tk.Entry(width=120, font=20)
    enter_code.place(relx=0.05, rely=0.2)
    dec_label=tk.Label(height=2, width=20, text="Message", font=20)
    dec_label.place(relx=0.01, rely=0.4)
    dec_code=tk.Entry(width=120, font=20)
    dec_code.place(relx=0.05, rely=0.55)
    def dec_caes_key():
        code_txt=enter_code.get()
        dec_txt=''
        for char in code_txt: 
            if  char.isupper():
                dec_txt=dec_txt+chr((ord(char)-key-65)%26+65)
            elif char.islower():
                dec_txt=dec_txt+chr((ord(char)-key-97)%26+97)
            else:
                dec_txt=dec_txt+char
        dec_code.insert(0,dec_txt)
    def cip_msg_key():
        msg_txt=dec_code.get()
        cip_txt=''
        for char in msg_txt: 
            if  char.isupper():
                cip_txt=cip_txt+chr((ord(char)+key-65)%26+65)
            elif char.islower():
                cip_txt=cip_txt+chr((ord(char)+key-97)%26+97)
            else:
                cip_txt=cip_txt+char
        enter_code.insert(0,cip_txt)
        
    dec=tk.Button(frame3, text="Decipher code", height=2, width=15, bg="light blue", font= 20, command=dec_caes_key)
    dec.place(relx=0.45, rely=0.30)
    cip=tk.Button(frame3, text="Cipher message", height=2, width=15, bg="light blue", font= 20, command=cip_msg_key)
    cip.place(relx=0.45, rely=0.65)
    back3=tk.Button(frame3, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=caeser)
    back3.place(relx=0.4, rely=0.80)
    
    
#reverse caeser
def reverse_dec():
    frame4=tk.Frame(root, bg="black")
    frame4.place(relwidth=1, relheight=1)
    rev_label=tk.Label(height=2, width=20, text="Code/Message", font=20)
    rev_label.place(relx=0.01, rely=0.05)
    enter_code1=tk.Entry(width=120, font=20)
    enter_code1.place(relx=0.05, rely=0.2)
    msg_label=tk.Label(height=2, width=20, text="Reversed code/message", font=20)
    msg_label.place(relx=0.01, rely=0.5)
    rev_code=tk.Entry(width=120, font=20)
    rev_code.place(relx=0.05, rely=0.65)
    def rev_dec():
        rev_text=enter_code1.get()
        rev_str=rev_text[::-1]
        rev_code.insert(0,rev_str)
    dec1=tk.Button(frame4, text="Reverse", height=2, width=15, bg="light blue", font= 20, command=rev_dec)
    dec1.place(relx=0.45, rely=0.30)
    back4=tk.Button(frame4, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=first)
    back4.place(relx=0.4, rely=0.80)
    
    
#caeser without key
def caes_no_key():
    frame5=tk.Frame(root, bg="black")
    frame5.place(relwidth=1, relheight=1)
    no_key_label=tk.Label(height=3, width=40, text="Code", font=20)
    no_key_label.place(relx=0.01, rely=0.05)
    entercode1=tk.Entry(width=120, font=20)
    entercode1.place(relx=0.05, rely=0.15)
    def no_key():
        text=Text(frame5, height=26, width=160)
        text.place(relx=0.05, rely=0.3)
        nokey_code=entercode1.get()
        for key1 in range(26):
            msg=''
            codetxt=entercode1.get()
            dectxt=''
            for char in codetxt: 
                if  char.isupper():
                    dectxt=dectxt+chr((ord(char)-key1-65)%26+65)
                elif char.islower():
                    dectxt=dectxt+chr((ord(char)-key1-97)%26+97)
                else:
                    dectxt=dectxt+char
            text.insert(INSERT,f"{key1}\t{dectxt}\n")
    decr1=tk.Button(frame5, text="Decipher", height=2, width=15, bg="light blue", font= 20, command=no_key)
    decr1.place(relx=0.45, rely=0.20)
    back5=tk.Button(frame5, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=caeser)
    back5.place(relx=0.4, rely=0.85)
    
    
#rot13
def rot13():
    key=13
    frame6=tk.Frame(root, bg="black")
    frame6.place(relwidth=1, relheight=1)
    rot_label=tk.Label(height=2, width=20, text="Code", font=20)
    rot_label.place(relx=0.01, rely=0.05)
    enter_code1=tk.Entry(width=120, font=20)
    enter_code1.place(relx=0.05, rely=0.2)
    dec_label1=tk.Label(height=2, width=20, text="Message", font=20)
    dec_label1.place(relx=0.01, rely=0.4)
    dec_code1=tk.Entry(width=120, font=20)
    dec_code1.place(relx=0.05, rely=0.55)
    def dec_rot():
        code_txt1=enter_code1.get()
        dec_txt1=''
        for char in code_txt1: 
            if  char.isupper():
                dec_txt1=dec_txt1+chr((ord(char)-key-65)%26+65)
            elif char.islower():
                dec_txt1=dec_txt1+chr((ord(char)-key-97)%26+97)
            else:
                dec_txt1=dec_txt1+char
        dec_code1.insert(0,dec_txt1)
    def cip_rot():
        msg_txt1=dec_code1.get()
        cip_txt1=''
        for char in msg_txt1: 
            if  char.isupper():
                cip_txt1=cip_txt1+chr((ord(char)+key-65)%26+65)
            elif char.islower():
                cip_txt1=cip_txt1+chr((ord(char)+key-97)%26+97)
            else:
                cip_txt1=cip_txt1+char
        enter_code1.insert(0,cip_txt1)
    dec2=tk.Button(frame6, text="Decipher code", height=2, width=15, bg="light blue", font= 20, command=dec_rot)
    dec2.place(relx=0.45, rely=0.30)
    cip2=tk.Button(frame6, text="Cipher message", height=2, width=15, bg="light blue", font= 20, command=cip_rot)
    cip2.place(relx=0.45, rely=0.65)
    back7=tk.Button(frame6, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=caeser)
    back7.place(relx=0.4, rely=0.80)
    
    
#transposition vertical
def transposition():
    frame7=tk.Frame(root, bg="black")
    frame7.place(relwidth=1, relheight=1)
    keys=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    variable.set("Key")
    keydrop=tk.OptionMenu(frame7, variable, *keys)
    keydrop.config(height=2, width=20, font=20)
    keydrop.place(relx=0.45, rely=0.02)
    code_label=tk.Label(height=2, width=20, text="Code", font=20)
    code_label.place(relx=0.01, rely=0.15)
    enter_code1=tk.Entry(width=120, font=20)
    enter_code1.place(relx=0.05, rely=0.25)
    dec_label1=tk.Label(height=2, width=20, text="Message", font=20)
    dec_label1.place(relx=0.01, rely=0.45)
    dec_code1=tk.Entry(width=120, font=20)
    dec_code1.place(relx=0.05, rely=0.55)
    def tran_dec():
        key=int(variable.get())
        msg=''
        code=enter_code1.get()
        key1=math.ceil(len(code)/key)
        for i in range(0,key1):
            for j in range(i,len(code),key1):
                msg=msg+code[j]
        dec_code1.insert(0,msg)  
    def tran_cip():
        key=int(variable.get())
        code1=''
        message=dec_code1.get()
        key1=math.ceil(len(message)/key)
        for i in range(0,key):
            codebit=''
            for j in range(i,len(message),key):
                codebit=codebit+message[j]
            while len(codebit)<key1:
                codebit=codebit+' '
            code1=code1+codebit
        enter_code1.insert(0,code1)
    
    dec2=tk.Button(frame7, text="Decipher code", height=2, width=15, bg="light blue", font= 20, command=tran_dec)
    dec2.place(relx=0.45, rely=0.30)
    cip2=tk.Button(frame7, text="Cipher message", height=2, width=15, bg="light blue", font= 20,command=tran_cip)
    cip2.place(relx=0.45, rely=0.6)
    back7=tk.Button(frame7, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=first)
    back7.place(relx=0.4, rely=0.80)
    
    

#morse    
def morse():
    frame8=tk.Frame(root, bg="black")
    frame8.place(relwidth=1, relheight=1)
    code_label=tk.Label(height=2, width=40, text="Code in '.' and '-' only. '_' between symbols", font=20)
    code_label.place(relx=0.01, rely=0.1)
    enter_code1=tk.Entry(width=120, font=20)
    enter_code1.place(relx=0.05, rely=0.22)
    dec_label1=tk.Label(height=2, width=40, text="Message - letters and numbers only", font=20)
    dec_label1.place(relx=0.01, rely=0.4)
    dec_code1=tk.Entry(width=120, font=20)
    dec_code1.place(relx=0.05, rely=0.52)
    morse_code={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----','A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}
    morse_keys=list(morse_code.keys())
    morse_values=list(morse_code.values())
    def decipher_morse():
        code=enter_code1.get()+'_'
        msg=''
        codebit=''
        symbols=(str(code.split(' '))).split('_')
        for i in code:
            if i==' ':
                if codebit in morse_values:
                    pos=morse_values.index(codebit)
                    msg=msg+morse_keys[pos]
                    codebit=''
                    msg=msg+' '
                else:
                    msg=msg+'?'
            elif i=='_':
                if codebit in morse_values:
                    pos=morse_values.index(codebit)
                    msg=msg+morse_keys[pos]
                    codebit=''
                else:
                    msg=msg+'?'
            else:
                if i=='.' or i=='-':
                    codebit=codebit+i
                else:
                    msg=msg+'*'
        dec_code1.insert(0,msg)
    def cipher_morse():
        message=dec_code1.get()
        cd=''
        msg1=message+'+'
        n=0
        for i in message:
            if i==' ':
                cd=cd+' '
            else:
                if msg1[n+1]==' ':
                    cd=cd+morse_code.get(i,'?')
                else:
                    cd=cd+morse_code.get(i,'?')+'_'
            if n<len(message):
                n=n+1
        cd=cd[:len(cd)-1]
        enter_code1.insert(0,cd)
        
    dec2=tk.Button(frame8, text="Decipher code", height=2, width=15, bg="light blue", font= 20, command=decipher_morse)
    dec2.place(relx=0.45, rely=0.30)
    cip2=tk.Button(frame8, text="Cipher message", height=2, width=15, bg="light blue", font= 20, command=cipher_morse)
    cip2.place(relx=0.45, rely=0.6)
    back7=tk.Button(frame8, text="Back", height=3, width=30, fg="white", bg="red", font=40, command=first)
    back7.place(relx=0.4, rely=0.80)
    



    
    
    
first()

root.mainloop()
    


# In[ ]:




