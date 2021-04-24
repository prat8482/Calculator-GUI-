from tkinter import *
import requests

HEIGHT=700
WIDTH=800


def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=weather['main']['temp']
        
        final_str='City: %s \nCondtions: %s \nTemperature(in deg.): %s'%(name, desc, temp)
    except:
        final_str='There was a problem retreiving data'
    return final_str

        
def get_weather(city):
    weather_key='2e13af1291350dbdd84ba993e8a9d302'
    url='https://api.openweathermap.org/data/2.5/weather?id=524901&appid=2e13af1291350dbdd84ba993e8a9d302'
    params={'APPID':'weather_key', 'q':city, 'units':'metric'}
    response=requests.get(url,params=params)
    weather=response.json()
    
    label['text']=format_response(weather) 


root=Tk()

canvas=Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image=PhotoImage(file=r'C:\Users\prath\Pictures\landscape3.png')
bg_label=Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame=Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry=Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button=Button(frame, text='Get Weather', font=40, command= lambda:get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame=Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')

label=Label(lower_frame, font=('Courier',18),anchor='nw', justify='left')
label.place(relwidth=1, relheight=1)

root.mainloop()
