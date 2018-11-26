from tkinter import *
from AuthenticateServer import *

##def lockAccount():
##    lock=Tk()
##    lock.title("Account Locked")
##    msg="Please reset your password, or contact an Admin"
##    text=Label(lock, text=msg)
##    text.pack()
##    Close=Button(lock, text="Close", command =lock.destroy)
##    Close.pack()
##    lock.resizable(0,0)
##    lock.mainloop()


class Login():
    def __init__(self, master):
        self.master=master
        master.title("Welcome!")
        master.config(background="#babbbc")

##        self.img=PhotoImage(file="illusion.gif",width=200,height=100)
##        self.imgDisplay=Label(master, image=self.img)
##        self.imgDisplay.grid(row=0)
        self.attempts=0

        self.EntryUsr=Text(master, state="normal", width=25, height=1, background="white",highlightbackground="black", highlightthickness=1)
        self.EntryUsr.grid(row=1, column=1, columnspan=1,)

        self.EntryPswd=Text(master, state="normal", width=25, height=1, background="white", highlightbackground="black", highlightthickness=1)
        self.EntryPswd.grid(row=2, column=1, columnspan=1)

        self.userLabel=Label(master, text="Username", background="#babbbc")
        self.userLabel.grid(row=1,column=0)

        self.pswdLabel=Label(master, text="Password", background="#babbbc")
        self.pswdLabel.grid(row=2,column=0)

        self.enter=Button(master, text="Enter", background="#babbbc",width=11, command = lambda: retrieveCredentials(self))
        self.enter.grid(row=3,column=1)

        def sendCredentials(self,usr,pswd):
            authenticate(self,usr,pswd)
            self.attempts+=1
            if(self.attempts==3):
                print("LOCKED")
                #lockAccount()
                
            
            
        def retrieveCredentials(self):
            self.readUsr=self.EntryUsr.get("1.0",'end-1c')
            self.readPswd=self.EntryPswd.get("1.0",'end-1c')
            sendCredentials(self,self.readUsr,self.readPswd)
            ClearDisplay(self)
            
        def ClearDisplay(self):
            self.EntryUsr.delete('1.0',END)
            self.EntryPswd.delete('1.0',END)
            




root=Tk()
root.resizable(0,0)
log=Login(root)
root.mainloop()
