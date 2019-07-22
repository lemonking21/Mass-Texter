from tkinter import Button, Menu, Toplevel, Label, Text, PanedWindow , VERTICAL, END, messagebox, Tk
from tkinter.filedialog import askopenfilename
import smtplib
import numpy
import pandas as pd
from email.mime.text import MIMEText
#############################################################
#Global variables
#############################################################
username = ''#'autotextingtest@gmail.com'
password = ''#'123456789Ab'
pnumber = ''
servicep = ''
lname = ''
fname = ''
filename= ''
message = ''


def getuseremail(i):
    global username, password
    gemail = open_wind(i)
    username_l = Label(gemail, text = 'Username:')
    username_l.pack()
    username_txt = Text(gemail, height = 1, width = 20)
    username_txt.pack()
    password_l = Label(gemail, text = 'Password:')
    password_l.pack()
    password_txt = Text(gemail, height = 1, width = 20)
    password_txt.pack()
    subbtn = Button(gemail, text ='Submit',command = lambda: (set_email_add(username_txt,password_txt)))
    subbtn.pack(side = 'bottom')

def set_email_add(emailN, passwordN):
    global username
    username = emailN.get('1.0',END)
    set_password(passwordN)

def set_password(passwordN):
    global password
    password = passwordN.get('1.0',END)
    messagebox.showinfo('Email Account Set!' , 'Email account has been set!! You should be good to go!')
#############################################################
#############################################################
def main():
    root = Tk()
    root.lift()
    main_win(root)
    root.mainloop()
#############################################################
#############################################################
def send_SMS():
    global username, password, pnumber, servicep, lname, fname, message
    txtNum = str(pnumber) + str(servicep)

    message = MIMEText('[A.M.T.S] \nDear ' + fname + ' ' + lname + '\n' + (message) + '')

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username,password)
    text= message.as_string()
    server.sendmail(username, txtNum,text )
    server.quit()
#############################################################
#############################################################
def select_file():
    global filename
    name = askopenfilename(initialdir='C:/Users/',
                           filetypes =(('CSV File', '*.csv'),('Text File', '*.txt'),('All Files','*.*')),
                           title = 'Choose a file.')
    #try:
        #with open(name,'r',newline = '') as UseFile:
            #print(UseFile.read())
    #except:
        #print("No file exists")
    filename= name
    return filename
#############################################################
#############################################################  
def readfrom_csv():
    global filename
    phone = pd.read_csv(filename)
    length = len(phone.index)
    for x in range(length):
        set_fname(phone['First Name'][x])
        set_lname(phone['Last Name'][x])
        set_pnumber(phone['Phone #'][x])
        set_servicep(phone['Provider'][x])
        send_SMS()
    messagebox.showinfo('SENT!' , 'All messages have been sent to the people in the CSV file!!')
#############################################################
#############################################################
def set_fname(firstname):
    global fname
    fname = firstname
#############################################################
#############################################################
def set_lname(lastname):
    global lname
    lname =lastname
#############################################################
#############################################################
def set_pnumber(phonenum):
    global pnumber
    pnumber= phonenum
#############################################################
#############################################################
def set_servicep(serProvider):
    global servicep
    servicep = get_SP_extension(serProvider)
#############################################################
#############################################################
def get_SP_extension(serProvider):
    serProvider = serProvider.lower()
    if serProvider == 'verizon':
        return '@vtext.com'
    elif serProvider == 'at&t':
        return '@txt.att.net'
    elif serProvider == 'sprint':
        return '@messaging.sprintpc.com'
    elif serProvider == 't-mobile':
        return 'tmomail.net'
    elif serProvider == 'boost mobile':
        return '@myboostmobile.com'
    elif serProvider == 'cricket':
        return '@sms.mycricket.com'
    elif serProvider == 'metro PCS':
        return '@mymetropcs.com'
    elif serProvider == 'tracfone':
        return '@mmst.tracfone.com'
    elif serProvider == 'u.s.cellular':
        return '@email.uucc.net'
    elif serProvider == 'virgin mobile':
        return '@vmobl.com'
#############################################################
#############################################################
def file_update(i, j):
    name = select_file()
    i.config(state= 'normal')
    i.delete('1.0', END)
    i.insert('1.0',name)
    i.config(state= 'disable')
#############################################################
#############################################################
def main_win(i):
    i.title('Auto Mass Texter System')
    p = PanedWindow(i, orient= VERTICAL, height = 10, width = 30)
    p.pack()
    label = Label(p, text = 'Select a file with the clients firstname, lastname, Phone Number and Phone provider')
    label.pack()
    file_name=Text(p, height = 1, width = 50)
    file_name.pack()
    smsBTN = Button(i, text = 'Send SMS', command = lambda:readfrom_csv())
    smsBTN.pack(side = 'bottom')
    fbtn= Button(p, text = "Upload File",command = lambda:file_update(file_name, smsBTN))
    fbtn.pack( expand = 1)
    win_menu(i)

def win_menu(i):
    menu= Menu(i)
    i.config(menu=menu)
    file= Menu(menu)
    view = Menu(menu)
    message = Menu(menu)
    email = Menu(menu)


    file.add_command(label = 'exit', command = i.destroy)
    menu.add_cascade(label = 'File', menu = file)

    view.add_command(label = 'Full Screen',  command= lambda:i.geometry("{0}x{1}+0+0".format(i.winfo_screenwidth(), i.winfo_screenheight())))
    view.add_command(label = 'Original Size',  command= lambda:i.geometry('406x95'))
    menu.add_cascade(label = 'View', menu = view)

    message.add_command(label = 'Message',command = lambda:message_win(i))
    menu.add_cascade(label = 'Message', menu = message)

    email.add_command(label = 'Email',command = lambda:getuseremail(i))
    menu.add_cascade(label = 'Email', menu = email)

def message_win(i):
    mess_w = open_wind(i)
    mess = Text(mess_w, height = 10, width = 50)
    mess.pack()
    subbtn = Button(mess_w, text ='Submit',command = lambda:message_w(mess))
    subbtn.pack(side = 'bottom')

def open_wind(i):
    i_win = Toplevel(i)
    i_win.attributes('-topmost',1)
    return i_win

def message_w(mess):
    global message
    message = mess.get('1.0',END)

#############################################################
#############################################################
main()
#############################################################
#############################################################