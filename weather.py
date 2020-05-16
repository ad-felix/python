from tkinter import *
import requests

class irctc:
    def __init__(self):
        self.root = Tk()

        self.root.title("Weather2Go")
        self.root.minsize(500,800)

        self.root.configure(background="#077fbb")

        self.label1 = Label(self.root, text="-----Weather2Go----" ,bg="#000",fg="#fff")
        self.label1.configure(font=("Sans-serif",22,'bold'))
        self.label1.pack(pady=(10))


        self.trainNo = Entry(self.root,text="City Name:")
        self.trainNo.pack(ipadx=40,ipady=5)


        self.click = Button(self.root,text="Check",bg="#fff",fg="#000",width=15,height=1,font=("Sans-serif",10),command=lambda:self.__fetch())
        self.click.pack(pady=(10))


        self.result = Label(self.root,text="",bg="#000")
        self.result.configure(font=("Constantia",10))
        self.result.pack(pady=(5,10))

        self.root.mainloop()

    def __fetch(self):
        location = self.trainNo.get()
        
        self.result.configure(text="")
        
        if location != "":
            print(location)
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=4eca99834152acf9fb3d40242a4137e6".format(location)
            response = requests.get(url)
            data = response.json()
            

            print(data['main']['temp'])
            k = int(data['main']['temp'])
            kmin = data['main']['temp_min']
            kmax = data['main']['temp_max']
            humidity = data['main']['humidity']
            c = k - 273
            cmin = int(kmin - 273)
            cmax = int(kmax - 273)
            self.result = Label(self.root,text="")
            self.result.configure(text="Temp : {} degrees Celcius \n Min : {} degrees Celcius \n Max : {} degrees Celcius \n Humidity : {}".format(c,cmin,cmax,humidity),font=("Sans-serif",14,'bold'))
            self.result.pack(pady=(5,10))
        else:
            self.result = Label(self.root,text="")
            self.result.configure(text="Invalid Data! Try Again!")
            self.result.pack(pady=(5,10))

i = irctc()
