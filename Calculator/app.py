from tkinter import *
root=Tk()

first_num=None
second_num=None
op=None

def get_digit(digit):
    current=result_label['text'] # It's just tkinter's special way of accessing widget properties — not an array or list.
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

# We don’t use .get() with Label and Button in Tkinter because they don’t store user input — they only display info.
# .get() is used with widgets like Entry, Text, or Spinbox that accept user input.
def get_first_num(operator):
    global first_num,op
    first_num=int(result_label['text'])
    op=operator
    result_label.config(text='')

def get_second_num():
    global second_num
    second_num=int(result_label['text'])
    if op=='+':
        result_label.config(text=str(first_num+second_num))
    elif op=='-':
        result_label.config(text=str(first_num-second_num))
    elif op=='x':
        result_label.config(text=str(first_num*second_num))
    elif op=='/':
        if(second_num==0):
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round((first_num/second_num),2)))
    else:
        result_label.config(text=second_num)

root.title("Calculator")
root.geometry('270x365')
root.resizable(0,0) # This means the window cannot be resized in the x-direction or y-direction
result_label=Label(root,text='',fg='white',font=('verdana',30,'bold'))
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25), sticky='w') # columnspan-over how many tiles it ranges, sticky- where it begins from

b7=Button(root, text='7',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(7))
# lambda: lets you pass a function with arguments without calling it immediately.
b7.grid(row=1,column=0)
b8=Button(root, text='8',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2,command=lambda:get_digit(8))
b8.grid(row=1,column=1)
b9=Button(root, text='9',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2,command=lambda:get_digit(9))
b9.grid(row=1,column=2)
b_plus=Button(root, text='+',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_first_num('+'))
b_plus.grid(row=1,column=3)

b4=Button(root, text='4',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(4))
b4.grid(row=2,column=0)
b5=Button(root, text='5',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(5))
b5.grid(row=2,column=1)
b6=Button(root, text='6',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(6))
b6.grid(row=2,column=2)
b_minus=Button(root, text='-',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_first_num('-'))
b_minus.grid(row=2,column=3)

b1=Button(root, text='1',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(1))
b1.grid(row=3,column=0)
b2=Button(root, text='2',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(2))
b2.grid(row=3,column=1)
b3=Button(root, text='3',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(3))
b3.grid(row=3,column=2)
b_multiply=Button(root, text='x',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_first_num('x'))
b_multiply.grid(row=3,column=3)

b_clr=Button(root, text='C',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=clear)
b_clr.grid(row=4,column=0)
b_equal=Button(root, text='=',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=get_second_num)
b_equal.grid(row=4,column=1)
b0=Button(root, text='0',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_digit(0))
b0.grid(row=4,column=2)
b_div=Button(root, text='/',highlightbackground="#00a62a",fg='red',font=('verdana',20,'bold'), width=2, height=2, command=lambda:get_first_num('/'))
b_div.grid(row=4,column=3)

root.mainloop()