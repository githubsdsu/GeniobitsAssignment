from django.shortcuts import render,HttpResponse,redirect
from MainApp.models import *
from MainApp.form import *
import os
import json
# Create your views here.





# taking data from user
def upload(request):
    form=""
    timeframe=''
    success='no'
    if request.method=="POST":
        form=UploadFileForm(request.POST,request.FILES)
        timeframe=request.POST.get('timeframe')
        if form.is_valid():
            
            form.save()
            success='yes'
        else:
            form=UploadFileForm()   
        if success=='yes':
            
            a=os.listdir(r"D:/GeniobitsInternship/TradingProject/media/files")
            path=r"D:/GeniobitsInternship/TradingProject/media/files/"+a[0]
            with open(path,'r') as k:
                z=k.readlines()
                u=z[1:]
            
                timeframe=int(timeframe)
                listu=u[0].split()
               
                count=len(u)#length of lines
              
            
                d=count%timeframe
              
                propercount=count-d
              
                sets=propercount//timeframe
               
               
                anslist=[]
               
                for m in range(sets): #taking data from the file and string it in list format
                    dict1={}
                    banknifty=[]
                    date=[]
                    time=[]
                    open1=[]
                    high=[]
                    low=[]
                    close=[]
                    volume=[]
                    for n in range(timeframe):
                        value=u[n+(m*timeframe)]
                        valuelist=value.split(',')
                        
                    
                        banknifty.append(valuelist[0])
                        date.append(valuelist[1])
                        time.append(valuelist[2])
                        open1.append(valuelist[3])
                        high.append(valuelist[4])
                        low.append(valuelist[5])
                        close.append(valuelist[6])
                        volume.append(valuelist[7])    

                    #storing data in dictionary
                    dict1['BANKNIFTY']=banknifty[0]
                    dict1['DATE']=date[0]
                    dict1['TIME']=time[0]
                    dict1['OPEN']=open1[0]
                    dict1['HIGH']=max(high)
                    dict1['LOW']=min(low)
                    dict1['CLOSE']=close[-1]
                    dict1['VOLUME']=volume[-1]
                    
                    anslist.append(dict1)    
              
                if d!=0:   #if extra data remains then it is evaluated here
                    newvalue=-1-(d-1)
                    t=u[newvalue:]
                    dict1={}
                    banknifty=[]
                    date=[]
                    time=[]
                    open1=[]
                    high=[]
                    low=[]
                    close=[]
                    volume=[]
                    for i in range(d):
                        value=t[i]
                        valuelist=value.split(',')
                    
                        banknifty.append(valuelist[0])
                        date.append(valuelist[1])
                        time.append(valuelist[2])
                        open1.append(valuelist[3])
                        high.append(valuelist[4])
                        low.append(valuelist[5])
                        close.append(valuelist[6])
                        volume.append(valuelist[7])

                    dict1['BANKNIFTY']=banknifty[0]
                    dict1['DATE']=date[0]
                    dict1['TIME']=time[0]
                    dict1['OPEN']=open1[0]
                    dict1['HIGH']=max(high)
                    dict1['LOW']=min(low)
                    dict1['CLOSE']=close[-1]
                    dict1['VOLUME']=volume[-1]
                  
                    anslist.append(dict1)    
                
                jsonfile=json.dumps(anslist)#converting to json
                jsonfilepath=r"D:/GeniobitsInternship/TradingProject/static/jsonfile" #storing json file inside a folder 
                os.chdir(jsonfilepath)
                #saving json file to directory
                with open('data.txt', 'w') as f:
                    data = jsonfile
                    f.write(data)
               
                return redirect("http://127.0.0.1:8000/downloadjson")
    return render(request,"index.html",{form:form})

def download(request):

    return render(request,"downloadjson.html")
