from tkinter import * 
from PIL import Image, ImageTk
import os
current_dir='/Users/puravdoshi/Downloads/GUI Projects/wallpaper_viewer/Wallpaper'
counter = 0
def rotate_img():
    global counter
    counter = counter+ 1
    img_label.config(image=img_array[counter%len(img_array)])

def rotate_img2():
    global counter
    counter = counter - 1
    img_label.config(image=img_array[counter%len(img_array)])

files=os.listdir(current_dir)
img_array=[]
root=Tk()
root.title("Wallpaper Viewer")
root.geometry(('400x550'))
root.configure(background='#0096DC')
for file in files:
    img=Image.open(os.path.join(current_dir, file)) # os.path.join() safely combines folder and file names into a valid path.
    resized_img=img.resize((250,300))
    img_array.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root, image=img_array[0])
img_label.pack(pady=(20,10))

next_button=Button(root, text='Next', background='white', fg='black', width=15, height=2, font=('verdana',12), command=rotate_img)
next_button.pack(ipady=6)

prev_button=Button(root, text='Previous', background='white', fg='black', width=15, height=2, font=('verdana',12), command=rotate_img2)
prev_button.pack(pady=(20,10),ipady=6)

root.mainloop()
