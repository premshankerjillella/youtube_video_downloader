import tkinter as tk
import pytube



window = tk.Tk()
#title
window.title(" Our YouTube Downloader")
#size
window.geometry("400x400")


#functions


def info_disp():
	greeting="File has been succesfully donwloaded!"
	greeting_display=tk.Text(master=window,height=10,width=20)
	greeting_display.grid(column=0,row=4,padx=10, pady=10)
	greeting_display.insert(tk.END,greeting)



def downloader():
	hi=info_disp()
	link=str(entry1.get())
	yt = pytube.YouTube(link)
	stream = yt.streams.first()
	destination="C:\\Users\\PC\\Desktop"
	stream.download(destination)

	
	




#label

title=tk.Label(text="Hello! welcome to my YouTube Downloader.",font=30)
title.grid(column=0,row=0,padx=10, pady=10)

#label2

label2=tk.Label(text="Please Enter the link of the video")
label2.grid(column=0,row=1,padx=10, pady=10)

#entry

entry1=tk.Entry()
entry1.grid(column=0,row=2)

#button 1
button1=tk.Button(text="Click Here",font=15,bg="red",command=downloader)
button1.grid(column=0,row=3,padx=10, pady=10)


window.mainloop()
