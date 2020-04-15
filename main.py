"""""
Copyright 2020 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""""

import tkinter as tk
from tkinter import filedialog, messagebox
import traceback
from PIL import ImageTk, Image
import socket
from openpyxl import Workbook

import regression as rg
import lstm as lstm
import Fibonacci as fib
import analysis as ays

# GUI CODE BELOW#

file_location = "a"

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    #function to check internet conectivity by pinging Google's DNS server
    def internet_check(self, host="8.8.8.8", port=53, timeout=3):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            #print(ex)
            #messagebox.showerror("Error", "No internet connectivity. Please check your network settings")
            return False

    def show_error(self, *args):
        error = traceback.format_exception(*args)
        #messagebox.showerror('Exception', error)

        title = 'Traceback Error'
        message = "An error has occurred: '{}'.".format(error)
        detail = traceback.format_exc()

        TopErrorWindow(title, message, detail)

    tk.Tk.report_callback_exception = show_error

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()

        self._frame = new_frame
        self._frame.grid()

        #internet connectivity check
        if self.internet_check() == 0:
            messagebox.showerror("Error", "No internet connectivity. Please check your network settings")

class StartPage(tk.Frame):
       
    #need to change to relative path
    logo_img = "/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/Source/assets/futuremetric.png" 
    logo_img_resized = None

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #master window title
        master.title("FutureMetric 2020")

        #create canvas
        canvas = tk.Canvas(self, width=250, height=290)
        canvas.grid(row=0, column=0)

        #open logo
        self.logo_img = Image.open(self.logo_img)
        #resize logo
        self.logo_img = self.logo_img.resize((245, 285), Image.ANTIALIAS)
        #open logo with PhotoImage
        self.logo_img_resized = ImageTk.PhotoImage(self.logo_img)
        #load logo into canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=self.logo_img_resized)

        #label
        tk.Label(self, text="Stock markets can be very volatile.\n As a result, there are no consistent patterns "
                    "that makes it possible to model stock prices to near perfection to avoid bad markets.\n "
                    "The goal of this application is to provide an additional tool for investors to use "
                    "when deciding whether to invest or not.").grid(row=0, column=1)

        #buttons
        tk.Button(self, text="LSTM", command=lambda: master.switch_frame(LSTM)).grid(row=1, column=1)
        tk.Button(self, text="Regression", command=lambda: master.switch_frame(Regression)).grid(row=2, column=1)
        tk.Button(self, text="Fibonacci", command=lambda: master.switch_frame(Fibonacci)).grid(row=3, column=1)
        tk.Button(self, text="Analysis", command=lambda: master.switch_frame(Graphing)).grid(row=4, column=1)
        #tk.Button(self, text="License", command=lambda: master.switch_frame(License)).grid(row=5, column=1)

        #menubar
        menubar = tk.Menu(master)
        helpmenu = tk.Menu(master, tearoff=0)
        helpmenu.add_command(label="License", command=lambda: master.switch_frame(License))
        menubar.add_cascade(label="Help", menu=helpmenu)

        master.config(menu=menubar)

class LSTM(tk.Frame):

    compile = lstm.Compile()

    def export_excel(self):
        #global file_location
        file_location = filedialog.asksaveasfilename(defaultextension='.xlsx')

        lstm.forecast.to_excel(file_location, index = False, header=True)

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #available stocks list
        stocks_list = ["AMD", "PFE", "RYCEY"]

        selected_stock = tk.StringVar(self)
        selected_stock.set(stocks_list[0])

        #dropdown with stocks_list
        opt = tk.OptionMenu(self,  selected_stock, *stocks_list)
        opt.config(width=20, font=('Helvetica', 12))
        opt.grid(row=3, column=1)

        #select stock code' text
        tk.Label(self, text="Select stock code").grid(row=3, column=0)

        #function to get selected stock and generate predictions
        def compile_predictions():
            #global selected_stock_var
            lstm.selected_stock_var = selected_stock.get()
            self.compile.compile_predictions_lstm()

        #button to run compile_predictions function to generate predictions
        compile_pred = tk.Button(self, text="Graph data", command=lambda : compile_predictions())
        compile_pred.grid(row=5, column=1)

        #export to excel
        show_graph = tk.Button(self, text="Export", command=lambda: self.export_excel())
        show_graph.grid(row=6, column=1)

        #button to go back to home screen
        tk.Button(self, text="Home", command=lambda: master.switch_frame(StartPage)).grid(row=7, column=1)

class Regression(tk.Frame):

    compile = rg.Compile()
    e_stock_code = None
    rg_regression = None


    def export_excel(self):
        #global file_location
        file_location = filedialog.asksaveasfilename(defaultextension='.xlsx') #filedialog.askdirectory()
        rg.svm_df.to_excel(file_location, index = False, header=True)

    def compile_regression(self):

        # run regression code
        self.compile.compile_predictions_regression(self.e_stock_code.get())

        # # display model confidence level
        # self.rg_regression.configure("Confidence Level " + str(rg.confidence) + "%")

        # show confidence
        #self.rg_regression = tk.Label(self, text="Confidence Level " + str(rg.confidence) + "%").grid(row=4, column=2)

        # show table
        # self.show_table()


    def __init__(self, master):
        tk.Frame.__init__(self, master)

        #enter stock code label
        tk.Label(self, text="Enter stock code").grid(row=1, column=0)
        self.e_stock_code = tk.Entry(self)
        self.e_stock_code.grid(row=1, column=1)

        #show graph
        show_graph = tk.Button(self, text="Graph data", command=lambda: self.compile_regression())
        show_graph.grid(row=4, column=1)

        #export to excel
        show_graph = tk.Button(self, text="Export", command=lambda: self.export_excel())
        show_graph.grid(row=5, column=1)

        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold"))
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage))

        #button to go back to home screen
        tk.Button(self, text="Home", command=lambda: master.switch_frame(StartPage)).grid(row=7, column=1)

class Fibonacci(tk.Frame):

    compile = fib.Compile()

    def __init__(self, master):
        tk.Frame.__init__(self, master)


        # enter stock code label
        tk.Label(self, text="Enter stock code").grid(row=1, column=0)
        stock_code = tk.Entry(self)
        stock_code.grid(row=1, column=1)
        # e_stock_code = e_stock_code.get()

        # enter end date label
        tk.Label(self, text="Enter end date").grid(row=2, column=0)
        end_date = tk.Entry(self)
        end_date.grid(row=2, column=1)

        def compile_fib():
            fib.stock_code = stock_code.get()
            fib.end_date = end_date.get()
            self.compile.compile_fibonacci()

        # show graph
        show_graph = tk.Button(self, text="Graph data", command=lambda: compile_fib())
        show_graph.grid(row=4, column=1)

        #button to go back to home screen
        tk.Button(self, text="Home", command=lambda: master.switch_frame(StartPage)).grid(row=5, column=1)

class Graphing(tk.Frame):

    compile = ays.Compile()

    e_stock_code = None
    e_start_date = None
    e_end_date = None
    period = None

    bb_check = None
    roi_check = None
    atr_check = None
    will_r_check = None

    def compile_analysis(self):

        #get and store user entered values
        ays.stock_code = self.e_stock_code.get()
        ays.start_date = self.e_start_date.get()
        ays.end_date = self.e_end_date.get()
        ays.atr = self.atr_check.get()

        #store period
        ays.period = int(self.period.get())

        #get and store if checkboxes are true or false
        ays.bb = self.bb_check.get()
        ays.roi = self.roi_check.get()
        ays.will_r = self.will_r_check.get()

        #compile
        self.compile.compile_analysis()

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # enter stock code label
        tk.Label(self, text="Enter stock code").grid(row=1, column=0)
        self.e_stock_code = tk.Entry(self)
        self.e_stock_code.grid(row=1, column=1)

        # enter start date label
        tk.Label(self, text="Enter start date").grid(row=2, column=0)
        self.e_start_date = tk.Entry(self)
        self.e_start_date.grid(row=2, column=1)

        # enter end date label
        tk.Label(self, text="Enter end date").grid(row=3, column=0)
        self.e_end_date = tk.Entry(self)
        self.e_end_date.grid(row=3, column=1)

        #enter period label
        tk.Label(self, text="Enter period").grid(row=4, column=0)
        self.period = tk.Entry(self)
        self.period.grid(row=4, column=1)

        #bollinger_bands
        self.bb_check = tk.BooleanVar()
        self.roi_check = tk.BooleanVar()
        self.atr_check = tk.BooleanVar()
        self.will_r_check = tk.BooleanVar()

        #label
        tk.Label(self, text="Graphing analysis").grid(row=1, column=3)

        #checkboxes
        tk.Checkbutton(self, text="Bollinger bands", variable=self.bb_check, onvalue=1, offvalue=0).grid(row=2, column=3, sticky=tk.W)
        tk.Checkbutton(self, text="Rate of Change (ROC)", variable=self.roi_check, onvalue=1, offvalue=0).grid(row=3, column=3, sticky=tk.W)
        tk.Checkbutton(self, text="Average true range (ATR)", variable=self.atr_check, onvalue=1, offvalue=0).grid(row=4, column=3, sticky=tk.W)
        tk.Checkbutton(self, text="Williams %R", variable=self.will_r_check, onvalue=1, offvalue=0).grid(row=5, column=3, sticky=tk.W)


        #function to check if only one checkbox is selected
        def submitHandle():
            any_checked = self.bb_check.get() + self.roi_check.get() + self.atr_check.get() + self.will_r_check.get()

            if any_checked == 1:
                self.compile_analysis()
            else:
                messagebox.showerror("Error", "Please check only one analysis.")

        #show graph
        show_graph = tk.Button(self, text="Graph data", command=lambda: submitHandle())
        show_graph.grid(row=5, column=1)

        #button to go back to home screen
        tk.Button(self, text="Home", command=lambda: master.switch_frame(StartPage)).grid(row=6, column=1)

class License(tk.Frame):


    def __init__(self, master):
        tk.Frame.__init__(self, master)

        tk.Label(self, text="Copyright [2020] Licensed under the Apache License, "
                            "Version 2.0 (the  """ "License" """  ); you may not use this file except in compliance
                            with the License. You may obtain a copy of the License at 
                            \n http://www.apache.org/licenses/LICENSE-2.0 \n \n Unless required by applicable law or 
                            agreed to in writing, software distributed under the License is distributed on an """ "AS " """
                           """ "IS" """ BASIS,WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
                            See the License for the specific language governing permissions and limitations under the 
                            License.""").grid(row=2, column=5)

class TopErrorWindow(tk.Toplevel):
    def __init__(self, title, message, detail):
        #code to “show details” button to a tkinter messagebox from Mike - SMT at Stackoverflow
        #https://stackoverflow.com/questions/49072942/how-can-i-add-a-show-details-button-to-a-tkinter-messagebox

        tk.Toplevel.__init__(self)
        self.details_expanded = False
        self.title(title)
        self.geometry('350x75')
        self.minsize(350, 75)
        self.maxsize(425, 250)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        button_frame = tk.Frame(self)
        button_frame.grid(row=0, column=0, sticky='nsew')
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)

        text_frame = tk.Frame(self)
        text_frame.grid(row=1, column=0, padx=(7, 7), pady=(7, 7), sticky='nsew')
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)

        tk.Label(button_frame, text=message).grid(row=0, column=0, columnspan=2, pady=(7, 7))
        tk.Button(button_frame, text='OK', command=self.destroy).grid(row=1, column=0, sticky='e')
        tk.Button(button_frame, text='Details', command=self.toggle_details).grid(row=1, column=1, sticky='w')

        self.textbox = tk.Text(text_frame, height=6)
        self.textbox.insert('1.0', detail)
        self.textbox.config(state='disabled')
        self.scrollb = tk.Scrollbar(text_frame, command=self.textbox.yview)
        self.textbox.config(yscrollcommand=self.scrollb.set)

    def toggle_details(self):
        if self.details_expanded:
            self.textbox.grid_forget()
            self.scrollb.grid_forget()
            self.geometry('350x75')
            self.details_expanded = False
        else:
            self.textbox.grid(row=0, column=0, sticky='nsew')
            self.scrollb.grid(row=0, column=1, sticky='nsew')
            self.geometry('350x160')
            self.details_expanded = True


if __name__ == "__main__":
    app = App()
    app.mainloop()

