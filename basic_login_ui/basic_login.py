from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email=email_input.get()
    password=password_input.get()
    if email=='pndoshi07@gmail.com' and password=='123':
        messagebox.showinfo('Hello there !', 'Login Successful')
    else:
        messagebox.showerror('Error !', 'Login Failed !')

root=Tk()
root.title("Login Form")
root.iconbitmap('favicon.ico') # to add icon image
# root.minsize(300,300) # minimum size of window
# root.maxsize(500,500) # maximum size of the window
root.geometry('450x700') # to create a window of fixed size
root.configure(background='#0096DC')

# process to configure and load an image
img=Image.open('flipkart.png')
resize_img=img.resize((150,150))
img=ImageTk.PhotoImage(resize_img) 
img_label=Label(root, image=img)
img_label.pack(pady=(10,10)) # using a geometry manager to fit the image explicitly with padding

# how to add text to an image
text_label=Label(root,text="Flipkart", fg='White', background='#0096DC')
text_label.pack()
text_label.config(font=('Verdana', 24)) # The .config() method is used to modify the properties of a widget after it has been created.

# Adding email and password options

email_label=Label(root,text="Enter your email", fg='white', background='#0096DC', font=('Verdana',12))
email_label.pack(pady=(20,5))

email_input=Entry(root, width=20, fg='black',background='yellow') # The Entry() widget in Tkinter creates a single-line text box where users can type input, like names, numbers, or passwords.
email_input.pack(ipady=6) # ipady in Tkinter stands for "internal padding in the y (vertical) direction".

password_label=Label(root, text="Enter your password", fg='white', background='#0096DC', font=('Verdana', 12))
password_label.pack(pady=(20,5))

password_input=Entry(root, fg='black', background='yellow')
password_input.pack(ipady=6)

# Button to Submit
login_btn = Button(root, text="Login Here", fg='black', background='white', font=("Verdana", 12), command=handle_login)
login_btn.pack(pady=(20,20),ipady=6)

root.mainloop() # keeps the GUI screen on constantly
