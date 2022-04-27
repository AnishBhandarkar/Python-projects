from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import pymysql


def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Patient Management System")

        self.master.geometry("1530x790+0+0")
        # self.master.maxsize(width=1530, height=790)
        # self.master.minsize(width=1530, height=790)
        # self.master.resizable(height=False, width=False)

        self.master.iconbitmap('H3.ico')
        
        self.master.configure(background = 'LightBlue1')
        self.frame = Frame(self.master,bg = 'LightBlue1')
        
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text="  Hospital Patient Management System ", font=('arial', 60, 'bold'), bd=20, bg='Dodgerblue2', fg='navy', relief=RIDGE)
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        #============================Menu========================================================

        menubar = Menu(self.frame)

        helpmenu=Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="1.Login as Admin to access Patient Registration System.")
        helpmenu.add_command(label="2.Login as Manager to access Hospital Management System.")
        helpmenu.add_command(label="3.Login as Doctor to access Patient Record System.")
        helpmenu.add_command(label="4.Enter Password.")
        helpmenu.add_command(label="5.Clck on Login.")
        helpmenu.add_command(label="6.Click on Reset to clear.")
        helpmenu.add_command(label="7.Click Exit to close the system.")

        aboutmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="About", menu=aboutmenu)
        aboutmenu.add_command(label="Developed and managed by :")
        aboutmenu.add_command(label="Anish Bhandarkar")

        self.master.config(menu=menubar)

        #===================================Frames==============================================================================

        self.LoginFrame1 = Frame(self.frame, width=1000, height=300, relief='ridge', bd=22, bg='cyan2')
        self.LoginFrame1.grid(row=1, column=0, pady=20)

        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, relief='ridge', bd=22, bg='cyan3')
        self.LoginFrame2.grid(row=2, column=0, pady=15, padx=300)

        self.LoginFrame3 = Frame(self.frame, width=1000, height=200, relief='ridge', bd=22, bg='cyan4')
        self.LoginFrame3.grid(row=3, column=0, pady=25)

        #===================================Button==============================================================================

        self.btnLogin = Button(self.LoginFrame2, text="Login", width=17, font=('arial', 20, 'bold'),bg='deep sky blue', fg='navy', activebackground='pink1', command=self.Login_System)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.LoginFrame2, text="Reset", width=17, font=('arial', 20, 'bold'),bg='deep sky blue', fg='navy', activebackground='pink1', command=self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.LoginFrame2, text="Exit", width=17, font=('arial', 20, 'bold'),bg='deep sky blue', fg='navy', activebackground='pink1', command=self.Exit)
        self.btnExit.grid(row=0, column=2)

        self.btnRegistration = Button(self.LoginFrame3, text="Patient registration system", bg='coral1', state=DISABLED, command=self.Registration_window, font=('arial', 20, 'bold'))
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.LoginFrame3, text="Hospital management system", bg='coral2', state=DISABLED, command=self.Hospital_window, font=('arial', 20, 'bold'))
        self.btnHospital.grid(row=0, column=1)

        self.btnMedical_report = Button(self.LoginFrame3, text="Patient Medical Report", bg='coral2', state=DISABLED, command=self.Patient_Record_window, font=('arial', 20, 'bold'))
        self.btnMedical_report.grid(row=0, column=2)


        #===================================Username and password==================================================================

        self.lblUsername = Label(self.LoginFrame1, text='Username', fg='blue4', bg='cyan', font=('arial', 30, 'bold'), bd=20)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.LoginFrame1, font=('arial', 30, 'bold'), bd=20, fg='gray26', textvariable=self.Username, width=28)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LoginFrame1, text='Password', fg='blue4', bg='cyan', font=('arial', 30, 'bold'), bd=20)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('arial', 30, 'bold'), bd=20, fg='gray26', show="*", textvariable=self.Password, width=28)
        self.txtPassword.grid(row=1, column=1)

        #======================================Button hover==========================================

        def on_enter_Login(e):
            self.btnLogin.configure(bg='cornflower blue')

        def on_leave_Login(e):
            self.btnLogin.configure(bg='deep sky blue')

        self.btnLogin.bind('<Enter>', on_enter_Login)
        self.btnLogin.bind('<Leave>', on_leave_Login)


        def on_enter_Reset(e):
            self.btnReset.configure(bg='cornflower blue')

        def on_leave_Reset(e):
            self.btnReset.configure(bg='deep sky blue')

        self.btnReset.bind('<Enter>', on_enter_Reset)
        self.btnReset.bind('<Leave>', on_leave_Reset)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='cornflower blue')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='deep sky blue')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

    #=====================================================Button Function===============================================================

    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        #Set username and password here
        if (user == str('Admin')) and (pas == str(1234)):
            tkinter.messagebox.showinfo("Patient Management System", "Logged in Succesfully")
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=DISABLED)
            self.btnMedical_report.config(state=DISABLED)

        elif (user == str('Manager')) and (pas == str(1234)):
            tkinter.messagebox.showinfo("Hospital Management System", "Logged in Succesfully")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=NORMAL)
            self.btnMedical_report.config(state=DISABLED)

        elif (user == str('Doctor')) and (pas == str(1234)):
            tkinter.messagebox.showinfo("Patient Record System", "Logged in Succesfully")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.btnMedical_report.config(state=NORMAL)

        else:
            tkinter.messagebox.showwarning("Hospital Patient Management System", "You have entered invalid login detail!")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.btnMedical_report.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.btnMedical_report.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askyesno("Hospital Patient Management System", "Confirm if you want to exit")
        if self.Exit > 0:
            self.master.destroy()
            return
        
        
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)

    def Patient_Record_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window7(self.newWindow)


#=================================================================================================================================================

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Registration System")
        self.master.geometry("1530x790+0+0")
        self.master.iconbitmap('H3.ico')
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%Y-%m-%d"))

        var2 = StringVar()#Gender
        var6 = StringVar()#problem
        var7 = StringVar()#room number
        var8 = StringVar()#Doctor id
        Pid=StringVar()
        Fname=StringVar()
        Lname=StringVar()
        addr=StringVar()
        Telephone=StringVar()

        #=====================Frame=================================================================================

        MainFrame = Frame(self.master)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=20, width=1530, padx=26, relief=RIDGE, bg='Dodgerblue2')
        TitleFrame.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('arial', 58, 'bold'), text="          Patient Registration System         ", padx=8, fg='navy')
        self.lbltitle.grid()

        #==============LowerFrames==================================================================================
        MemberDetailsFrame = LabelFrame(MainFrame, width=1530, height=700, bd=20, pady=5, relief=RIDGE, bg='DodgerBlue2')
        MemberDetailsFrame.pack(side=TOP)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=1530, height=600, relief=RIDGE, bg='LightBlue1')
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=450, height=600, font=('arial', 12, 'bold'), text='Patient Details', relief=RIDGE, bg='cyan3', fg='navy')
        MembersName_F.pack()

        MembersName_F_1 = LabelFrame(MembersName_F, bd=10, width=450, height=600, font=('arial', 12, 'bold'), relief=RIDGE, bg='cyan3', fg='navy')
        MembersName_F_1.grid(row=0, column=0, sticky=N)
        MembersName_F_2 = LabelFrame(MembersName_F, bd=10, width=450, height=600, font=('arial', 12, 'bold'), relief=RIDGE, bg='cyan3', fg='navy')
        MembersName_F_2.grid(row=0, column=1, sticky=N)

        ButtonFrame = LabelFrame(MainFrame,width=1000, bd=5 ,bg='cyan')
        ButtonFrame.pack(side=BOTTOM)

        #=================================Functions declared===========================================================

        def iExit():
            master.destroy()
            return


        def Reset():
            self.txtPat_id.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtTelephone.delete(0, END)
            var2.set("")
            var6.set("")
            var7.set("")
            var8.set("")
                
        def Ref_No():
                x = random.randint(10000, 90000)
                randomRef = str(x)
                Pid.set('P' + randomRef)

        #===================DB Connecting methods===========================

        def addData():
            if Pid.get() == "" or Fname.get() == "" or Lname.get() == "":
                tkinter.messagebox.showerror("Error","Enter Correct details!")
            else:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
                cur = sqlCon.cursor()
                cur.execute("insert into patient values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    Pid.get(),
                    Fname.get(),
                    Lname.get(),
                    addr.get(),
                    DateofOrder.get(),
                    var2.get(),
                    Telephone.get(),
                    var6.get(),
                    var7.get(),
                    var8.get()
                )
                )
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Patient Registration System", "Record entered succesfully")

        #============================================Widgets==============================================

        self.lblPat_id = Label(MembersName_F_1, font=('arial', 17, 'bold'), text='Patient ID', bd=20, bg='cyan3')
        self.lblPat_id.grid(row=0, column=0, sticky=W, pady=10)
        self.txtPat_id = Entry(MembersName_F_1, font=('arial', 17, 'bold'), bd=11, textvariable=Pid, insertwidth=2)
        self.txtPat_id.grid(row=0, column=1, pady=10, padx=40)

        self.lblFirstname = Label(MembersName_F_1, font=('arial', 17, 'bold'), text='First name', bd=20, bg='cyan3')
        self.lblFirstname.grid(row=1, column=0, sticky=W, pady=10)
        self.txtFirstname = Entry(MembersName_F_1, font=('arial', 17, 'bold'), bd=11, textvariable=Fname, insertwidth=2)
        self.txtFirstname.grid(row=1, column=1, pady=10, padx=40)

        self.lblSurname = Label(MembersName_F_1, font=('arial', 17, 'bold'), text='Last name', bd=20, bg='cyan3')
        self.lblSurname.grid(row=2, column=0, sticky=W, pady=10)
        self.txtSurname = Entry(MembersName_F_1, font=('arial', 17, 'bold'), bd=11, textvariable=Lname, insertwidth=2)
        self.txtSurname.grid(row=2, column=1, pady=10, padx=40)

        self.lbl_gender = Label(MembersName_F_2, font=('arial', 17, 'bold'), text='Gender', bd=19, bg='cyan3')
        self.lbl_gender.grid(row=1, column=2, sticky=W, pady=13)
        self.cbo_gender = ttk.Combobox(MembersName_F_2, textvariable=var2, state='readonly',  font=('arial', 17, 'bold'), width=19)
        self.cbo_gender['value']=('', 'Male', 'Female', 'Others')
        self.cbo_gender.current(0)
        self.cbo_gender.grid(row=1, column=3, pady=13)


        self.lblAddress = Label(MembersName_F_1, font=('arial', 17, 'bold'), text='Address', bd=20, bg='cyan3')
        self.lblAddress.grid(row=3, column=0, sticky=W, pady=10)
        self.txtAddress = Entry(MembersName_F_1, font=('arial', 17, 'bold'), bd=11, textvariable=addr, insertwidth=2)
        self.txtAddress.grid(row=3, column=1, pady=10, padx=40)

        self.lblTelephone = Label(MembersName_F_1, font=('arial', 17, 'bold'), text='Telephone', bd=20, bg='cyan3')
        self.lblTelephone.grid(row=4, column=0, sticky=W, pady=10)
        self.txtTelephone = Entry(MembersName_F_1, font=('arial', 17, 'bold'), bd=11, textvariable=Telephone, insertwidth=2)
        self.txtTelephone.grid(row=4, column=1, pady=10, padx=40)

        self.lblDate = Label(MembersName_F_2, font=('arial', 17, 'bold'), text='Date', bd=20, bg='cyan3')
        self.lblDate.grid(row=0, column=2, sticky=W, pady=10)
        self.txtDate = Entry(MembersName_F_2, font=('arial', 17, 'bold'), bd=11, textvariable=DateofOrder, insertwidth=2)
        self.txtDate.grid(row=0, column=3, pady=10, padx=40)


        self.lblProblem = Label(MembersName_F_2, font=('arial', 17, 'bold'), text='Problem', bd=19, bg='cyan3')
        self.lblProblem.grid(row=2, column=2, sticky=W, pady=10)
        self.cboProblem = ttk.Combobox(MembersName_F_2, textvariable=var6, state='readonly',  font=('arial', 17, 'bold'), width=19)
        self.cboProblem['value']=('', 'Heart', 'Tooth', 'Diabetes', 'Stomach', 'Fever', 'Headache', 'Allergy', 'Asthama', 'Asthama', 'Cancer', 'Infection', 'Kedney', 'Mental', 'Eye', 'Ear', 'Nose', 'Throat', 'Bone', 'Muscle', 'Pregnancy', 'Hair', 'Skin', 'Nail', 'New Born Baby')
        self.cboProblem.current(0)
        self.cboProblem.grid(row=2, column=3, pady=10, padx=15)

        self.lblRoom_id = Label(MembersName_F_2, font=('arial', 17, 'bold'), text='Room Number', bd=19, bg='cyan3')
        self.lblRoom_id.grid(row=3, column=2, sticky=W, pady=10)
        self.cboRoom_id = ttk.Combobox(MembersName_F_2, textvariable=var7, state='readonly',  font=('arial', 17, 'bold'), width=19)
        self.cboRoom_id['value']=('', 'F001','F002','F003','F004','F005','F006','F007','F008','F009','F010','F011','F012','F013','F014','\n', 'S001','S002','S003','S004','S005','S006','S007','S008','S009','S010','S011','S012','S013','S014','\n', 'T001','T002','T003','T004','T005','T006','T007','T008','T009','T010','T011','T012','T013','T014','\n')
        self.cboRoom_id.current(0)
        self.cboRoom_id.grid(row=3, column=3, pady=10)

        self.lblDoctor_id = Label(MembersName_F_2, font=('arial', 17, 'bold'), text='Doctor ID', bd=19, bg='cyan3')
        self.lblDoctor_id.grid(row=4, column=2, sticky=W, pady=10)
        self.cboDoctor_id = ttk.Combobox(MembersName_F_2, textvariable=var8, state='readonly',  font=('arial', 17, 'bold'), width=19)
        self.cboDoctor_id['value']=('', 'CARD001', 'CARD002', 'CARD003', '\n', 'DENT001', 'DENT002', '\n', 'DIAB001', 'DIAB002', 'DIAB003', '\n','GAST001','GAST002','GAST003', '\n','IMUN001', 'IMUN002', 'IMUN003', '\n', 'INFC001','INFC002', '\n', 'GMED001','GMED002','GMED003', '\n', 'ONCO001','ONCO002','ONCO003','ONCO004', '\n','NEPR001','NEPR002','NEPR003', '\n','NEUR001','NEUR002','NEUR003', '\n', 'OPTH001','OPTH002', 'OPTH003', '\n','ORTH001','ORTH002', '\n', 'GYNA001','GYNA002', '\n','DERM001','DERM002', '\n', 'ENTS001','ENTS002', '\n', 'NEON001','NEON002')
        self.cboDoctor_id.current(0)
        self.cboDoctor_id.grid(row=4, column=3, pady=10)


        #========================Buttons=================================================================

        self.btnReceipt= Button(ButtonFrame, font=('arial', 16, 'bold'), text="NEW", bd=4,relief=RAISED,
                     padx=24, width=18, height=2, command=Ref_No, bg='medium purple')
        self.btnReceipt.grid(row=0, column=0)

        self.btnAddNew = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Register", bd=4,relief=RAISED,
                     padx=24, width=18, height=2, command=addData, bg='medium purple')
        self.btnAddNew.grid(row=0, column=1, padx=1)

        self.btnReset = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Clear", bd=4,relief=RAISED,
                             padx=24, width=18, height=2, command=Reset, bg='medium purple')
        self.btnReset.grid(row=0, column=2, padx=1)

        self.btnExit = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Exit", bd=4,relief=RAISED,
                             padx=24, width=18, height=2, command=iExit, bg='medium purple')
        self.btnExit.grid(row=0, column=3, padx=1)

        self.btnView = Button(ButtonFrame, font=('arial', 16, 'bold'), text="View\nRecords", bd=4,relief=RAISED,
                             padx=24, width=18, height=2, command=self.Pat_db_view_window, bg='medium purple')
        self.btnView.grid(row=0, column=4, padx=1)

        #======================================Button hover==========================================

        def on_enter_Receipt(e):
            self.btnReceipt.configure(bg='turquoise')

        def on_leave_Receipt(e):
            self.btnReceipt.configure(bg='medium purple')

        self.btnReceipt.bind('<Enter>', on_enter_Receipt)
        self.btnReceipt.bind('<Leave>', on_leave_Receipt)


        def on_enter_Reset(e):
            self.btnReset.configure(bg='turquoise')

        def on_leave_Reset(e):
            self.btnReset.configure(bg='medium purple')

        self.btnReset.bind('<Enter>', on_enter_Reset)
        self.btnReset.bind('<Leave>', on_leave_Reset)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='turquoise')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='medium purple')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

        def on_enter_AddNew(e):
            self.btnAddNew.configure(bg='turquoise')

        def on_leave_AddNew(e):
            self.btnAddNew.configure(bg='medium purple')

        self.btnAddNew.bind('<Enter>', on_enter_AddNew)
        self.btnAddNew.bind('<Leave>', on_leave_AddNew)


        def on_enter_View(e):
            self.btnView.configure(bg='purple', fg='white')

        def on_leave_View(e):
            self.btnView.configure(bg='medium purple', fg='black')

        self.btnView.bind('<Enter>', on_enter_View)
        self.btnView.bind('<Leave>', on_leave_View)

    def Pat_db_view_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)


#=================================================================================================================================================


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry("1530x790+0+0")
        self.master.iconbitmap('H3.ico')

        #============================Frames==============
        MainFrame = Frame(self.master, padx=2)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=18, width=1530, height=120, padx=2, relief=RIDGE, bg='Dodgerblue2')
        TitleFrame.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('arial', 58, 'bold'), text="          Hospital Management System         ", fg='navy')
        self.lbltitle.grid(row=0, column=0)

        DateofToday=StringVar()
        DateofToday.set(time.strftime("%d/%m/%Y"))
        TimeofToday=StringVar()
        TimeofToday.set(time.strftime("%H:%M"))

        #=========================Background Image==============
        self.img = PhotoImage(file='H9.png')
        label = Label(self.master, image=self.img)
        label.place(x = 0, y = 130)

        #=====================================Functions===================================
        def iExit():
            master.destroy()
            return

        #===================================Buttons===========================
        self.btnHosp_db= Button(self.master, font=('arial', 16, 'bold'), text="View\nHospital Database", bd=12,relief=RIDGE,
                     padx=24, width=18, height=2,  bg='medium purple', command=self.Hosp_db_view_window)
        self.btnHosp_db.place(x=250, y=280)

        self.btnDoct_db = Button(self.master, font=('arial', 16, 'bold'), text="View\nDoctor Database", bd=12,relief=RIDGE,
                     padx=24, width=18, height=2, bg='medium purple', command=self.Doct_db_view_window)
        self.btnDoct_db.place(x=1000, y=280)

        self.btnPat_db = Button(self.master, font=('arial', 16, 'bold'), text="View\nPatient Database", bd=12,relief=RIDGE,
                             padx=24, width=18, height=2, bg='medium purple', command=self.Pat_db_view_window)
        self.btnPat_db.place(x=250, y=580)

        self.btnPat_rec = Button(self.master, font=('arial', 16, 'bold'), text="View\nPatient Records", bd=12,relief=RIDGE,
                             padx=24, width=18, height=2, bg='medium purple', command=self.Rec_db_view_window)
        self.btnPat_rec.place(x=1000, y=580)

        self.btnExit = Button(self.master, font=('arial', 16, 'bold'), text="Exit", bd=12,relief=RIDGE,
                             padx=24, width=18, height=2, command=iExit, bg='medium purple')
        self.btnExit.place(x=620, y=700)

        self.txtDate = Entry(self.master, font=('arial', 15, 'bold'), bd=11, textvariable=DateofToday, insertwidth=2)
        self.txtDate.place(x=0, y=130)

        self.txtTime = Entry(self.master, font=('arial', 15, 'bold'), bd=11, textvariable=TimeofToday, insertwidth=2)
        self.txtTime.place(x=1287, y=130)


        #===========================================Button hover====================================

        def on_enter_Hosp_db(e):
            self.btnHosp_db.configure(bg='turquoise')

        def on_leave_Hosp_db(e):
            self.btnHosp_db.configure(bg='medium purple')

        self.btnHosp_db.bind('<Enter>', on_enter_Hosp_db)
        self.btnHosp_db.bind('<Leave>', on_leave_Hosp_db)


        def on_enter_Doct_db(e):
            self.btnDoct_db.configure(bg='turquoise')

        def on_leave_Doct_db(e):
            self.btnDoct_db.configure(bg='medium purple')

        self.btnDoct_db.bind('<Enter>', on_enter_Doct_db)
        self.btnDoct_db.bind('<Leave>', on_leave_Doct_db)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='turquoise')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='medium purple')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

        def on_enter_Pat_db(e):
            self.btnPat_db.configure(bg='turquoise')

        def on_leave_Pat_db(e):
            self.btnPat_db.configure(bg='medium purple')

        self.btnPat_db.bind('<Enter>', on_enter_Pat_db)
        self.btnPat_db.bind('<Leave>', on_leave_Pat_db)

        def on_enter_Pat_rec(e):
            self.btnPat_rec.configure(bg='turquoise')

        def on_leave_Pat_rec(e):
            self.btnPat_rec.configure(bg='medium purple')

        self.btnPat_rec.bind('<Enter>', on_enter_Pat_rec)
        self.btnPat_rec.bind('<Leave>', on_leave_Pat_rec)


    #==================Window functions==================
    def Pat_db_view_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)

    def Hosp_db_view_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.newWindow)

    def Doct_db_view_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window6(self.newWindow)

    def Rec_db_view_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window7(self.newWindow)
        


#=================================================================================================================================================

class Window4:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Database")
        self.master.geometry("1530x790+0+0")
        self.master.iconbitmap('H3.ico')
        self.frame = Frame(self.master)

        MainFrame = Frame(self.master)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=20, width=1530, padx=2, relief=RIDGE, bg='navy')
        TitleFrame.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('arial', 58, 'bold'), text="\t       Patient Database\t    ", padx=8, fg='navy', bg = 'cyan')
        self.lbltitle.grid()

        MemberDetailsFrame = LabelFrame(MainFrame, width=1530, height=700, bd=20, pady=5, relief=RIDGE, bg='navy')
        MemberDetailsFrame.pack(side=TOP)
        
        Receipt_Frame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_Frame.pack(side=LEFT)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_ButtonFrame.pack(side=RIGHT)

        ButtonFrame = LabelFrame(MainFrame,width=1000)
        ButtonFrame.pack(side=BOTTOM)


        DateofOrder=StringVar()
        gender = StringVar()
        problem = StringVar()
        Room_no = StringVar()
        Doc_id = StringVar()
        Pid=StringVar()
        Fname=StringVar()
        Lname=StringVar()
        addr=StringVar()
        Telephone=StringVar()

         #===================DB Connecting methods===========================

        def iExit():
            master.destroy()
            return


        def Reset():
            self.txtPat_id.delete(0, END)
            self.txtFname.delete(0, END)
            self.txtLname.delete(0, END)
            self.txtPhno.delete(0, END)
            self.txtProblem.delete(0, END)
            self.txtRoom_num.delete(0, END)
            self.txtDoc_id.delete(0, END)
            self.patient_records.delete(*self.patient_records.get_children())


        def DisplayData():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("select PID, FNAME, LNAME, PHNO, PROBLEM, ROOM_NUM, DID from patient")
            result = cur.fetchall()
            if len(result) != 0:
                self.patient_records.delete(
                    *self.patient_records.get_children())
                for row in result:
                    self.patient_records.insert('', END, values=row)
            sqlCon.commit()
            sqlCon.close()

        def view():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("SELECT * FROM GET_CURRENT_DATE_PATIENT")
            result = cur.fetchall()
            if len(result) != 0:
                self.patient_records.delete(
                    *self.patient_records.get_children())
                for row in result:
                    self.patient_records.insert('', END, values=row)
            sqlCon.commit()
            sqlCon.close()


        def Stored_procedure():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("CALL GET_CURRENT_MONTH_PATIENT()")
            result = cur.fetchall()
            if len(result) != 0:
                self.patient_records.delete(
                    *self.patient_records.get_children())
                for row in result:
                    self.patient_records.insert('', END, values=row)
            sqlCon.commit()
            sqlCon.close()

        
        def patientInfo(ev):
            viewInfo = self.patient_records.focus()
            learnerData = self.patient_records.item(viewInfo)
            row = learnerData['values']
            Pid.set(row[0])
            Fname.set(row[1])
            Lname.set(row[2])
            Telephone.set(row[3])
            problem.set(row[4])
            Room_no.set(row[5])
            Doc_id.set(row[6])

        def deleteDB():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("delete from patient where PID=%s", Pid.get())
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Patient Database", "Record deleted succesfully")

        def searchDB():
            try:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
                cur = sqlCon.cursor()
                cur.execute("select * from patient where PID='%s'" % Pid.get())
                row = cur.fetchone()
                Pid.set(row[0])
                Fname.set(row[1])
                Lname.set(row[2])
                addr.set(row[3])
                DateofOrder.set(row[4])
                gender.set(row[5])
                Telephone.set(row[6])
                problem.set(row[7])
                Room_no.set(row[8])
                Doc_id.set(row[9])
                sqlCon.commit()
            except:
                tkinter.messagebox.showwarning(
                    "Patient Database", "No Record found")
                Reset()

            sqlCon.close()

        def update():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("update patient set FNAME=%s, LNAME=%s, PADDR=%s, PROBLEM=%s, ROOM_NUM=%s, DID=%s where PID=%s", (
                Fname.get(),
                Lname.get(),
                Telephone.get(),
                problem.get(),
                Room_no.get(),
                Doc_id.get(),
                Pid.get()
            )
            )
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Doctor Database", "Record updated succesfully")

        #===============================Treeview===============================

        scroll_y = Scrollbar(Receipt_Frame, orient=VERTICAL)

        self.patient_records = ttk.Treeview(Receipt_Frame,  height=24, columns=(
            "PID", "FNAME", "LNAME", "PHNO", "PROBLEM","ROOM_NUM", "DID"), yscrollcommand=scroll_y.set)


        #Adding color, font to treeview
        ttk.Style().configure("Treeview", background='PaleGreen1', foreground='blue2',font=('Courier', 15, 'bold'))

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.patient_records.yview)

        self.patient_records.heading("PID", text="ID")
        self.patient_records.heading("FNAME", text="First name")
        self.patient_records.heading("LNAME", text="Lastname")
        # self.patient_records.heading("PADDR", text="Address")
        # self.patient_records.heading("DATE_R", text="Date")
        # self.patient_records.heading("GENDER", text="Gender")
        self.patient_records.heading("PHNO", text="Telephone")
        self.patient_records.heading("PROBLEM", text="Problem")
        self.patient_records.heading("ROOM_NUM", text="Room Number")
        self.patient_records.heading("DID", text="Doctor ID")

        self.patient_records['show'] = 'headings'


        self.patient_records.column("PID", width=120)
        self.patient_records.column("FNAME", width=150)
        self.patient_records.column("LNAME", width=180)
        # self.patient_records.column("PADDR", width=180)
        # self.patient_records.column("DATE_R",width=120)
        # self.patient_records.column("GENDER",width=120)
        self.patient_records.column("PHNO", width=180)
        self.patient_records.column("PROBLEM", width=180)
        self.patient_records.column("ROOM_NUM", width=120)
        self.patient_records.column("DID", width=125)

        self.patient_records.pack(fill=BOTH, expand=1)
        self.patient_records.bind("<ButtonRelease-1>", patientInfo)


        #=============================  Buttons====================================

        self.btnDisplay = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Display", bd=7,relief=RAISED,
                                pady=1, padx=24, width=10, height=2, command=DisplayData, bg='medium purple')
        self.btnDisplay.grid(row=0, column=0)

        self.btnDelete = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Delete", bd=7,relief=RAISED,
                                pady=1, padx=24, width=10, height=2, command=deleteDB, bg='medium purple')
        self.btnDelete.grid(row=0, column=1)

        self.btnSearch = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Search", bd=7,relief=RAISED,
                                pady=1, padx=24, width=10, height=2, command=searchDB, bg='medium purple')
        self.btnSearch.grid(row=0, column=2)

        self.btnUpdate = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Update", bd=7,relief=RAISED,
                                pady=1, padx=24, width=10, height=2, command=update, bg='medium purple')
        self.btnUpdate.grid(row=0, column=3)

        self.btnReset = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Reset", bd=7,relief=RAISED,
                            pady=1, padx=24, width=10, height=2, command=Reset, bg='medium purple')
        self.btnReset.grid(row=0, column=4)

        self.btnExit = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Exit", bd=7,relief=RAISED,
                            pady=1, padx=24, width=10, height=2, command=iExit, bg='medium purple')
        self.btnExit.grid(row=0, column=5)

        self.btnView = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Get Today's\nPatient", bd=7,relief=RAISED,
                            pady=1, padx=24, width=9, height=2, command=view, bg='medium purple')
        self.btnView.grid(row=0, column=6)

        self.btnSt_proc = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Get this\nmonth's Patient", bd=7,relief=RAISED,
                            pady=1, padx=24, width=8, height=2, command=Stored_procedure, bg='medium purple')
        self.btnSt_proc.grid(row=0, column=7)

        

        #==========================Button hover ================================

        
        def on_enter_View(e):
            self.btnView.configure(bg='turquoise')

        def on_leave_View(e):
            self.btnView.configure(bg='medium purple')

        self.btnView.bind('<Enter>', on_enter_View)
        self.btnView.bind('<Leave>', on_leave_View)

        def on_enter_St_proc(e):
            self.btnSt_proc.configure(bg='turquoise')

        def on_leave_St_proc(e):
            self.btnSt_proc.configure(bg='medium purple')

        self.btnSt_proc.bind('<Enter>', on_enter_St_proc)
        self.btnSt_proc.bind('<Leave>', on_leave_St_proc)


        def on_enter_Display(e):
            self.btnDisplay.configure(bg='turquoise')

        def on_leave_Display(e):
            self.btnDisplay.configure(bg='medium purple')

        self.btnDisplay.bind('<Enter>', on_enter_Display)
        self.btnDisplay.bind('<Leave>', on_leave_Display)

        def on_enter_Delete(e):
            self.btnDelete.configure(bg='turquoise')

        def on_leave_Delete(e):
            self.btnDelete.configure(bg='medium purple')

        self.btnDelete.bind('<Enter>', on_enter_Delete)
        self.btnDelete.bind('<Leave>', on_leave_Delete)


        def on_enter_Search(e):
            self.btnSearch.configure(bg='turquoise')

        def on_leave_Search(e):
            self.btnSearch.configure(bg='medium purple')

        self.btnSearch.bind('<Enter>', on_enter_Search)
        self.btnSearch.bind('<Leave>', on_leave_Search)

        def on_enter_Update(e):
            self.btnUpdate.configure(bg='turquoise')

        def on_leave_Update(e):
            self.btnUpdate.configure(bg='medium purple')

        self.btnUpdate.bind('<Enter>', on_enter_Update)
        self.btnUpdate.bind('<Leave>', on_leave_Update)

        def on_enter_Reset(e):
            self.btnReset.configure(bg='turquoise')

        def on_leave_Reset(e):
            self.btnReset.configure(bg='medium purple')

        self.btnReset.bind('<Enter>', on_enter_Reset)
        self.btnReset.bind('<Leave>', on_leave_Reset)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='turquoise')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='medium purple')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

        #================================Frames==================================
        self.lblPat_id = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Patient ID', bd=5, bg='LightBlue1', fg='navy')
        self.lblPat_id.grid(row=0, column=0, sticky=W, pady=10)
        self.txtPat_id = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Pid, insertwidth=2, width=25)
        self.txtPat_id.grid(row=0, column=1, pady=15)

        self.lblFname = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='First name', bd=5, bg='LightBlue1', fg='navy')
        self.lblFname.grid(row=1, column=0, sticky=W,pady=10)
        self.txtFname = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Fname, insertwidth=2, width=25)
        self.txtFname.grid(row=1, column=1, pady=15)

        self.lblLname = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Last name', bd=5, bg='LightBlue1', fg='navy')
        self.lblLname.grid(row=2, column=0, sticky=W, pady=10)
        self.txtLname = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Lname, insertwidth=2, width=25)
        self.txtLname.grid(row=2, column=1, pady=15)

        self.lblPhno = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Phone', bd=5, bg='LightBlue1', fg='navy')
        self.lblPhno.grid(row=3, column=0, sticky=W, pady=10)
        self.txtPhno = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Telephone, insertwidth=2, width=25)
        self.txtPhno.grid(row=3, column=1, pady=15)

        self.lblProblem = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Problem', bd=5, bg='LightBlue1', fg='navy')
        self.lblProblem.grid(row=8, column=0, sticky=W, pady=10)
        self.txtProblem = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=problem, insertwidth=2, width=25)
        self.txtProblem.grid(row=8, column=1, pady=15)

        self.lblRoom_num = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Room number', bd=5, bg='LightBlue1', fg='navy')
        self.lblRoom_num.grid(row=9, column=0, sticky=W, pady=10)
        self.txtRoom_num = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Room_no, insertwidth=2, width=25)
        self.txtRoom_num.grid(row=9, column=1, pady=15)

        self.lblDoc_id = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Doctor id', bd=5, bg='LightBlue1', fg='navy')
        self.lblDoc_id.grid(row=10, column=0, sticky=W, pady=10)
        self.txtDoc_id = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Doc_id, insertwidth=2, width=25)
        self.txtDoc_id.grid(row=10, column=1, pady=15)


#===============================================================================================================================

class Window5:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Database")
        self.master.geometry("1530x790+0+0")
        self.master.iconbitmap('H3.ico')
        self.frame = Frame(self.master)

        MainFrame = Frame(self.master)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=20, width=1530, padx=3, relief=RIDGE, bg='tomato')
        TitleFrame.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('arial', 58, 'bold'), text="\t   Hospital Datbase\t    ", padx=12, fg='navy', bg='peach puff')
        self.lbltitle.grid()

        MemberDetailsFrame = LabelFrame(MainFrame, width=1530, height=700, bd=20, pady=5, relief=RIDGE, bg='tomato')
        MemberDetailsFrame.pack(side=TOP)
        
        Receipt_Frame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_Frame.pack(side=LEFT)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_ButtonFrame.pack(side=RIGHT)

        ButtonFrame = LabelFrame(MainFrame,width=1530)
        ButtonFrame.pack(side=BOTTOM)

        Room_no=StringVar()
        Room_loc=StringVar()
        Room_type=StringVar()

        #==================================Functions================================

        def iExit():
            master.destroy()
            return
        
        def Clear():
            self.txtRoom_NUM.delete(0, END)
            self.txtRoom_Loc.delete(0, END)
            self.txtRoom_type.delete(0, END)
            self.Hospital_db.delete(*self.Hospital_db.get_children())
        
        def DisplayData():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("select * from hospital")
            result = cur.fetchall()
            if len(result) != 0:
                self.Hospital_db.delete(
                    *self.Hospital_db.get_children())
                for row in result:
                    self.Hospital_db.insert('', END, values=row)
            sqlCon.commit()
            sqlCon.close()


        def searchDB():
            try:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
                cur = sqlCon.cursor()
                cur.execute("select * from hospital where ROOM_NUM='%s'" % Room_no.get())
                row = cur.fetchone()
                Room_no.set(row[0])
                Room_loc.set(row[1])
                Room_type.set(row[2])
                # tkinter.messagebox.showinfo("Hospital Database", "Record found")
                sqlCon.commit()
            except:
                tkinter.messagebox.showwarning(
                    "Hospital Database", "No Record found")
                Clear()

            sqlCon.close()


        def HospitalInfo(ev):
            viewInfo = self.Hospital_db.focus()
            learnerData = self.Hospital_db.item(viewInfo)
            row = learnerData['values']
            Room_no.set(row[0])
            Room_loc.set(row[1])
            Room_type.set(row[2])

        #===============================Treeview===============================

        scroll_y = Scrollbar(Receipt_Frame, orient=VERTICAL)

        self.Hospital_db = ttk.Treeview(Receipt_Frame,  height=23, columns=(
            "ROOM_NUM", "ROOM_LOC", "ROOM_TYPE"), yscrollcommand=scroll_y.set)

        #Adding color, font to treeview
        ttk.Style().configure("Treeview", background='LightBlue1', foreground='black',font=('Courier', 15, 'bold'))

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.Hospital_db.yview)

        self.Hospital_db.heading("ROOM_NUM", text="Room Number")
        self.Hospital_db.heading("ROOM_LOC", text="Room Location")
        self.Hospital_db.heading("ROOM_TYPE", text="Room Type")

        self.Hospital_db['show'] = 'headings'

        self.Hospital_db.column("ROOM_NUM", width=310)
        self.Hospital_db.column("ROOM_LOC", width=310)
        self.Hospital_db.column("ROOM_TYPE", width=310)

        self.Hospital_db.pack(fill=BOTH, expand=1)
        self.Hospital_db.bind("<ButtonRelease-1>", HospitalInfo)     

        #=========================================================

        self.lblRoom_NUM = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Room Number', bd=5, bg='LightBlue1')
        self.lblRoom_NUM.grid(row=0, column=0, sticky=W, pady=60, padx=30)
        self.txtRoom_NUM = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Room_no, insertwidth=2, width=25)
        self.txtRoom_NUM.grid(row=0, column=1, pady=60, padx=30)

        self.lblRoom_Loc = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Room Location', bd=5, bg='LightBlue1')
        self.lblRoom_Loc.grid(row=1, column=0, sticky=W, pady=60, padx=30)
        self.txtRoom_Loc = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Room_loc, insertwidth=2, width=25)
        self.txtRoom_Loc.grid(row=1, column=1, pady=60, padx=30)

        self.lblRoom_type = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Room Type', bd=5, bg='LightBlue1')
        self.lblRoom_type.grid(row=2, column=0, sticky=W, pady=60, padx=30)
        self.txtRoom_type = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Room_type, insertwidth=2, width=25)
        self.txtRoom_type.grid(row=2, column=1, pady=60, padx=30)

        #==============================Buttons==========================

        self.btnDisplay = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Display", bd=12,relief=RAISED,
                                pady=1, padx=24, width=9, height=2, command=DisplayData, bg='medium purple')
        self.btnDisplay.grid(row=0, column=0, padx=40)  

        self.btnSearch = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Search", bd=12,relief=RAISED,
                                pady=1, padx=24, width=9, height=2, command=searchDB, bg='medium purple')
        self.btnSearch.grid(row=0, column=1, padx=40) 

        self.btnClear = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Reset", bd=12,relief=RAISED,
                            pady=1, padx=24, width=9, height=2, command=Clear, bg='medium purple', fg='black')
        self.btnClear.grid(row=0, column=2, padx=40)

        self.btnExit = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Exit", bd=12,relief=RAISED,
                            pady=1, padx=24, width=9, height=2, command=iExit, bg='medium purple')
        self.btnExit.grid(row=0, column=3, padx=40)

        #==========================================Button Hover ======================

        def on_enter_Search(e):
            self.btnSearch.configure(bg='turquoise')

        def on_leave_Search(e):
            self.btnSearch.configure(bg='medium purple')

        self.btnSearch.bind('<Enter>', on_enter_Search)
        self.btnSearch.bind('<Leave>', on_leave_Search)

        def on_enter_Clear(e):
            self.btnClear.configure(bg='turquoise')

        def on_leave_Clear(e):
            self.btnClear.configure(bg='medium purple')

        self.btnClear.bind('<Enter>', on_enter_Clear)
        self.btnClear.bind('<Leave>', on_leave_Clear)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='turquoise')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='medium purple')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

        def on_enter_Display(e):
            self.btnDisplay.configure(bg='turquoise')

        def on_leave_Display(e):
            self.btnDisplay.configure(bg='medium purple')

        self.btnDisplay.bind('<Enter>', on_enter_Display)
        self.btnDisplay.bind('<Leave>', on_leave_Display)


#==========================================================================================================================

class Window6:
    def __init__(self, master):
        self.master = master
        self.master.title("Doctor Database")
        self.master.geometry("1530x790+0+0")
        self.master.iconbitmap('H3.ico')
        self.frame = Frame(self.master)

        MainFrame = Frame(self.master)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=20, width=1530, padx=3, relief=RIDGE, bg='dark violet')
        TitleFrame.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('arial', 58, 'bold'), text="\t     Doctor Datbase\t\t    ", padx=12, fg='navy')
        self.lbltitle.grid()

        MemberDetailsFrame = LabelFrame(MainFrame, width=1530, height=700, bd=20, pady=5, relief=RIDGE, bg='dark violet')
        MemberDetailsFrame.pack(side=TOP)
        
        Receipt_Frame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_Frame.pack(side=LEFT)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_ButtonFrame.pack(side=RIGHT)

        ButtonFrame = LabelFrame(MainFrame,width=1000)
        ButtonFrame.pack(side=BOTTOM)

        Doc_id=StringVar()
        Doc_name=StringVar()
        Doc_sal=StringVar()
        domain = StringVar()
        qualif = StringVar()
        Room_no = StringVar()

        #==================================Functions================================

        def iExit():
            master.destroy()
            return
        
        def Clear():
            self.txtDoc_id.delete(0, END)
            self.txtDoc_name.delete(0, END)
            self.txtSalary.delete(0, END)
            self.txtDomain.delete(0, END)
            self.txtQualif.delete(0, END)
            self.txtRoom_num.delete(0, END)
            self.Doctor_db.delete(*self.Doctor_db.get_children())
        
        def DisplayData():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("select * from doctor")
            result = cur.fetchall()
            if len(result) != 0:
                self.Doctor_db.delete(
                    *self.Doctor_db.get_children())
                for row in result:
                    self.Doctor_db.insert('', END, values=row)
            sqlCon.commit()
            sqlCon.close()


        def searchDB():
            try:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
                cur = sqlCon.cursor()
                cur.execute("select * from doctor where DID='%s'" % Doc_id.get())
                row = cur.fetchone()
                Doc_id.set(row[0])
                Doc_name.set(row[1])
                Doc_sal.set(row[2])
                domain.set(row[3])
                qualif.set(row[4])
                Room_no.set(row[5])
                # tkinter.messagebox.showinfo("Hospital Database", "Record found")
                sqlCon.commit()
            except:
                tkinter.messagebox.showwarning(
                    "Doctor Database", "No Record found")
                Clear()

            sqlCon.close()


        def DoctorInfo(ev):
            viewInfo = self.Doctor_db.focus()
            learnerData = self.Doctor_db.item(viewInfo)
            row = learnerData['values']
            Doc_id.set(row[0])
            Doc_name.set(row[1])
            Doc_sal.set(row[2])
            domain.set(row[3])
            qualif.set(row[4])
            Room_no.set(row[5])

        def update():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("update doctor set DNAME=%s, SALARY=%s, DOMAIN=%s, QUALIFICATION=%s, ROOM_NUM=%s where DID=%s", (
                Doc_name.get(),
                Doc_sal.get(),
                domain.get(),
                qualif.get(),
                Room_no.get(),
                Doc_id.get()
            )
            )
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Doctor Database", "Record updated succesfully")

        def deleteDB():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("delete from doctor where DID=%s", Doc_id.get())
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Doctor Database", "Record deleted succesfully")

        #===============================Treeview===============================

        scroll_y = Scrollbar(Receipt_Frame, orient=VERTICAL)

        self.Doctor_db = ttk.Treeview(Receipt_Frame,  height=24, columns=(
            "DID", "DNAME", "SALARY", "DOMAIN", "QUALIFICATION", "ROOM_NUM"), yscrollcommand=scroll_y.set)

        #Adding color, font to treeview
        ttk.Style().configure("Treeview", background='LightBlue1', foreground='black', font=('Courier', 15, 'bold'))

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.Doctor_db.yview)

        self.Doctor_db.heading("DID", text="Doctor ID")
        self.Doctor_db.heading("DNAME", text="Name")
        self.Doctor_db.heading("SALARY", text="Salary")
        self.Doctor_db.heading("DOMAIN", text="Domain")
        self.Doctor_db.heading("QUALIFICATION", text="Qualification")
        self.Doctor_db.heading("ROOM_NUM", text="Room number")

        self.Doctor_db['show'] = 'headings'

        self.Doctor_db.column("DID", width=120)
        self.Doctor_db.column("DNAME", width=276)
        self.Doctor_db.column("SALARY", width=100)
        self.Doctor_db.column("DOMAIN", width=220)
        self.Doctor_db.column("QUALIFICATION", width=180)
        self.Doctor_db.column("ROOM_NUM", width=90)

        self.Doctor_db.pack(fill=BOTH, expand=1)
        self.Doctor_db.bind("<ButtonRelease-1>", DoctorInfo)     

        #=========================================================

        self.lblDoc_id = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Doctor ID', bd=5, bg='LightBlue1')
        self.lblDoc_id.grid(row=0, column=0, sticky=W, pady=27, padx=30)
        self.txtDoc_id = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Doc_id, insertwidth=2, width=25)
        self.txtDoc_id.grid(row=0, column=1, pady=10, padx=5)

        self.lblDoc_name = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Name', bd=5, bg='LightBlue1')
        self.lblDoc_name.grid(row=1, column=0, sticky=W, pady=27, padx=30)
        self.txtDoc_name = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Doc_name, insertwidth=2, width=25)
        self.txtDoc_name.grid(row=1, column=1, pady=10, padx=5)

        self.lblSalary = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Salary', bd=5, bg='LightBlue1')
        self.lblSalary.grid(row=2, column=0, sticky=W, pady=27, padx=30)
        self.txtSalary = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Doc_sal, insertwidth=2, width=25)
        self.txtSalary.grid(row=2, column=1, pady=10, padx=5)

        self.lblDomain = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Domain', bd=5, bg='LightBlue1')
        self.lblDomain.grid(row=3, column=0, sticky=W, pady=27, padx=30)
        self.txtDomain = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=domain, insertwidth=2, width=25)
        self.txtDomain.grid(row=3, column=1, pady=10, padx=5)

        self.lblQualif = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Qualification', bd=5, bg='LightBlue1')
        self.lblQualif.grid(row=4, column=0, sticky=W, pady=27, padx=30)
        self.txtQualif = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=qualif, insertwidth=2, width=25)
        self.txtQualif.grid(row=4, column=1, pady=10, padx=5)

        self.lblRoom_num = Label(Receipt_ButtonFrame, font=('arial', 13, 'bold'), text='Room number', bd=5, bg='LightBlue1')
        self.lblRoom_num.grid(row=5, column=0, sticky=W, pady=27, padx=30)
        self.txtRoom_num = Entry(Receipt_ButtonFrame, font=('arial', 13, 'bold'), bd=11, textvariable=Room_no, insertwidth=2, width=25)
        self.txtRoom_num.grid(row=5, column=1, pady=10, padx=5)

        #==============================Buttons==========================
        
        self.btnDisplay = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Display", bd=12,relief=RAISED,
                                pady=1, padx=24, width=9, height=2, command=DisplayData, bg='medium purple')
        self.btnDisplay.grid(row=0, column=0, padx=30)  

        self.btnSearch = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Search", bd=12,relief=RAISED,
                                pady=1, padx=24, width=9, height=2, command=searchDB, bg='medium purple')
        self.btnSearch.grid(row=0, column=1, padx=30) 

        self.btnUpdate = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Update", bd=12,relief=RAISED,
                                pady=1, padx=24, width=9, height=2, command=update, bg='medium purple')
        self.btnUpdate.grid(row=0, column=2, padx=30) 

        self.btnDelete = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Delete", bd=12,relief=RAISED,
                            pady=1, padx=24, width=9, height=2, command=deleteDB, bg='medium purple')
        self.btnDelete.grid(row=0, column=3, padx=30)

        self.btnClear = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Clear", bd=12,relief=RAISED,
                            pady=1, padx=24, width=9, height=2, command=Clear, bg='medium purple')
        self.btnClear.grid(row=0, column=4, padx=30)

        self.btnExit = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Exit", bd=12,relief=RAISED,
                            pady=1, padx=24, width=9, height=2, command=iExit, bg='medium purple')
        self.btnExit.grid(row=0, column=5, padx=30)

        #==========================================Button Hover ======================

        def on_enter_Search(e):
            self.btnSearch.configure(bg='turquoise')

        def on_leave_Search(e):
            self.btnSearch.configure(bg='medium purple')

        self.btnSearch.bind('<Enter>', on_enter_Search)
        self.btnSearch.bind('<Leave>', on_leave_Search)

        def on_enter_Clear(e):
            self.btnClear.configure(bg='turquoise')

        def on_leave_Clear(e):
            self.btnClear.configure(bg='medium purple')

        self.btnClear.bind('<Enter>', on_enter_Clear)
        self.btnClear.bind('<Leave>', on_leave_Clear)

        def on_enter_Update(e):
            self.btnUpdate.configure(bg='turquoise')

        def on_leave_Update(e):
            self.btnUpdate.configure(bg='medium purple')

        self.btnUpdate.bind('<Enter>', on_enter_Update)
        self.btnUpdate.bind('<Leave>', on_leave_Update)


        def on_enter_Delete(e):
            self.btnDelete.configure(bg='turquoise')

        def on_leave_Delete(e):
            self.btnDelete.configure(bg='medium purple')

        self.btnDelete.bind('<Enter>', on_enter_Delete)
        self.btnDelete.bind('<Leave>', on_leave_Delete)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='turquoise')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='medium purple')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

        def on_enter_Display(e):
            self.btnDisplay.configure(bg='turquoise')

        def on_leave_Display(e):
            self.btnDisplay.configure(bg='medium purple')

        self.btnDisplay.bind('<Enter>', on_enter_Display)
        self.btnDisplay.bind('<Leave>', on_leave_Display)


#==========================================================================================================================

class Window7:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Record")
        self.master.geometry("1530x790+0+0")
        self.master.iconbitmap('H3.ico')

        Rid=StringVar()
        Pid=StringVar()
        Disorder=StringVar()
        Treatment = StringVar()
        DateofExamination=StringVar()
        DateofExamination.set(time.strftime("%d/%m/%Y"))

        #=====================Frame=================================================================================

        MainFrame = Frame(self.master)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=20, width=1530, padx=5, relief=RIDGE, bg='SeaGreen1')
        TitleFrame.pack(side=TOP)

        self.lbltitle = Label(TitleFrame, font=('arial', 58, 'bold'), text="              Patient Record Database            ", padx=11, fg='navy')
        self.lbltitle.grid()

        #==============LowerFrames==================================================================================
        MemberDetailsFrame = LabelFrame(MainFrame, width=1530, height=700, bd=20, pady=5, relief=RIDGE, bg='SeaGreen1')
        MemberDetailsFrame.pack(side=TOP)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=1530, height=600, relief=RIDGE, bg='LightBlue1')
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=450, height=600, font=('arial', 12, 'bold'), text='Patient Record', relief=RIDGE, bg='PaleGreen1', fg='navy')
        MembersName_F.grid(row=0, column=0)

        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=600, relief=RIDGE, bg='LightBlue1')
        Receipt_ButtonFrame.pack(side=RIGHT)

        ButtonFrame = LabelFrame(MainFrame,width=1000, bg='cyan')
        ButtonFrame.pack(side=BOTTOM)

        #=================================Functions declared===========================================================

        def iExit():
            master.destroy()
            return

        def Reset():
            self.txtRid.delete(0, END)
            self.txtPid.delete(0, END)
            self.txtDate_E.delete(0, END)
            Disorder.set("")
            Treatment.set("")
            self.patient_records.delete(*self.patient_records.get_children())
                

        def Ref_No():
                x = random.randint(10000, 90000)
                randomRef = str(x)
                Rid.set('R' + randomRef)


        #===================DB Connecting methods===========================

        def addData():
            if Rid.get() == "" or Pid.get() == "":
                tkinter.messagebox.showerror("Enter Correct details!")
            else:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
                cur = sqlCon.cursor()
                cur.execute("insert into PATIENT_RECORD values(%s, %s, %s, %s, %s)", (
                    Rid.get(),
                    Pid.get(),
                    Disorder.get(),
                    DateofExamination.get(),
                    Treatment.get(),
                )
                )
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Patient Record", "Record entered succesfully")


        def DisplayData():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("select * from PATIENT_RECORD")
            result = cur.fetchall()
            if len(result) != 0:
                self.patient_records.delete(
                    *self.patient_records.get_children())
                for row in result:
                    self.patient_records.insert('', END, values=row)
            sqlCon.commit()
            sqlCon.close()

        
        def Patient_RecordInfo(ev):
            viewInfo = self.patient_records.focus()
            learnerData = self.patient_records.item(viewInfo)
            row = learnerData['values']
            Rid.set(row[0])
            Pid.set(row[1])
            Disorder.set(row[2])
            DateofExamination.set(row[3])
            Treatment.set(row[4])


        def update():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("update PATIENT_RECORD set PID=%s, DISORDER=%s, DATE_E=%s, TREATMENT=%s where RID=%s", (
                Pid.get(),
                Disorder.get(),
                DateofExamination.get(),
                Treatment.get(),
                Rid.get()
            )
            )
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Patient Record", "Record updated succesfully")

        def deleteDB():
            sqlCon = pymysql.connect(
                host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
            cur = sqlCon.cursor()
            cur.execute("delete from PATIENT_RECORD where RID=%s", Rid.get())
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo(
                "Patient Record", "Record deleted succesfully")

        def searchDB():
            try:
                sqlCon = pymysql.connect(
                    host="localhost", user="root", password="8#danish?63M", database="mini_proj_db")
                cur = sqlCon.cursor()
                cur.execute("select * from PATIENT_RECORD where RID='%s'" %
                            Rid.get())
                row = cur.fetchone()
                Rid.set(row[0]),
                Pid.set(row[1]),
                Disorder.set(row[2]),
                DateofExamination.set(row[3]),
                Treatment.set(row[4])
                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo(
                    "Data Entry Form", "No Record found")
                Reset()

            sqlCon.close()


        #============================================Widgets==============================================

        self.lblRid = Label(MembersName_F, font=('arial', 13, 'bold'), text='Record Number', bd=5, bg='PaleGreen1')
        self.lblRid.grid(row=0, column=0, sticky=W, pady=28, padx=20)
        self.txtRid = Entry(MembersName_F, font=('arial', 13, 'bold'), bd=11, textvariable=Rid, insertwidth=2)
        self.txtRid.grid(row=0, column=1, pady=28, padx=20)

        self.lblPid = Label(MembersName_F, font=('arial', 13, 'bold'), text='Patient ID', bd=5, bg='PaleGreen1')
        self.lblPid.grid(row=1, column=0, sticky=W, pady=28, padx=20)
        self.txtPid = Entry(MembersName_F, font=('arial', 13, 'bold'), bd=11, textvariable=Pid, insertwidth=2)
        self.txtPid.grid(row=1, column=1, pady=28, padx=20)

        self.lblDate_E = Label(MembersName_F, font=('arial', 13, 'bold'), text='Date', bd=5, bg='PaleGreen1')
        self.lblDate_E.grid(row=3, column=0, sticky=W, pady=28, padx=20)
        self.txtDate_E = Entry(MembersName_F, font=('arial', 13, 'bold'), bd=11, textvariable=DateofExamination, insertwidth=2)
        self.txtDate_E.grid(row=3, column=1, pady=28, padx=20)


        self.lblDisorder = Label(MembersName_F, font=('arial', 13, 'bold'), text='Disorder', bd=6, bg='PaleGreen1')
        self.lblDisorder.grid(row=4, column=0, sticky=W, pady=28, padx=20)

        self.cboDisorder = ttk.Combobox(MembersName_F, textvariable=Disorder, state='readonly',  font=('arial', 13, 'bold'), width=22)
        self.cboDisorder['value']=('', 'Cardiology', '------------', 'CAD', 'Heart Failure', 'Cardiac Arrest', '---------','Dentist', '---------', 'Toothache','Cavities', 'Crooked Teeth','---------', 'Diabetology', '----------', 'Diabetes', '----------', 'Gastroenterologist', '-----------', 'Stomach Pain', 'Appendicitis', 'Stomach Flu', '------------', 'Immunology', '-----------', 'Allergy', 'Asthama', '----------', 'Infection', '-----------', 'Malaria', 'Dengue', 'STD', '----------', 'General Medicine', '------------', 'Fever', 'cold', 'Cough', 'Headache', '----------', 'Oncologist', '---------', 'Lung Cancer', 'Liver Cancer', 'Blood Cancer', '------------', 'Nephrology', '----------', 'Chronic Keydney disease', 'Keydney Stone', 'Keydney Failure', '-----------', 'Neurology', '-----------', 'Brain Tumor', 'Alzheimer',  'Head Injury', 'Stroke', '-------------', 'Opthamology', '-----------', 'Cataract', 'Glaucoma', 'Amblyopia', 'Low Vision', '-------------', 'Orthopedix', '-----------', 'Lower Back Pain', 'Ankle pain', 'Knee pain', 'Arthritis', '------------', 'Gynecology', '-----------', 'Delivery', 'Endometriosis', 'Uterine fibroids', '-------------', 'Pimples', 'Dry Skin', 'Hairfall', 'Ingrown nails', '-------------', 'ENT', '-----------', 'Breathing Difficulties', 'Nose bleeds', 'Facial Nerve Injuries', 'Hearing Loss', '-------------', 'Neonatology','------------', 'Respiratory disorders', 'Severe infections', 'Heart problems')
        self.cboDisorder.current(0)
        self.cboDisorder.grid(row=4, column=1, pady=28, padx=20)


        self.lblTreatment = Label(MembersName_F, font=('arial', 13, 'bold'), text='Treatment', bd=6, bg='PaleGreen1')
        self.lblTreatment.grid(row=5, column=0, sticky=W, pady=28, padx=20)

        self.cboTreatment = ttk.Combobox(MembersName_F, textvariable=Treatment, state='readonly',  font=('arial', 13, 'bold'), width=22)
        self.cboTreatment['value']=('', 'Surgery', 'Medicine', 'Transplantation')
        self.cboTreatment.current(0)
        self.cboTreatment.grid(row=5, column=1, pady=28, padx=20)



        #===========Table Tree view=============================================================================

        scroll_y = Scrollbar(Receipt_ButtonFrame, orient=VERTICAL)

        self.patient_records = ttk.Treeview(Receipt_ButtonFrame, height=24, columns=(
            "RID", "PID", "DISORDER", "DATE_E","TREATMENT"), yscrollcommand=scroll_y.set)

        #Adding color to treeview
        ttk.Style().configure("Treeview", background='paleGreen1', foreground='blue2', font=('Courier', 15, 'bold'))

        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.patient_records.yview)

        self.patient_records.heading("RID", text="Record Number")
        self.patient_records.heading("PID", text="Patient ID")
        self.patient_records.heading("DISORDER", text="Disorder")
        self.patient_records.heading("DATE_E", text="Date")
        self.patient_records.heading("TREATMENT", text="Treatment")

        self.patient_records['show'] = 'headings'

        self.patient_records.column("RID", width=130)
        self.patient_records.column("PID", width=130)
        self.patient_records.column("DISORDER", width=310)
        self.patient_records.column("DATE_E", width=180)
        self.patient_records.column("TREATMENT", width=220)

        self.patient_records.pack(fill=BOTH, expand=1)
        self.patient_records.bind("<ButtonRelease-1>", Patient_RecordInfo)
        
        #========================Buttons=================================================================

        self.btnReceipt= Button(ButtonFrame, font=('arial', 16, 'bold'), text="NEW", bd=7,relief=RAISED,
                    pady=1, padx=24, width=8, height=2, command=Ref_No, bg='pale green')
        self.btnReceipt.grid(row=0, column=0)

        self.btnAddNew = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Insert", bd=7,relief=RAISED,
                    pady=1, padx=24, width=8, height=2, command=addData, bg='pale green')
        self.btnAddNew.grid(row=0, column=1, padx=1)

        self.btnDisplay = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Display", bd=7,relief=RAISED,
                                pady=1, padx=24, width=8, height=2, command=DisplayData, bg='pale green')
        self.btnDisplay.grid(row=0, column=2, padx=1)

        self.btnUpdate = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Update", bd=7,relief=RAISED,
                                pady=1, padx=24, width=8, height=2, command=update, bg='pale green')
        self.btnUpdate.grid(row=0, column=3, padx=1)

        self.btnDelete = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Delete", bd=7,relief=RAISED,
                                pady=1, padx=24, width=8, height=2, command=deleteDB, bg='pale green')
        self.btnDelete.grid(row=0, column=4, padx=1)

        self.btnSearch = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Search", bd=7,relief=RAISED,
                                pady=1, padx=24, width=8, height=2, command=searchDB, bg='pale green')
        self.btnSearch.grid(row=0, column=5, padx=1)

        self.btnReset = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Reset", bd=7,relief=RAISED,
                            pady=1, padx=24, width=8, height=2, command=Reset, bg='pale green')
        self.btnReset.grid(row=0, column=6, padx=1)

        self.btnExit = Button(ButtonFrame, font=('arial', 16, 'bold'), text="Exit", bd=7,relief=RAISED,
                            pady=1, padx=24, width=8, height=2, command=iExit, bg='pale green')
        self.btnExit.grid(row=0, column=7, padx=1)

        self.btnPat_db = Button(ButtonFrame, font=('arial', 16, 'bold'), text="View Patient\nDatabase", bd=7,relief=RAISED,
                     padx=24, width=7, height=2, bg='pale green', command=self.Pat_db_view_window)
        self.btnPat_db.grid(row=0, column=8, padx=1)

        #======================================Button hover==========================================

        def on_enter_Receipt(e):
            self.btnReceipt.configure(bg='turquoise')

        def on_leave_Receipt(e):
            self.btnReceipt.configure(bg='pale green')

        self.btnReceipt.bind('<Enter>', on_enter_Receipt)
        self.btnReceipt.bind('<Leave>', on_leave_Receipt)


        def on_enter_AddNew(e):
            self.btnAddNew.configure(bg='turquoise')

        def on_leave_AddNew(e):
            self.btnAddNew.configure(bg='pale green')

        self.btnAddNew.bind('<Enter>', on_enter_AddNew)
        self.btnAddNew.bind('<Leave>', on_leave_AddNew)


        def on_enter_Display(e):
            self.btnDisplay.configure(bg='turquoise')

        def on_leave_Display(e):
            self.btnDisplay.configure(bg='pale green')

        self.btnDisplay.bind('<Enter>', on_enter_Display)
        self.btnDisplay.bind('<Leave>', on_leave_Display)


        def on_enter_Update(e):
            self.btnUpdate.configure(bg='turquoise')

        def on_leave_Update(e):
            self.btnUpdate.configure(bg='pale green')

        self.btnUpdate.bind('<Enter>', on_enter_Update)
        self.btnUpdate.bind('<Leave>', on_leave_Update)


        def on_enter_Delete(e):
            self.btnDelete.configure(bg='turquoise')

        def on_leave_Delete(e):
            self.btnDelete.configure(bg='pale green')

        self.btnDelete.bind('<Enter>', on_enter_Delete)
        self.btnDelete.bind('<Leave>', on_leave_Delete)


        def on_enter_Search(e):
            self.btnSearch.configure(bg='turquoise')

        def on_leave_Search(e):
            self.btnSearch.configure(bg='pale green')

        self.btnSearch.bind('<Enter>', on_enter_Search)
        self.btnSearch.bind('<Leave>', on_leave_Search)


        def on_enter_Reset(e):
            self.btnReset.configure(bg='turquoise')

        def on_leave_Reset(e):
            self.btnReset.configure(bg='pale green')

        self.btnReset.bind('<Enter>', on_enter_Reset)
        self.btnReset.bind('<Leave>', on_leave_Reset)


        def on_enter_Pat_db(e):
            self.btnPat_db.configure(bg='medium purple', fg='white')

        def on_leave_Pat_db(e):
            self.btnPat_db.configure(bg='pale green', fg='black')

        self.btnPat_db.bind('<Enter>', on_enter_Pat_db)
        self.btnPat_db.bind('<Leave>', on_leave_Pat_db)


        def on_enter_Exit(e):
            self.btnExit.configure(bg='turquoise')

        def on_leave_Exit(e):
            self.btnExit.configure(bg='pale green')

        self.btnExit.bind('<Enter>', on_enter_Exit)
        self.btnExit.bind('<Leave>', on_leave_Exit)

    def Pat_db_view_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)

#=========================================================================================================================
    
if __name__ == '__main__':
    main()	

