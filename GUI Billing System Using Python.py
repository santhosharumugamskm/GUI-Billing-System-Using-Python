# import tkinter module 
from tkinter import *
import tkinter as tk
# make a window 
window = tk.Tk() 

# specify it's size 
window.geometry("700x600") 

# label it in the background 
label17 = Label(window)

# position the image as well 
label17.place(x=0, y=0) 


# function to calculate the 
# price of all the orders 
def calculate(): 

		# dic for storing the 
	# food quantity and price 
	dic = {'dosa': [e1, 30], 
		'vada': [e2, 10], 
		'upma': [e3, 25], 
		'puri': [e4, 15], 
		'pongal': [e5, 30], 
		'idly': [e6, 10]} 
	total = 0
	for key, val in dic.items(): 
		if val[0].get() != "": 
			total += int(val[0].get())*val[1] 

	label16 = Label(window, 
					text="Your Total Bill is - "+str(total), 
					font="times 18") 

	# position it 
	label16.place(x=20, y=490) 
	label16.after(1000, label16.destroy) 
	window.after(1000, calculate) 


label8 = Label(window, 
			text="SANTHOSH RESTAURANT ", 
			font="times 28 bold") 
label8.place(x=350, y=20, anchor="center") 


label1 = Label(window, 
			text="Menu", 
			font="times 28 bold") 

label1.place(x=520, y=70) 

label2 = Label(window, text="dosa \ Rs 30", font="times 18") 

label2.place(x=450, y=120) 

label3 = Label(window, text="vada \ Rs 10", font="times 18") 

label3.place(x=450, y=150) 

label4 = Label(window, text="upma \ Rs 25", font="times 18") 
label4.place(x=450, y=180) 

label5 = Label(window, text="puri \  Rs 15", font="times 18") 

label5.place(x=450, y=210) 

label6 = Label(window, text="pongal\  Rs 30", font="times 18") 

label6.place(x=450, y=240) 

label7 = Label(window, text="idly \  Rs 15", font="times 18") 

label7.place(x=450, y=270) 

# billing section 
label9 = Label(window, text="Select the items", 
			font="times 18") 
label9.place(x=115, y=70) 

label10 = Label(window, 
				text="dosa", 
				font="times 18") 
label10.place(x=20, y=120) 

e1 = Entry(window) 
e1.place(x=20, y=150) 

label11 = Label(window, text="vada", 
				font="times 18") 
label11.place(x=20, y=200) 

e2 = Entry(window) 
e2.place(x=20, y=230) 

e3 = Entry(window) 
e3.place(x=20, y=310) 

label12 = Label(window, text="upma", 
				font="times 18") 
label12.place(x=20, y=280) 

label13 = Label(window, 
				text="puri", 
				font="times 18") 
label13.place(x=20, y=360) 

e4 = Entry(window) 
e4.place(x=20, y=390) 

label14 = Label(window, 
				text="pongal", 
				font="times 18") 
label14.place(x=250, y=120) 

e5 = Entry(window) 
e5.place(x=250, y=150) 

label15 = Label(window, 
				text="idly", 
				font="times 18") 

label15.place(x=250, y=200) 

e6 = Entry(window) 
e6.place(x=250, y=230) 

# execute calculate function after 1 second 
window.after(1000, calculate) 

# closing the main loop 
window.mainloop() 
