#importing required libraries
import tkinter as tk
from tkinter import *
from lyrics_extractor import SongLyrics

root = Tk()
root.geometry('600x600')
root.title('GetLyrics')
root.configure(bg='#326273') #background
head=Label(root, text="Enter the song you want Lyrics for", bg='#326273', font=('Raleway 15'))# a lable
head.pack(pady=25)
result =tk.StringVar()#ensuring result is string type
song=tk.StringVar()#ensuring song is string type

#window icon
icon_image = PhotoImage(file='icon.png')
root.iconphoto(False, icon_image)


def get_lyrics():
    song_name=song.get()# using get method getting value of song
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    extract_lyrics = SongLyrics(api_key, engine_id)
    song_lyrics = extract_lyrics.get_lyrics(song_name)
    result.set(song_lyrics)#setting the result

Entry(root, textvariable=song).pack()# enter a song name
Message(root,textvariable=result, bg="#eeeee4").pack(side=TOP,anchor=W,fill=BOTH, expand=1)#displaying the lyrics
#create a button
Button(root, text="SEARCH",command=get_lyrics, bg='#abdbe3').pack()

root.mainloop()

