# https://jsonviewer.stack.hu/ - use this to view the raw json file
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import webbrowser
class NewsApp:
    # A constructor is a special method in a class that automatically runs when you create an object of that class. 
    # It's mainly used to initialize variables.
    
    # 'self' is a reference to the current object (instance) inside a class. 
    # We use self because we don’t know in advance what the object’s name will be (like p, person1, etc.) when the class is used. 
    # It lets us access or modify that specific object's data from within its methods. 
    # Suppose the name of the object is 'p'. Then self.data gets replaced and becomes p.data. 
    # If we change the current object name or add another object (eg: p1) self.data becomes p1.data for the overwritten/new object.

    def __init__(self):
        # fetching data
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=yourAPIKEY').json()
        # The API sends JSON text, not Python objects.
        # .json() parses that text into a usable Python dictionary.
        self.load_gui()
        self.load_news_item(0)
    def load_gui(self):
        self.root=Tk()
        self.root.title("News App")
        self.root.geometry('350x600')
        self.root.resizable(0,0)
    
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        
    def load_news_item(self, index):
        # clear the screen
        self.clear()
        
        # place the image
        try:
            image_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(image_url).read() # Downloads the image from the URL as raw bytes
            im=Image.open(io.BytesIO(raw_data)).resize((350,250)) # # Converts raw bytes into an image and resizes it
            photo=ImageTk.PhotoImage(im) # Converts the image into a format Tkinter can display
            label=Label(self.root,image=photo)
            label.pack()
        except Exception:
            im=Image.open('/Users/puravdoshi/Downloads/GUI Projects/news_app/images-not-found.png').resize((350,250)) # # Converts raw bytes into an image and resizes it
            photo=ImageTk.PhotoImage(im) # Converts the image into a format Tkinter can display
            label=Label(self.root,image=photo)
            label.pack()
        # load news item
        heading=Label(self.root,text=self.data['articles'][index]['title'],fg='white',wraplength=350,justify='center',font=('verdana',20))
        heading.pack(pady=(20,10))
    
        # load news item
        details=Label(self.root,text=self.data['articles'][index]['description'],fg='white',wraplength=350,justify='center',font=('verdana',15))
        details.pack(pady=(20,10))
        
        # creating a frame
        frame=Frame(self.root) # Creates a container (frame) inside the main window to organize widgets.
        frame.pack(expand=True, fill=BOTH) # Expands the frame to fill all available space both horizontally and vertically.
        
        # creating the buttons
        if index!=0:
            prev=Button(frame,text='Previous',width=9, height=3, command=lambda: self.load_news_item(index-1))
            prev.pack(side=LEFT)
        
        read=Button(frame,text='Read More',width=9, height=3, command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        
        if index!=len(self.data['articles'])-1:
            next_news=Button(frame,text='Next',width=9, height=3, command=lambda: self.load_news_item(index+1))
            next_news.pack(side=LEFT)
        
        self.root.mainloop()
        
    def open_link(self,url):
        webbrowser.open(url)
        
obj=NewsApp()