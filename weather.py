import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk
import requests
HEIGHT = 600
WIDTH = 800
root = tk.Tk()
root.title('Weather app')
def on_enter(e):
    button.configure(bg='#e68a00',fg='white')

def on_leave(l):
    button.configure(bg='powder blue',fg='black')

def test_function(entry):
    print("The entry: ",entry)

def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
        pressure = weather['main']['pressure']
        humidity= weather['main']['humidity']
        final_str=' City: %s \n Conditions: %s \n Temperature (°F): %s \n Pressure: %s \n Humidity: %s' %(name,desc,temp,pressure,humidity)

    except :
        final_str ='There was a problem retrieving that information'

    return final_str

def get_weather(city):
    weather_key ='yourkey'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params  = {'APPID':weather_key,'q':city,'units':'imperial'}
    response  = requests.get(url,params=params)
    weather =response.json()
    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(file='weather1.jpg')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='#4d1933',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry= tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text="Get Weather",font=('Arial', 20,'italic bold'),bd=8,padx=16,pady=16 ,command=lambda: get_weather(entry.get()),activebackground='green',activeforeground='white',bg='powder blue')
button.place(relx=0.7 ,relwidth=0.3,relheight=1)

lower_frame = tk.Frame(root,bg='#4d1933',bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label = tk.Label(lower_frame,font=('Courier',18,'italic bold'),anchor='nw',justify='left',bd=4)
label.place( relwidth=1,relheight=1)

weather_icon = tk.Canvas(label , bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

button.bind('<Enter>',on_enter)
button.bind('<Leave>',on_leave)

root.mainloop()


