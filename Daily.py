import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import scrolledtext
from tkcalendar import Calendar, DateEntry
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import *


class Main_Win:
    """
    This class opens an introduction window.
    """

    def __init__(self, main):
        self.main = main
        self.main.title("Technician's Service Journal")
        
        ## this is a blank icon that replaced the Wing Personal 7.2 default icon
        self.main.iconbitmap('c:/Users/prhig/Dropbox/Programming/LocalGit/DailyJournal/wing.ico')  
        
        ## get the user's screen information
        sc_width = self.main.winfo_screenwidth()
        sc_height = self.main.winfo_screenheight()
        
        WIDTH = sc_width
        HEIGHT = sc_height
        
        self.main.geometry("%dx%d"%(WIDTH, HEIGHT))
        
        ## window opens maximized with no resize ability
        self.main.state('zoomed')  
        self.main.resizable(False, False)
        
        ## using a canvas so an image can be displayed
        self.canvas = tk.Canvas(self.main)
        self.canvas.pack(fill='both', expand=True)
        
        self.Label=tk.Label(self.canvas, text="", height=7).pack(fill='x')
        self.Label=tk.Label(self.canvas, text="Welcome to the Service Technicians Journal", bg="lightgreen", font=24).pack(fill='x')
        self.Label=tk.Label(self.canvas, text="Created by an Alarm Service Tech for Service Technicians", bg="lightgreen").pack(fill='x')
        self.Label=tk.Label(self.canvas, text="An Archive for Service Calls and Private Notes", bg="lightgreen").pack(fill='x')
        
        ## the image is located and then centered on the canvas
        self.img = tk.PhotoImage(file='c:/Users/prhig/Dropbox/Programming/LocalGit/DailyJournal/keypad.png')
        my_image = self.canvas.create_image((sc_width/2),(sc_height/2), anchor='center', image=self.img)
        
       
        self.exit_btn = tk.Button(self.canvas, text=("<", 'Exit'), command=self.close_main).place(relx=0.25, rely=0.4, relheight=0.2)
        self.next_btn = tk.Button(self.canvas, text=('Next', ">"), command=self.open_child).place(relx=0.75, rely=0.4, relheight=0.2)
        
        
        self.Label=tk.Label(self.canvas, text="", height=7).pack(side='bottom', fill='x')
        self.Label=tk.Label(self.canvas, text="By Paul Higginbotham Open Source Software 2021", bg="lightgreen").pack(side='bottom', fill='x')
        
    def close_main(self):
        self.main.destroy()
        
    def open_child(self):
        ## closes the introduction window BUT it can be brought back with "root.deiconify()"
        self.main.withdraw()
        
        ## THE MAGIC THAT OPENS THE NEW WINDOW
        self.new_window = tk.Toplevel(self.main)
        
        ## the 2nd self is passing a reference of the main window to the new window
        win2 = Child_Win2(self.new_window, self)
        self.new_window.title("Call Sheet Information")             
    
class Child_Win2:
    
    def __init__(self, win2, mainwindow):
        self.win2 = win2
        
        ## this is a blank icon that replaced the Wing Personal 7.2 default icon
        self.win2.iconbitmap('c:/Users/prhig/Dropbox/Programming/LocalGit/DailyJournal/wing.ico')         
        
        ## get the user's screen information
        sc_width = self.win2.winfo_screenwidth()
        sc_height = self.win2.winfo_screenheight()
        
        WIDTH = sc_width
        HEIGHT = sc_height
        
        self.win2.geometry("%dx%d"%(WIDTH, HEIGHT))
        
        ###############################
        ##   Disable window resize   ##
        ###############################
        self.win2.state('zoomed')  
        self.win2.resizable(False, False)
        
        ###############################
        ##       Frame Widgets       ##
        ###############################
        self.frame1 = tk.Frame(self.win2, bd=10, highlightbackground='sky blue', highlightcolor='sky blue', highlightthickness=2)
        self.frame1.pack(fill='both', expand=True)
        
        ###############################
        ##       Label Widgets       ##
        ###############################
        self.win2lbl = tk.Label(self.frame1, text="Date: ", font=40)
        self.win2lbl.pack(side='nw', padx=20)

        ###############################
        ##       Input Widgets       ##
        ###############################
        self.cal = DateEntry(self.frame1, font=40)
        self.cal.pack(side='nw', padx=20)


        ###############################
        ##       Button Widgets      ##
        ###############################
        self.mainbtn = tk.Button(self.mainframe, text = "New Call") #, command=self.win2_newcall
        self.mainbtn.place(relx=0.025, rely=0.37, relwidth=0.3, relheight=0.25)
        self.mainbtn = tk.Button(self.mainframe, text = "Return Call")
        self.mainbtn.place(relx=0.348, rely=0.37, relwidth=0.3, relheight=0.25)
        self.mainbtn = tk.Button(self.mainframe, text = "Search")
        self.mainbtn.place(relx=0.67, rely=0.37, relwidth=0.3, relheight=0.25)        
        self.mainbtn = tk.Button(self.mainframe, text = "Exit") #, command=self.close_main
        self.mainbtn.place(relx=0.025, rely=0.69, relwidth=0.944, relheight=0.25)        
'''
    def close_main(self):
        self.main.destroy()

        ###############################
        ##  Toplevel Window Widgets  ##
        ###############################      
    def win2_newcall(self):
        self.main.withdraw()
        # THE MAGIC THAT OPENS THE NEW WINDOW
        self.newcallwindow = tk.Toplevel(self.main)
        # the 2nd self is passing a reference of mainWindow to the new window
        win2 = CallWindow(self.newcallwindow, self)
        self.newcallwindow.title("New Call")

    def returncallsearch_window(self):
        self.main.withdraw()
        self.newcallwindow = tk.Toplevel(self.main)
        rcwin = ReturnCallSearch(self.newcallwindow, self)
        self.newcallwindow.title("Return Call Search")    

    def search_window(self):
        self.main.withdraw()
        self.searchwindow = tk.Toplevel(self.main)
        srchwin = Search(self.searchwindow, self)
        
        
class CallWindow():
    """
    This class will receive the date from the main class and display it, it will also
    display multiple label, entry and button widgits which will later interact with a 
    SQLite3 database
    """
    def __init__(self, call_win, mainwindow): # mainwindow reference is what allows data to be passed to the this class
        self.call_win = call_win
        
        sc_width = self.call_win.winfo_screenwidth()
        sc_height = self.call_win.winfo_screenheight()
        WIDTH=(sc_width/10)*4
        HEIGHT=(sc_height/10)*8       
        x_coordinate = (sc_width/2)-(WIDTH/2)
        y_coordinate = (sc_height/2)-(HEIGHT/2)
        self.call_win.geometry("%dx%d+%d+%d"%(WIDTH, HEIGHT, x_coordinate, y_coordinate))
        #self.call_win.resizable(width=False, height=False)
        
        self.cwframe = tk.Frame(self.call_win)
        self.cwframe.place(relwidth=1, relheight=1)
        
        
        ###########################################
        ##       Call Window Label Widgets       ##
        ###########################################
        self.cwlbl_date = tk.Label(self.cwframe, text="Date: ", font=40)
        self.cwlbl_tracking = tk.Label(self.cwframe, text="Tracking # :", font=40)
        self.cwlbl_workorder = tk.Label(self.cwframe, text="Work Order # :", font=40)
        self.cwlbl_custname = tk.Label(self.cwframe, text="Customer Name :", font=40)
        self.cwlbl_custaddr = tk.Label(self.cwframe, text="Customer Address :", font=40)
        self.cwlbl_custissue = tk.Label(self.cwframe, text="Customer's Issue :", font=40)
        self.cwlbl_repairnotes = tk.Label(self.cwframe, text="Repair Notes :", font=40)
        
        self.cwlbl_date.place(relx=0.02, rely=0.03)
        self.cwlbl_tracking.place(relx=0.02, rely=0.07)
        self.cwlbl_workorder.place(relx=0.02, rely=0.11)
        self.cwlbl_custname.place(relx=0.02, rely=0.15)
        self.cwlbl_custaddr.place(relx=0.02, rely=0.19)
        self.cwlbl_custissue.place(relx=0.02, rely=0.24)
        self.cwlbl_repairnotes.place(relx=0.02, rely=0.32)
        
        
        ###########################################
        ##       Call Window Input Widgets       ##
        ###########################################        
        self.cwtxt_date = tk.Entry(self.cwframe, font=40)
        self.cwtxt_date.place(relx=0.22, rely=0.03, relwidth=0.125)
        self.cwtxt_tracking = tk.Entry(self.cwframe, font=40)
        self.cwtxt_tracking.place(relx=0.22, rely=0.07, relwidth=0.14) 
        self.cwtxt_workorder = tk.Entry(self.cwframe, font=40)
        self.cwtxt_workorder.place(relx=0.22, rely=0.11, relwidth=0.14) 
        self.cwcbo_custname = ttk.Combobox(self.cwframe, font=40)
        self.cwcbo_custname.place(relx=0.22, rely=0.15, relwidth=0.5)
        self.cwcbo_custaddr = ttk.Combobox(self.cwframe, font=40)
        self.cwcbo_custaddr.place(relx=0.22, rely=0.19, relwidth=0.5)
        self.cwtxt_custissue = tk.Entry(self.cwframe, font=40)
        self.cwtxt_custissue.place(relx=0.02, rely=0.27, relwidth=0.9)
        self.cwtxt_notes = scrolledtext.ScrolledText(self.cwframe, wrap='word', font=40)
        self.cwtxt_notes.place(relx=0.02, rely=0.35, relwidth=0.92, relheight=0.1)
        
        
        ###########################################
        ##       Call Window Button Widgets      ##
        ###########################################        
        self.cwbtn_save = tk.Button(self.cwframe, text = "SAVE", font=40, bd=2)
        self.cwbtn_save.place(relx=0.02, rely=0.475, relwidth=0.125)
        self.cwbtn_clear = tk.Button(self.cwframe, text = "CLEAR", font=40, bd=2)
        self.cwbtn_clear.place(relx=0.175, rely=0.475, relwidth=0.125)
        self.cwbtn_update = tk.Button(self.cwframe, text = "UPDATE", font=40, bd=2)
        self.cwbtn_update.place(relx=0.33, rely=0.475, relwidth=0.125)
        self.cwbtn_exit = tk.Button(self.cwframe, text = "EXIT", font=40, bd=2, command=self.close_call_win)
        self.cwbtn_exit.place(relx=0.485, rely=0.475, relwidth=0.125)        
         
         
         
        ############################################
        ##       Call Window Display Widgets      ##
        ############################################ 
         
        
        
    ###########################################
    ##    Call Window Functions / Methods    ##
    ###########################################
    def close_call_win(self):
        root.deiconify()
        self.call_win.destroy()
        
        # transfering data from the 1st class into the 2nd class populating the entry box
        #self.nctxt_date.insert(0, mainwindow.cal.get())
        
'''        

        



if __name__ == '__main__':
    root = tk.Tk()
    app = Main_Win(root)
    root.mainloop()


