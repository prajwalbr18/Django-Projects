from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def register(request):
    if request.method=="POST":
        f=request.POST['fname']
        u=request.POST['uname']
        e=request.POST['email']
        p1=request.POST['password']
        p2=request.POST['password1']
        if p1==p2:
             if User.objects.filter(username=u).exists():
                messages.info(request,"username available")
                return render(request,"register.html")
             elif User.objects.filter(email=e).exists():
                  messages.info(request,"email exists")
                  return render(request,"register.html")
             else:
            
                 user=User.objects.create_user(first_name= f,username= u,email= e,password=p1)
                 user.save()
                 return redirect('login')
        else:
             messages.info(request,"password not matching")
             return render(request,"register.html")
    else:
              
            return render(request,"register.html")
def login(request):
         if request.method=="POST":
              u=request.POST['uname']
              p=request.POST['password']
              user=auth.authenticate(username=u,password=p)
              if user is not None:
                   auth.login(request,user)
                   return redirect("data")
              else:
                    messages.info(request,"invalid credentials")
                    return render(request,"login.html")   
         return render(request,"login.html")

def logout(request):
     auth.logout(request)
     return redirect("/")
def data(request):
    return render(request,"data.html")
def detect(request):
    if request.method=="POST":
         V1=float(request.POST['v1'])
         V2=float(request.POST['v2'])
         V3=float(request.POST['v3'])
         V4=float(request.POST['v4'])
         V5=float(request.POST['v5'])
         V6=float(request.POST['v6'])
         V7=float(request.POST['v7'])
         V8=float(request.POST['v8'])
         V9=float(request.POST['v9'])
         V10=float(request.POST['v10'])
         import pandas as pd
         df=pd.read_csv(r"static/credit.csv")
         import matplotlib.pyplot as plt
         import seaborn as sns

         sns.heatmap(df.isnull())
         plt.show()
         print("****")
         print(df.shape)
         print("****")
         print(df.isnull().sum)
         print("****")
         print(df.dropna(inplace=True))
         print("****")
         sns.countplot(df["Amount"])
         plt.show()
         X_train=df[["V2","V3","V4","V5","V6","V7","V8","V9","V10"]]
         Y_train=df[["Amount"]]
         from sklearn.linear_model import LinearRegression
         lin=LinearRegression()
         lin.fit(X_train,Y_train)
         import numpy as np
         detect_credit=np.array([[V2,V3,V4,V5,V6,V7,V8,V9,V10]],dtype=object)
         detect_credit1=lin.predict(detect_credit)
         print("detected credit:",detect_credit1)
         return render(request,"detect.html",{"V1":V1,"V2":V2,"V3":V3,"V4":V4,
                                              "V5":V5,"V6":V6,"V7":V7,"V8":V8,"V9":V9,"V10":V10,
                                              "credit":detect_credit1})
    return render(request,"detect.html")

