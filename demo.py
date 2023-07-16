from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&units=imperial&APPID=df0791a9681275d07634c50ae72abc88").json()
    w_label1.config(text= data["weather"][0]["main"])
    wd_label1.config(text= data["weather"][0]["description"])
    temp_label1.config(text= str(int(data["main"]["temp"] )))       
    pre_label1.config(text= data["main"]["pressure"])


win = Tk()
win.title("stuti app")
win.config(bg= "teal")
win.geometry("500x570")

name_label = Label(win, text= "stuti's weather app", 
                   font= ("Ariel" , 30, "bold"))
name_label.place(x=25,y=50,height=50,width=450)


city_name = StringVar()
list_name = ("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
com = ttk.Combobox(win, text= "stuti's weather app", values= list_name,
                 font= ("Ariel" , 20), textvariable= city_name)
com.place(x=20,y=120,height=50,width=450)


w_label = Label(win, text= "Weather climate", 
                   font= ("Ariel" , 18))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win, text= "", 
                   font= ("Ariel" , 18))
w_label1.place(x=250,y=260,height=50,width=210)

wd_label = Label(win, text= "Weather description", 
                   font= ("Ariel" , 16))
wd_label.place(x=25,y=330,height=50,width=210)

wd_label1 = Label(win, text= "", 
                   font= ("Ariel" , 16))
wd_label1.place(x=250,y=330,height=50,width=210)

temp_label = Label(win, text= "Temperature", 
                   font= ("Ariel" , 18))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win, text= "", 
                   font= ("Ariel" , 18))
temp_label1.place(x=250,y=400,height=50,width=210)

pre_label = Label(win, text= "Pressure", 
                   font= ("Ariel" , 18))
pre_label.place(x=25,y=470,height=50,width=210)

pre_label1 = Label(win, text= "", 
                   font= ("Ariel" , 18))
pre_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win, text= "Done", 
                   font= ("Ariel" , 18), command= data_get)
done_button.place(x=200,y=190,height=50, width=100)

win.mainloop()