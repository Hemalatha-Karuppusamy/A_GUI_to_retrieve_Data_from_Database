from tkinter import *
from tkinter import messagebox
import mysql.connector
import pandas as pd

window = Tk()
window.title("Client Information Access")
window.configure(background="#0D4064",borderwidth=2,relief= GROOVE)
window.geometry('650x600')
window.resizable(False,False)

client = mysql.connector.connect(host='localhost', user='root', password='',
                                     port='3306', database='know_your_client')
c = client.cursor()
def save():
    try:
        c = client.cursor()
        c.execute("select * from kyc")
        output = c.fetchall()
        name = []
        age = []
        contact =[]
        address = []
        for i in output:
            name.append(i[0])
            age.append(i[0])
            contact.append(i[0])
            address.append(i[0])
        dic={"Name":name,"Age":age,"Contact_info":contact,"Address":address}
        df = pd.DataFrame(dic)
        df_csv = df.to_csv("E:\Retrived_data.csv")
        messagebox.showinfo("success","File downloaded successfully")
    except:
        messagebox.showinfo("Error","Error in processing request")
def click():
    try:
        messagebox.showinfo("info", "To read complete data download the file")
        cname0 = Label(window, text= "Name", width=10,font=("Times New Roman", 13), fg="white", bg="#0D4064", justify=CENTER)
        cname0.grid(row=4, column=1, padx=10, pady=5, ipadx=10)
        cname1 = Label(window, text="Age", width=2,font=("Times New Roman", 13), fg="white", bg="#0D4064", justify=CENTER)
        cname1.grid(row=4, column=2, padx=10, pady=5, ipadx=10)
        cname2 = Label(window, text= "Contact Information",width=15, font=("Times New Roman", 13), fg="white", bg="#0D4064", justify=CENTER)
        cname2.grid(row=4, column=3, padx=10, pady=5, ipadx=10)
        cname3 = Label(window, text= "Address", width=25,font=("Times New Roman", 13), fg="white", bg="#0D4064", justify=CENTER)
        cname3.grid(row=4, column=4, padx=10, pady=5, ipadx=10)
        cname4= Label(window, width=2, text="S.No", font=("Times New Roman", 13), fg="white", bg="#0D4064", justify=CENTER)
        cname4.grid(row=4, column=0, padx=10, pady=5, ipadx=10)
        c = client.cursor()
        c.execute("select * from kyc")
        output = c.fetchall()
        nrow = 5
        n = 1
        for i in output:
            label_name = Label(window, text= i[0], width=10,font=("Times New Roman",12), fg="white", bg="#0D4064", justify=CENTER)
            label_name.grid(row=nrow, column=1, padx=10, pady=5, ipadx=10)

            label_age = Label(window, text=i[1],width=2, font=("Times New Roman", 12), fg="white", bg="#0D4064", justify=CENTER)
            label_age.grid(row=nrow, column=2, padx=10, pady=5, ipadx=10)

            label_contact_info = Label(window,width=15, text=i[2], font=("Times New Roman", 12), fg="white", bg="#0D4064", justify=CENTER)
            label_contact_info.grid(row=nrow, column=3, padx=10, pady=5, ipadx=10)

            label_address = Label(window, width=25,text=i[3], font=("Times New Roman", 12), fg="white", bg="#0D4064", justify=CENTER)
            label_address.grid(row=nrow, column=4, padx=10, pady=5, ipadx=10)

            label_slno = Label(window, width=2, text = n, font=("Times New Roman", 12), fg="white", bg="#0D4064",justify=CENTER)
            label_slno.grid(row=nrow, column=0, padx=10, pady=5, ipadx=10)
            n += 1
            nrow += 1
            client.commit()
        messagebox.showinfo("Success","Data Retrieved Successfully")
    except:
        messagebox.showinfo("Error","Error in Retrieving the data")

label_head = Label(window, text="Client Information Access Form", width=45,font=("Times New Roman",18),fg="white",bg="#0D4064",justify=CENTER)
label_head.grid(row=0,columnspan=5,padx=10,pady=5,ipadx=10)

label_head = Label(window, text="click show to retrive data from database",width=45, font=("Times New Roman",11),fg="white",bg="#0D4064",justify=CENTER)
label_head.grid(row=1,columnspan=5,padx=10,pady=5,ipadx=10)

button_submit =Button(window, text="Show", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=CENTER,command=click)
button_submit.grid(row=2,columnspan=5,ipadx=15,pady=10)

button_save =Button(window, text="Export as CSV", font=("Times New Roman",12),fg="white",bg="#0D4064",justify=CENTER,command=save)
button_save.grid(row=3,columnspan=5,ipadx=15,pady=10)

window.mainloop()