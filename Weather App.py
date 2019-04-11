import requests
import json
from tkinter import *
from PIL import Image, ImageTk
import os
import urllib.request


class WeatherApp:
    def __init__(self, master):
        self.width = 600
        self.height = 550
        self.canvas = Canvas(master, height= self.height, width= self.width)
        self.canvas.pack()
        self.background_image = PhotoImage(file='canvaspic.png')
        self.background_label = Label(master, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)
        self.frame1 = Frame(master, bg="#80dfff", bd=10)
        self.frame1.place(relx = 0.1, rely=0.1, relheight = 0.2, relwidth= 0.8)
        self.label1 = Label(self.frame1, bg="white")
        self.label1.place(relx = 0.001, rely=0.005, relheight = 1, relwidth= 1)
        self.button1 = Button(self.label1, text="Get Weather", font="Arial", command= lambda: self.get_weather())
        self.button1.place(relx = 0.65, rely=0.2, relheight = 0.6, relwidth= 0.3)
        self.entry1 = Entry(self.label1, font="Arial")
        self.entry1.place(relx=0.05, rely=0.2, relheight=0.6, relwidth=0.5)
        self.frame2 = Frame(master, bg="#80dfff", bd=10)
        self.frame2.place(relx = 0.1, rely=0.7, relheight = 0.2, relwidth= 0.8)
        self.label2 = Label(self.frame2, bg="white", font="Arial")
        self.label2.place(relx = 0.001, rely=0.005, relheight = 1, relwidth= 1)
        self.testimage = PhotoImage(file="01d.png")
        self.label3 = Canvas(self.frame2, bg="white", bd=0, highlightthickness=0)
        self.label3.place(relx=0.7, rely=0.1, relheight=0.7, relwidth=0.3)

    def get_weather(self):
        try:
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=85071fc9957db8d8bf613dfd2b66c598"
            city = self.entry1.get()
            r = requests.get(url.format(city)).json()
            city_ = city
            temp = r["main"]["temp"]
            conditions = r["weather"][0]["description"]
            icon_ = r["weather"][0]["icon"]
            final_output = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city_, conditions, temp)
            self.label2["text"] = final_output
            self.open_image(icon_)
        except:
            self.label2["text"] = "There was a problem retrieving that information"

    def open_image(self, icon):
        size = int(self.frame2.winfo_height() * 0.75)
        img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
        self.label3.delete("all")
        self.label3.image = img
        self.label3.create_image(0, 0, anchor='nw', image=img)

root = Tk()
root.title("Weather App")
app_gui = WeatherApp(root)
root.mainloop()












