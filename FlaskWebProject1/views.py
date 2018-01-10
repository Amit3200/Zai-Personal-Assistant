"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
import sys
import os
import pyaudio
import speech_recognition as sr
import _tkinter
from tkinter import *
import random
import platform
import psutil
import pygame
import pygame.camera
from twilio.rest import Client
import time
import pickle
import webbrowser as wb
import subprocess
gojo=0
tempo=0
nametext=""
dobtext=""
tagtext=""
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
#home page######################################################################################################################################
################################################################################################################################################
################################################################################################################################################
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )
#contact page######################################################################################################################################
#################################################################################################################################################
################################################################################################################################################
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
#about page######################################################################################################################################
################################################################################################################################################
################################################################################################################################################
@app.route('/intro')
def intro():
        print("Hello")
        try:
            def saveas():
                f = open("Data.txt", "w+")
                t = text.get("1.0", "end-1c")
                # x=input("Enter the name : ")
                y = "Hello, " + t + "! Nice to Meet You."
                y += "I am Amit's personal assissant speaking to you developed by him."
                f.write(y)
                f.close()


            def readcreate():
                f = open("Data.txt", "r")
                v = open("speax.vbs", "w")
                z = f.read()
                k = "Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak " + '"' + z + '"'
                v.write(k)
                v.close()
                f.close()


            def speak():
                os.system("speax.vbs")
        except:
            pass

        root=Tk("Text Editor")
        text=Text(root,height=10,width=40,bg="#0E161E",fg="#fff",font="Anton")
        text.grid(row=0)
        button=Button(root, text="Save", command=saveas,height=1,width=7,font="Anton",bg="#263C52",fg="#fff")
        button.grid(row=0,column=1)
        button=Button(root, text="Create", command=readcreate,height=1,width=7,font="Anton",bg="#263C52",fg="#fff")
        button.grid(row=0,column=2) 
        button=Button(root, text="Speak", command=speak,height=1,width=7,font="Anton",bg="#263C52",fg="#fff")
        button.grid(row=0,column=3) 
        root.mainloop()
        return "Nice to Meet You"



#talk###########################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#talk###########################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#talk###########################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#talk###########################################################################################################################################
################################################################################################################################################
################################################################################################################################################

@app.route('/talkload')
def talkload():
     return render_template(
     'Sample.html',calculated="NA")

@app.route('/talk')
def talk():
    k=str(psutil.virtual_memory())
    ramdetails=(k[6:len(k)].split(','))
    totalram=ramdetails[0]
    totalram=int(totalram[6:])
    totalram=round(totalram//(1024*1024*1000))
    totalram=str(totalram)
    msg="Hi , Zaii is listening"
    f=open("msg.vbs","w+")
    k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
    f.write(k)
    f.close()
    os.system("msg.vbs")
    while(True):
        
        print("Inside Loop")
        t=0
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print((r.energy_threshold))
            print("Listening Status : ")
            audio=r.listen(source)
        print(audio)
       

        #mathlist+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        
        try:
                mathslist=["calculation","calculate","solve","evaluate","maths","math"]
                talklist=["tell me about yourself","who are you","who r u","tell me something about yourself","introduce","introduce yourself","intro","give intro"]
                testcontent=["how are you","who made you","why do you exist"]
                smslist=["sms","message","send text","send","text","chat","message me","remind me through text"]
                exitlist=["exit","terminate","close","collapse"]
                searchlist=["curious","search","interested","i would like to know about","know about","know","Tell me about","Tell"]
                text1 = r.recognize_google(audio)
                print("You said: " + text1)
                msg="You said: " + text1
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                #tts=gTTS(text=text1,lang='en')
                #tts.save("Record.mp3")
                #os.system("Record.mp3")
                speechsaid=text1.lower().split()
                print(speechsaid)
                to=0
                for i in exitlist:
                    if i in speechsaid:
                                msg="Zai is exiting"
                                f=open("Speech1.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("Speech1.vbs")
                                to=1
                                return render_template(
                                'index.html',
                                title='Home Page',
                                year=datetime.now().year,
                                ) 
                                break
                if to==1:
                    break
                    return render_template(
                    'index.html',
                    title='Home Page',
                    year=datetime.now().year,
                    ) 
                try:
                        for i in mathslist:
                                if i in speechsaid:
                                    t=1
                                    print("Yes")
                                    break
                        if t==1:
                                mathmsg="Hi , I will help you with Maths Calculation"
                                f=open("MathSpeech.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+mathmsg+'"'
                                f.write(k)
                                f.close()
                                os.system("MathSpeech.vbs")
                                print("Give Expression : ")
                                r1=sr.Recognizer()
                                with sr.Microphone() as source:
                                    r1.adjust_for_ambient_noise(source)
                                    print(r1.energy_threshold)
                                    audio=r1.listen(source)
                                print(audio)
                                try:
                                    text2 = r1.recognize_google(audio)
                                    if "multiplied" in text2:
                                            text2=text2.replace("multiplied","*")
                                            print("Detected")
                                    if "multiplied by" in text2:
                                            text2=text2.replace("multiplied by","*")
                                    if "x" in text2:
                                            text2=text2.replace("x","*")
                                    if "Multiplied" in text2:
                                            text2=text2.replace("multiplied","*")
                                    if "Multiplied by" in text2:
                                            text2=text2.replace("multiplied by","*")
                                    if "multiply" in text2:
                                            text2=text2.replace("multiply","*")
                                    if "multiply by" in text2:
                                            text2=text2.replace("multiply by","*")
                                    print("Expression said : "+text2)
                                    f=open("MathResult.vbs","w+")
                                    result="Evaluated Result is : "+str(eval(text2))
                                    k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+result+'"'
                                    f.write(k)
                                    f.close()
                                    print("Evaluated Result : "+str(eval(text2)))
                                    k=str(eval(text2))
                                    os.system("MathResult.vbs")
                                    return render_template(
                                    'Sample.html',calculated=k)
                                except sr.UnknownValueError:
                                        print("Google Speech Recognition could not understand audio")
                             
                                except sr.RequestError as e:
                                        print("Could not request results from Google  Speech Recognition service; {0}".format(e))
                                
                except:
                        pass

                #wordlist+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                
                try:
                        for i in talklist:
                                if i in text1:
                                    t=2
                                    print("Yes")
                                    break
                        if t==2:
                                wordmsg="I am ToughX version 1.0. I am a basic python build assistant. I can run on any machine which supports python 3.6."
                                wordmsg+="Currently My Platform Machine is "+platform.machine()+" . "
                                wordmsg+="My Platform System is "+platform.system()+" . "
                                wordmsg+="Platform Processor is "+platform.processor()+" . "
                                wordmsg+="Current RAM Memory  "+totalram+" GigaBytes . "
                                f=open("IntroSpeech.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+wordmsg+'"'
                                f.write(k)
                                f.close()
                                os.system("IntroSpeech.vbs")

                except:
                        pass

#smslist++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                try:
                        for i in smslist:
                                if i in text1:
                                    t=4
                                    print("Yes")
                                    break
                        if t==4:
                            smsmsg="Okay! I get that. You want to send the message. Remember Currently Message can be sent to the Amit only."
                            f=open("SMSSpeech.vbs","w+")
                            k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+smsmsg+'"'
                            f.write(k)
                            f.close()
                            os.system("SMSSpeech.vbs")
                            print("Speak Message")
                            smsmsg="Speak Message"
                            f=open("SMSSpeech.vbs","w+")
                            k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+smsmsg+'"'
                            f.write(k)
                            f.close()
                            os.system("SMSSpeech.vbs")
                            r1=sr.Recognizer()
                            with sr.Microphone() as source:
                                    r1.adjust_for_ambient_noise(source)
                                    print(r1.energy_threshold)
                                    audio=r1.listen(source)
                            print(audio)
                            try:
                                    text3 = r1.recognize_google(audio)
                                    save="You Said "+text3
                                    f=open("ConSpeech.vbs","w+")
                                    k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+save+'"'
                                    f.close()
                                    os.system("ConSpeech.vbs")
                            except sr.UnknownValueError:
                                        print("Google Speech Recognition could not understand audio")
                             
                            except sr.RequestError as e:
                                        print("Could not request results from Google  Speech Recognition service; {0}".format(e))
                            account_sid = "AC5adda6db593a0f369a427283c8436959"
                            auth_token = "fc647306d1cd37646ac0f1f23c55e612"
                            client = Client(account_sid, auth_token)
                            client.api.account.messages.create(
                            to="+13153538299",
                            from_="+13153229683",
                            body=text3)
                            smsmsg="Message Sent Successfully"
                            f=open("SMSSpeech.vbs","w+")
                            k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+smsmsg+'"'
                            f.write(k)
                            f.close()
                            os.system("SMSSpeech.vbs")
                except:
                        pass


                try:
                    for i in searchlist:
                           if i in text1:
                                msg="What would you like to know about ?"
                                f=open("Speechb.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("Speechb.vbs")
                                print("HEllo")
                                r=sr.Recognizer()
                                with sr.Microphone() as source:
                                    r.adjust_for_ambient_noise(source)
                                    print((r.energy_threshold))
                                    print("Listening Status : ")
                                    audio=r.listen(source)
                                print(audio)
                                t=5
                                try:
                                    text3 = r.recognize_google(audio)
                                except:
                                    pass
                    if t==5:
                        msg="Searching for result , Opening Browser"
                        f=open("Speechb.vbs","w+")
                        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                        f.write(k)
                        f.close()
                        os.system("Speechb.vbs")
                        wb.open_new_tab(text3)
                        print("Done")
                except:
                    pass
                        



                try:
                    for i in testcontent:
                        if i in text1:
                            if i == "how are you":
                                msg="Hello! I am Fine Thanks for asking!"
                                f=open("Speech2.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("Speech2.vbs")
                            elif i == "who made you":
                                msg="I am made by ToughX team!"
                                f=open("Speech2.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("Speech2.vbs")
                            elif i == "why do you exist":
                                msg="I am here to help you and have fun with you all! but remember i am currently in developing mode"
                                f=open("Speech2.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("Speech2.vbs")
                except:
                    pass
        except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
             
        except sr.RequestError as e:
                print("Could not request results from Google  Speech Recognition service; {0}".format(e))







#zai pack#######################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#zai pack#######################################################################################################################################
################################################################################################################################################
################################################################################################################################################
#zai pack#######################################################################################################################################
################################################################################################################################################
################################################################################################################################################



@app.route('/zaiintro')
def zaiintro():
    return render_template('Records_Signin.html')



@app.route('/zaipack')
def zaipack():
        msg="Hi , Zai Pack is listening"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        t=0
        msg="Please Enter your username"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        r4=sr.Recognizer()
        with sr.Microphone() as source:
            r4.adjust_for_ambient_noise(source)
            print(r4.energy_threshold)
            print("Listening Status : ")
            audio=r4.listen(source)
        print(audio)
        try:
            text1 = r4.recognize_google(audio)
            msg="You said: " + text1
            f=open("msg.vbs","w+")
            k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
            f.write(k)
            f.close()
            os.system("msg.vbs")
            speechsaid=text1.lower().split()
            print(speechsaid)
            msg="Zai Pack's Username is "+text1
            f=open("msg.vbs","w+")
            k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
            f.write(k)
            f.close()
            os.system("msg.vbs")
            print("You said: " + text1)
            t=1
            try:
                            if t==1:
                                    zmsg="Please provide OTP sent to your phone"
                                    f=open("ZaiSpeech.vbs","w+")
                                    k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+zmsg+'"'
                                    f.write(k)
                                    f.close()
                                    os.system("ZaiSpeech.vbs")
                                    print("Give Expression : ")
                                    randomnumber=random.randint(13241,50000)
                                    account_sid = "AC5adda6db593a0f369a427283c8436959"
                                    auth_token = "fc647306d1cd37646ac0f1f23c55e612"
                                    client = Client(account_sid, auth_token)
                                    client.api.account.messages.create(
                                    to="+13153538299",
                                    from_="+13153229683",
                                    body=randomnumber)
                                    print("Message Sent")
                                    smsmsg="Message Sent Successfully"
                                    f=open("SMSSpeech.vbs","w+")
                                    k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+smsmsg+'"'
                                    f.write(k)
                                    f.close()
                                    os.system("SMSSpeech.vbs")
                                    return render_template('LoginUp.html',username=text1,otp=randomnumber)       
            except:
                pass
                                    
        except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
             
        except sr.RequestError as e:
                print("Could not request results from Google  Speech Recognition service; {0}".format(e))
        except:
            print("Error Found")

#Registration###################################################################################################################################
#Registration###################################################################################################################################
#Registration###################################################################################################################################
#Registration###################################################################################################################################
#Registration###################################################################################################################################
#Registration###################################################################################################################################
#Registration###################################################################################################################################
#Registration###################################################################################################################################

@app.route('/zaiireg')
def zaiireg():
    return render_template('Registration.html')

@app.route('/registation')
def registration():
    global tempo
    if tempo==0:
        text110=""
        text2=""
        text3=""
        text4=""
        msg="Hi , Zai Pack is listening"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        msg="Please tell Username"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        t=0
        r4=sr.Recognizer()
        with sr.Microphone() as source:
            r4.adjust_for_ambient_noise(source)
            print(r4.energy_threshold)
            print("Listening Status : ")
            audio=r4.listen(source)
        print(audio)
        try:
                text110 = r4.recognize_google(audio)
                print(text110)
                msg="You said: " + text110
                print("Hello")
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                speechsaid=text110.lower().split()
                print(speechsaid)
                msg="Zai Pack's Username is "+text110
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                print("You said: " + text110)      
        except:
            pass
        msg="Please tell Name"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        t=0
        r4=sr.Recognizer()
        with sr.Microphone() as source:
            r4.adjust_for_ambient_noise(source)
            print(r4.energy_threshold)
            print("Listening Status : ")
            audio=r4.listen(source)
        print(audio)
        try:
                text2 = r4.recognize_google(audio)
                msg="You said: " + text2
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                speechsaid=text2.lower().split()
                print(speechsaid)
                msg="Zai Pack's Name is "+text2
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                print("You said: " + text2)
        except:
            pass
        msg="Please tell Date of Birth"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        t=0
        r4=sr.Recognizer()
        with sr.Microphone() as source:
            r4.adjust_for_ambient_noise(source)
            print(r4.energy_threshold)
            print("Listening Status : ")
            audio=r4.listen(source)
        print(audio)
        try:
                text3 = r4.recognize_google(audio)
                print(text3)
                msg="You said: " + text3
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                speechsaid=text3.lower().split()
                print(speechsaid)
                msg="Zai Pack's Date of Birth is "+text3
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                print("You said: " + text3)
        except:
            pass
        msg="Please tell Punchline of yours"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        t=0
        r4=sr.Recognizer()
        with sr.Microphone() as source:
            r4.adjust_for_ambient_noise(source)
            print(r4.energy_threshold)
            print("Listening Status : ")
            audio=r4.listen(source)
        print(audio)
        try:
                text4 = r4.recognize_google(audio)
                print(text4)
                print(text4)
                print("Hello")
                msg="You said: " + text4
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                speechsaid=text4.lower().split()
                print(speechsaid)
                msg="Your Zai Pack's Punch line is "+text4
                f=open("msg.vbs","w+")
                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                f.write(k)
                f.close()
                os.system("msg.vbs")
                print("You said: " + text4)                                 
        except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
             
        except sr.RequestError as e:
                    print("Could not request results from Google  Speech Recognition service; {0}".format(e))
        except:
                print("Error Found")
        msg="Thanks for Registration Just go through credentials and please enter OTP sent to the mobile"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        randomnumber=random.randint(13241,50000)
        account_sid = "AC5adda6db593a0f369a427283c8436959"
        auth_token = "fc647306d1cd37646ac0f1f23c55e612"
        client = Client(account_sid, auth_token)
        client.api.account.messages.create(
        to="+13153538299",
        from_="+13153229683",
        body=randomnumber)
        print("Message Sent")
        smsmsg="Message Sent Successfully"
        f=open("SMSSpeech.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+smsmsg+'"'
        f.write(k)
        f.close()
        os.system("SMSSpeech.vbs")
        try:
            tempdata=[]
            fin=open("Userdata.txt","rb")
            fdata=pickle.load(fin)
            print(fdata)
            for i in range(1,len(fdata)):
                print(fdata[i])
                for j in range(len(fdata[i])):
                    print(fdata[i][j])
                    tempdata.append(fdata[i][0])
            print(tempdata)
            fin.close()
        except:
            print("Error Found")
            pass
        try:
            fin=open("Userdata.txt","ab")
            if text110 in tempdata:
                print("Cannot be saved")
            else:
                pickle.dump([[text110,text2,text3,text4]],fin)
                print([["'"+text110+"'","'"+text2+"'","'"+text3+"'","'"+text4+"'"]])
                print("Write Done")
                tempfileuser=open("Tempuser.txt","w")
                tempfileuser.write(text11)
                tempfileuser.close();
            fin.close()
        except:
            pass
        tempo+=1
        global gojo
        global nametext
        global dobtext
        global tagtext
        nametext = text2
        dobtext= text3
        tagtext = text4
        print(nametext,dobtext,tagtext)
        return render_template('Registration.html',username=text110,name=text2,dob=text3,tagline=text4,otp=randomnumber)   
    elif tempo>0:
        print("Logining in")
        if gojo==0:
            gojo+=1
            return render_template('Social.html',name=nametext,tagline=tagtext,dob=dobtext,numberlikes1=0,numberlikes2=0)   
        else:
            social()




#Profile Work #####################################################################################################################################
#Profile Work #####################################################################################################################################
#Profile Work #####################################################################################################################################
#Profile Work #####################################################################################################################################
#Profile Work #####################################################################################################################################
#Profile Work #####################################################################################################################################
#Profile Work #####################################################################################################################################
number=0
@app.route('/FurtherSocial')
def social():
    fun=["like"]
    global number
    while(True):
        r4=sr.Recognizer()
        with sr.Microphone() as source:
             r4.adjust_for_ambient_noise(source)
             print(r4.energy_threshold)
             print("Listening Status : ")
             audio=r4.listen(source)
        print(audio)
        try:
           text4 = r4.recognize_google(audio)
           print(text4)
        except:
            print("Error")
            pass
        for i in fun:
            if i in text4:
                number+=1
        return render_template('Social.html',numberlikes1=number)


@app.route('/Notes1')
def notesz():
    return render_template('Notes.html')


@app.route('/Notes')
def notes1():
        text4=""
        text5=""
        msg="Listening to the lecture! Don't Worry I will mark down the imporatant part for you and will send it to you"
        f=open("msg.vbs","w+")
        k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
        f.write(k)
        f.close()
        os.system("msg.vbs")
        print("Inside Login Loop")
        listenlist=["important","very important","essential","must study"]
        while(True):
            r=sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print(r.energy_threshold)
                print("Listening Status : ")
                audio=r.listen(source)
            print(audio)
            try:
                text4 = r.recognize_google(audio)
                speechset=text4.split()
                print(text4)
            except:
                pass
            if (text4=="terminate"):
                                msg="Terminating"
                                f=open("msg.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("msg.vbs")
                                return render_template('layout.html')  
            else:
                for i in listenlist:
                    if i in speechset:
                                r4=sr.Recognizer()
                                with sr.Microphone() as source:
                                                r4.adjust_for_ambient_noise(source)
                                                print(r4.energy_threshold)
                                                print("Listening Status 23 : ")
                                                audio=r4.listen(source)
                                print(audio)
                                try:
                                               text5 = r4.recognize_google(audio)
                                               print(text5)
                                except:
                                                pass
                                 
                                msg="Marking down the important notes and sending it to your phone"
                                f=open("msg.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+msg+'"'
                                f.write(k)
                                f.close()
                                os.system("msg.vbs")
                                print("Inside Login Loop")
                                account_sid = "AC5adda6db593a0f369a427283c8436959"
                                auth_token = "fc647306d1cd37646ac0f1f23c55e612"
                                client = Client(account_sid, auth_token)
                                client.api.account.messages.create(
                                to="+13153538299",
                                from_="+13153229683",
                                body=text5)
                                print("Message Sent")
                                smsmsg="Notes Sent Successfully"
                                f=open("SMSSpeech.vbs","w+")
                                k="Dim sapi \nSet sapi=Createobject(\"sapi.spvoice\") \nsapi.Speak "+'"'+smsmsg+'"'
                                f.write(k)
                                f.close()
                                os.system("SMSSpeech.vbs")
        return render_template('Notes.html',notes=text5)




