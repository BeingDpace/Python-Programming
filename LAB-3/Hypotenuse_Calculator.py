import tkinter
class Hypotenuse:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Right Triangle Calculator")

        # Create the four frames.
        self.a_frame = tkinter.Frame(self.main_window)
        self.b_frame = tkinter.Frame(self.main_window)
        self.c_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for side A.
        self.a_label = tkinter.Label(self.a_frame, text='side A:')
        self.a_entry = tkinter.Entry(self.a_frame, width=40)
        self.a_label.pack(side='left', padx=5)
        self.a_entry.pack(side='left')
        
        # Create and pack the widgets for side B.
        self.b_label = tkinter.Label(self.b_frame, text='side B:')
        self.b_entry = tkinter.Entry(self.b_frame, width=40)
        self.b_label.pack(side='left', padx=5)
        self.b_entry.pack(side='left')

        # Create and pack the widgets for the side C(Hypotenuse).
        self.result_label = tkinter.Label(self.c_frame, text='side C:')
        self.c = tkinter.StringVar() # To update Hypotenuse
        self.c_label = tkinter.Label(self.c_frame, textvariable=self.c)
        self.result_label.pack(side='left', padx=5)
        self.c_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate',
                                          command=self.calc_hypotenuse, width=10)
        self.exit_button = tkinter.Button(self.button_frame,text='Exit',
                                          command=self.main_window.destroy, width=10)
        self.exit_button.pack(side='right', padx=5)
        self.calc_button.pack(side='right')
        

        # Pack the frames.
        self.a_frame.pack(pady=5, padx=5)
        self.b_frame.pack(pady=5, padx=5)
        self.c_frame.pack(anchor='w', padx=5, pady=5)
        self.button_frame.pack(anchor='se', padx=3, pady=3)

        # Start the main loop.
        tkinter.mainloop()
        
    def calc_hypotenuse(self):
        # Get the two sides and store them in variable.
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        
        # Calculate the hypotenuse.
        h = (a ** 2 + b ** 2) ** (1/2)
        
                            

        # Update the c_label widget by storing the value of self.c in the StringVar
        # object referenced by c.
        self.c.set(format(h,'.3f'))

# Create an instance of the TestAvg class.
c_hypotenuse = Hypotenuse()
