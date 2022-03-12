from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("YouTube Video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
menu=StringVar()
menu.set("Select Resolution")

drop=OptionMenu(root,menu,"240p","360p","480p","720p","1080p").place(x = 60, y = 120)



def Downloader():    
    url =YouTube(str(link.get()))
    video = url.streams.filter(res=str(menu.get())).first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()