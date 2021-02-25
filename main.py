from tkinter import *
import tkinter as tk
import requests
from PIL import ImageTk, Image

def output(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		if Fbutton:
			final_str = 'Place: %s \nWeather: %s \nTemperature: %s' % (name, desc, temp)

		if Cbutton:
			final_str = 'Place: %s \nWeather: %s \nTemperature: %s' % (name, desc, temp)


	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def c_weather(location):
	weather_key = '7f7b3c3fbedd8bd25ca73f09b2a9ac7a'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	parameter = {'APPID': weather_key, 'q': location, 'units': 'Imperial'}
	response = requests.get(url, params=parameter)
	weather = response.json()

	label['text'] = output(weather)

def f_weatherM(location):
	weather_key = '7f7b3c3fbedd8bd25ca73f09b2a9ac7a'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	parameter = {'APPID': weather_key, 'q': location, 'units': 'Metric'}
	response = requests.get(url, params=parameter)
	weather = response.json()

	label['text'] = output(weather)

root = tk.Tk()

root.title("WEATHER APP")

img = ImageTk.PhotoImage(Image.open('weather icon.png'))

root.resizable(height=False, width=False)

canvas = tk.Canvas(root, height=650, width=650,bg='light yellow')
canvas.pack()

frame = tk.Frame(root, height=550, width='550', bg='light blue', bd=30)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n',)

entry = tk.Entry(frame, font=30, bg='lightgrey')
entry.place(relwidth=0.5, relheight=1)

Fbutton = tk.Button(frame, text="Fahrenheit", font='25', command=lambda: c_weather(entry.get()))
Fbutton.place(relx=0.55,rely=-.5,relheight=1, relwidth=0.25)

Cbutton = tk.Button(frame, text="Celsius", font='25', command=lambda: f_weatherM(entry.get()))
Cbutton.place(relx=0.55,rely=.5,relheight=1, relwidth=0.25)

lower_frame = tk.Frame(root, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame,bg='lightgrey', font='25')
label.place(relwidth=1, relheight=1)



root.mainloop()