import requests
from bs4 import BeautifulSoup
import plyer
def datacolleted():
    def notification(title,message):
        plyer.notification.notify(
        title = title,
        message =  message,
        app_icon = 'covid.ico',
        timeout = 30       #we will keep notification for 30 sec
        )
        
        
    url = "https://www.worldometers.info/coronavirus/"
    res = requests.get(url)     #we can see responcse 200 means all our data has been fetched successfully
    soup = BeautifulSoup(res.content,'html.parser')
    tbody = soup.find('tbody')
    abc = tbody.find_all('tr')
    countrynotification = cntdata.get()
    #we will kepp world as a by default  when no country entered
    if(countrynotification == ""):
        countrynotification="world"

    # list of countries
    serial_number, countries, total_cases, new_cases, total_death, new_deaths, total_recovered, active_cases =[],[],[],[],[],[],[],[]
    serious_critical, total_cases_permn, total_death_permn, total_tests,total_test_permillion, total_pop = [],[],[],[],[],[]


    #header is used to name the columne that we have to downloded
    header = ['serial_number', 'countries', 'total_cases', 'new_cases', 'total_death', 'new_deaths', 'total_recovered', 'active_cases','serious_critical', 'total_cases_permn', 'total_death_permn', 'total_tests','total_test_permillion', 'total_pop']

    for i in abc:
        id = i.find_all('td')
        #print(id[1].text)          #id 1 is for country names all the country names will be printed
        if(id[1].text.strip().lower() == countrynotification):
            totalcases1 = int(id[2].text.strip().replace(',',""))
            totaldeath = id[4].text.strip()
            newcases = id[3].text.strip()        
            newdeaths = id[5].text.strip()
            notification("CORONA RECENT UPDATES of {}".format(countrynotification),"Total Cases : {}\nTotal Deaths : {}\nNew cases : {}\nNew Deaths : {}".format( 
                         totalcases1,totaldeath,newcases,newdeaths, 
                         ))
                       
            
        serial_number.append(id[0].text.strip())
        countries.append(id[1].text.strip())
        total_cases.append(id[2].text.strip().replace(',',""))  #because we want to remove comma blw numbers
        new_cases.append(id[3].text.strip())
        total_death.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip())
        total_recovered.append(id[6].text.strip())
        active_cases.append(id[7].text.strip())
        serious_critical.append(id[8].text.strip())
        total_cases_permn.append(id[ 9].text.strip())
        total_death_permn.append(id[10].text.strip())
        total_tests.append(id[11].text.strip())
        total_test_permillion.append(id[12].text.strip())
        total_pop.append(id[13].text.strip())
    # print(countries)    #it print the data about country
    # print(total_cases)   #it print the tottal cases by country
    # print(total_death)     #it print the tottal deaths by country
    
    #here we use zip function to store all the data together
    dataframe = pd.DataFrame(list(zip(serial_number, countries, total_cases, new_cases, total_death, new_deaths, total_recovered, active_cases,
                                      serious_critical, total_cases_permn, total_death_permn, total_tests,total_test_permillion, total_pop  )),columns=header)     
                                      
    
    #now for sort we use sort function  and here we will sort casese in acending 
    #which ountry has more cases
    
    sorts = dataframe.sort_values('total_cases',ascending = False)
    for a in flist:
        if(a== 'html'):
            path2 = '{}/coronadata.html'.format(path)
            sorts.to_html(r'{}'.format(path2))
            #we have given r to read our mentioned path
        if(a== 'json'):
            path2 = '{}/coronadata.json'.format(path)
            sorts.to_json(r'{}'.format(path2))
        if(a== 'excel'):
            path2 = '{}/coronadata.excel'.format(path)
            sorts.to_excel(r'{}'.format(path2))


# create message box
        if(len(flist)!=0):
            messagebox.showinfo("Notification","Corona Record is Saved {}".format(path2),parent=coro)
    
    
    
    #function for downloding the file
def downloaddata():
    #now if any dailog was not click
  
    if(len(flist)!=0):
        path = filedialog.askdirectory()
    else :
        pass
    datacolleted()
    flist.clear()  #after it donlod it come back to its normal state or disabled state
    Inhtml.configure(state = 'normal') 
    Injson.configure(state = 'normal') 
    Inexcel.configure(state = 'normal') 
    
    #this function for Disabled the html,json,excel files
def inhtmldownload():
    flist.append('html')
    Inhtml.configure(state = 'disabled')
     
def injsondownload():
    flist.append('json')
    Injson.configure(state = 'disabled')

def inexceldownload():
    flist.append('excel')
    Inexcel.configure(state = 'disabled')
      


#for data acending order we import pandas

import pandas as pd
from tkinter import *
from tkinter import messagebox,filedialog
coro = Tk()
coro.title("corona Virus Information")
coro.geometry("800x500+200+100")
coro.configure(bg='#046173')
#coro.iconbitmap('corona.ico')
flist =[]
path = ''





#labels

mainlabel = Label(coro,text="Corona Virus Live Tracker",font=("new roman",30,"italic bold"),bg="#05897A",width=33,fg="black",bd=5)
mainlabel.place(x=0,y=0)

label1 = Label(coro,text="Country Name :",font=("arial",20,"italic bold"),bg="#046173")
label1.place(x=15,y=100)

label2 = Label(coro,text="Download file in :",font=("arial",20,"italic bold"),bg="#046173")
label2.place(x=15,y=200)


cntdata=StringVar()
entry1=Entry(coro,textvariable=cntdata,font = ("arial",20,"italic bold"), relief = RIDGE,bd = 2,width =32)
entry1.place(x = 280,y=100)

#Buttons

Inhtml = Button(coro,text="Html",bg="#2DAE9A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground ="red",activeforeground="white",bd=5,width=5,command=inhtmldownload)

Inhtml.place(x=300,y=200)

Injson= Button(coro,text="Json",bg="#2DAE9A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground ="red",activeforeground="white",bd=5,width=5,command=injsondownload)

Injson.place(x=300,y=260)

Inexcel = Button(coro,text="Excel",bg="#2DAE9A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground ="red",activeforeground="white",bd=5,width=5,command=inexceldownload)

Inexcel.place(x=300,y=320)


Submit = Button(coro,text="Submit",bg="#CB054A",font=("arial",15,"italic bold"),relief=RIDGE,activebackground ="#7B0519",activeforeground="white",bd=5,width=25,command = datacolleted)

Submit.place(x=450,y=260)

coro.mainloop()





