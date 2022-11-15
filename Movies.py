from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import json
import webbrowser

#window/canvas
root = Tk()
root.title ("Movie Lookup")
root.geometry("200x600")
root.configure(background="#856ff8")

#lookup function for title
def titlelookup():
    #title.get()
    #titlename= Label(root, text=title.get())
    #titlename.grid(row=1, column=0, columnspan=2)
    try:   
        request= requests.get("http://www.omdbapi.com/?apikey=12a12b8c&t="+title.get())
        api= json.loads(request.content) #recieved content is recieved in JSON
        movie= api['Title']
        plot= api['Plot']
        awards= api['Awards']
        poster= api['Poster'] #used later on in order to get a poster image
    #in case of an error while fetching data from API
    except Exception as e:
        api= "Error..."

    #label for the movie once searched
    label= Label(root, text= movie +"-"+ plot +"\n\n"+ "Awards: "+ awards , font=("Times New Roman", 14), background="#856ff8", wraplength= 150) 
    label.grid(row=1, column=0, columnspan=4)

    #define a function to open link from a given URL secured from the API
    def posterlink():
        webbrowser.open_new(poster)
    #make the button and link it to a poster
    posterbtn= ttk.Button(root, text='Obtain Movie Poster', command=posterlink)
    posterbtn.grid(row=3,column=0)


#input to lookup
title=Entry(root)
title.grid(row=0, column=0)

#search button
titlebtn= Button(root, text="Search", command=titlelookup)
titlebtn.grid(row=0, column=3)

root.mainloop()