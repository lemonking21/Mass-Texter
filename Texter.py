from tkinter import Button, Menu, Toplevel, Label, Text, PanedWindow , VERTICAL, END, messagebox, Tk
from tkinter.filedialog import askopenfilename
import smtplib
import pandas as pd
from email.mime.text import MIMEText
#############################################################
#Global variables
#############################################################
username = 'autotextingtest@gmail.com'
password = '123456789Ab'
pnumber = ''
servicep = ''
lname = ''
fname = ''
filename= ''
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
    global username, password, pnumber, servicep, lname, fname
    txtNum = str(pnumber) + str(servicep)

    msg = str(fname) + str(lname)
    message = MIMEText('''Subject: text-message %s''' % (msg))

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
    i.title('Mass Texter')
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
#############################################################
#############################################################
main()
#############################################################
#############################################################