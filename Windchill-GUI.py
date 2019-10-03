# Author: Jessica Strait
# This project creates a windchill calculator using GUI methods.

#Let's begin by importing the tkinter module. Next, we will establish our class and start defining our method.
import tkinter


class windchill:

    def __init__(self):
#Per the instructions given in the video, we will create our main window and all necessary frames.
        self.main_window = tkinter.Tk("Windchill Calculator")
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()
        
#Next, we will need four labels and two entries: a title label, a temperature label and entry, a wind speed label and entry, and a solution label. Choose colors for our title also!
        self.title_label = tkinter.Label(self.frame1, text="Windchill Calculator", bg="light blue", fg="navy",\
                                         font='verdana, 12')
        self.temperature_label = tkinter.Label(self.frame2, text="Enter the temperature in degrees Fahrenheit.")
        self.temperature_entry = tkinter.Entry(self.frame2, width=10)
        self.speed_label = tkinter.Label(self.frame3, text="Enter the wind speed in miles per hour.")
        self.speed_entry = tkinter.Entry(self.frame3, width=10)
        self.solution_label = tkinter.Label(self.frame5, text="The windchill temperature in degrees Fahrenheit is:")

#Don't forget to pack everything we made!
        self.title_label.pack(side='left')
        self.temperature_label.pack(side='left')
        self.speed_label.pack(side='left')
        self.temperature_entry.pack(side='left')
        self.speed_entry.pack(side='left')
        self.solution_label.pack(side='left')

#We will set a string variable value to allow for our program to run multiple times. We will assign that value a label, a place in the window, and pack it.
        self.value = tkinter.StringVar()
        self.windchill_label = tkinter.Label(self.frame5, textvariable=self.value)
        self.windchill_label.pack(side='bottom')

#Now, let's create the button that will be clicked to calculate our windchill. We will get to the function that does the calculating quickly. Remember to pack it!
        self.calculate_button = tkinter.Button(self.frame4, text='Calculate Windchill', command=self.convert)
        self.calculate_button.pack(side='top')

#While we're packing, let's go ahead and pack all of our frames. Then, we enter the main loop.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        tkinter.mainloop()

#Now it's time to define our calculator function. We can use the same calculations we used in Assignment 11, but we should adjust the variables to use the data from our entries.
    def convert(self):
        temperature = float(self.temperature_entry.get())
        speed = float(self.speed_entry.get())
        chill = 35.74 + (.6215 * int(temperature) - (35.75 * int(speed) ** .16) + (
                .4275 * int(temperature) * int(speed) ** .16))
#We should round off our answer. Next, we can set our string variable to our value. It can be changed each time the function is run.
        solution = round(float(chill), 1)
        self.value.set(solution)

#At last, we create an instance of our code!
windchill_GUI = windchill()
