from tkinter import *

import psycopg2

conn = psycopg2.connect(database="postgres", user = "postgres", password = "1234", host = "127.0.0.1", port = "5432")
cur = conn.cursor()

import tkinter as tk
from PIL import Image, ImageTk
import requests,json
import time
def main():
		a = Tk()
		a.resizable(0,0)
		a.tk.call('wm', 'iconphoto', a._w,PhotoImage(file='001.png'))
		a.title("WEATHER")
		image = Image.open('0001.png')
		photo_image = ImageTk.PhotoImage(image)
		label = tk.Label(a, image = photo_image)
		label.grid(sticky="nse",rowspan="5",columnspan="5")

				
		current_temperature = IntVar()
		current_pressure = IntVar()
		current_humidity = IntVar()

		def calc(event=NONE):
    			
    			
				api_key = "bb9781bebd5657f08df059a18fb00091"
				base_url = "http://api.openweathermap.org/data/2.5/weather?"
				city_name = c.get()
				complete_url = base_url + "appid=" + api_key + "&q=" + city_name
				response = requests.get(complete_url)
				x = response.json()

				if x["cod"] != "404":
					y = x["main"]
					current_temperature = y["temp"]
					current_humidity = y["humidity"]
					z = x["weather"]
					weather_description = z[0]["description"]
					e3.insert(END,current_temperature-273.15)
					e5.insert(END,current_humidity)
					e4.insert(END,weather_description)
					e6.insert(END,times())
					h=times()
					v=dates()



					cur.execute('insert into weather (city,temp,humidity,time,date)values (%s,%s,%s,%s,%s)',(city_name,(current_temperature-273),current_humidity,h,v));
					conn.commit()




		def clear():
				e3.delete(1.0,END)
				e5.delete(1.0,END)
				e4.delete(1.0,END)
				e6.delete(1.0,END)

		def times():
			time1 = time.strftime('%H:%M:%S')
			return time1

		def dates():
			date1=time.strftime('%d/%m/%Y')
			return date1


		a.bind('<Return>', calc)

		b1=tk.Button(a,text="VIEW",command=calc)
		b1.grid(row=0,column=2)
		t1=Label(a,text="ENTER CITY NAME",height=1,width=20)
		t1.grid(row=0,column=0)
		c=StringVar()
		e1=Entry(a,textvariable=c)
		e1.grid(row=0,column=1)
		t2=Label(a,text="TEMP.",height=1,width=20)
		t2.grid(row=1,column=0)
		e3=Text(a,height=1,width=20)
		e3.grid(row=1,column=1)
		t4=Label(a,text="HUMIDITY",height=1,width=20)
		t4.grid(row=2,column=0)
		e5=Text(a,height=1,width=20)
		e5.grid(row=2,column=1)
		t3=Label(a,text="WEATHER POSSIBILITY",height=1,width=20)
		t3.grid(row=3,column=0)
		e4=Text(a,height=1,width=20)
		e4.grid(row=3,column=1)
		reset=Button(text="reset values",command=clear)
		reset.grid(row=4,column=4)
		t6=Label(a,text="Time",height=1,width=20)
		t6.grid(row=4,column=0)
		e6=Text(a,height=1,width=20)
		e6.grid(row=4,column=1)



		a.mainloop()



main()
conn.close()
