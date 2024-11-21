import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("User Interface for Face Recognition Attendance System ")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_288=tk.Message(root)
        GMessage_288["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=38)
        GMessage_288["font"] = ft
        GMessage_288["fg"] = "#333333"
        GMessage_288["justify"] = "center"
        GMessage_288["text"] = "Face Recognition Camera"
        GMessage_288["relief"] = "raised"
        GMessage_288.place(x=100,y=40,width=370,height=267)

        GButton_566=tk.Button(root)
        GButton_566["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=28)
        GButton_566["font"] = ft
        GButton_566["fg"] = "#000000"
        GButton_566["justify"] = "center"
        GButton_566["text"] = "Mark Attendace "
        GButton_566.place(x=110,y=370,width=376,height=82)
        GButton_566["command"] = self.GButton_566_command

        GCheckBox_665=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=18)
        GCheckBox_665["font"] = ft
        GCheckBox_665["fg"] = "#333333"
        GCheckBox_665["justify"] = "center"
        GCheckBox_665["text"] = ". Elon Musk"
        GCheckBox_665.place(x=430,y=80,width=156,height=30)
        GCheckBox_665["offvalue"] = "0"
        GCheckBox_665["onvalue"] = "1"
        GCheckBox_665["command"] = self.GCheckBox_665_command

        GCheckBox_924=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=18)
        GCheckBox_924["font"] = ft
        GCheckBox_924["fg"] = "#333333"
        GCheckBox_924["justify"] = "center"
        GCheckBox_924["text"] = ". Bill Gates"
        GCheckBox_924.place(x=430,y=120,width=143,height=30)
        GCheckBox_924["offvalue"] = "0"
        GCheckBox_924["onvalue"] = "1"
        GCheckBox_924["command"] = self.GCheckBox_924_command

        GCheckBox_16=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=18)
        GCheckBox_16["font"] = ft
        GCheckBox_16["fg"] = "#333333"
        GCheckBox_16["justify"] = "center"
        GCheckBox_16["text"] = ". Jack Ma"
        GCheckBox_16.place(x=440,y=160,width=106,height=30)
        GCheckBox_16["offvalue"] = "0"
        GCheckBox_16["onvalue"] = "1"
        GCheckBox_16["command"] = self.GCheckBox_16_command

        GMessage_26=tk.Message(root)
        ft = tkFont.Font(family='Times',size=18)
        GMessage_26["font"] = ft
        GMessage_26["fg"] = "#333333"
        GMessage_26["justify"] = "left"
        GMessage_26["text"] = "Attendance Table "
        GMessage_26.place(x=420,y=30,width=205,height=30)

    def GButton_566_command(self):
        print("command")


    def GCheckBox_665_command(self):
        print("command")


    def GCheckBox_924_command(self):
        print("command")


    def GCheckBox_16_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
