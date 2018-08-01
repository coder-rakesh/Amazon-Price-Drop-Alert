#Currently works only for amazon.com Support for other regions to be added soon.

from amazon.api import AmazonAPI
from twilio.rest import Client
import time
from Tkinter import *
import tkMessageBox

idno=[]

#data for authorization for sending message 
account_sid="ACb2a7534e1d84c28169f5b13bb7764745"
auth_token="787b63f2b13c95adf4fb70c5f247931a"
my_no="9077174834"#your phone no

amazon= AmazonAPI("AKIAJIUJ43R4FVJQFV7Q", "qu/VBpLKHRBe/p+leDjuY0RE39cNCGmuqfdd+/Sm", "rakeshamazona-20")

#sends the "text" as a message to your phone
def sendmsg(text):
    try:    
        client = Client(account_sid, auth_token)
        message = client.messages.create(to=my_no, from_="+16194040245",body=text)
    except Exception as e:
         msg="Sorry could not send message due to %s"%((type(e).__name__))
         tkMessageBox.showinfo("Oops!",msg)
         
            
#function on clicking submit button
def click(event):
    while len(idno)!=0:
        idno.pop()
    if len(entry[1].get())==0 and len(entry[2].get())==0 and len(entry[3].get())==0 and len(entry[4].get())==0 and len(entry[5].get())==0:
        tkMessageBox.showinfo("Oops!","You have not entered even a single item")
    else:
        for i in range(1,6):
            if len(entry[i].get())!=0:
                idno.append(entry[i].get())
        no_of_items=len(idno)
        old_price=[]     
        title=[]
        error=0
 
        for i in range(no_of_items):
            try:
                product=amazon.lookup(ItemId=str(idno[i])) 
                title.append(product.title)
                oldp_rice.append(product.price_and_currency[0])
            except Exception as e:
                msg="Error for item "+str(i+1)+"\n"+(type(e).__name__)+"\n"
                tkMessageBox.showinfo("Oops!",msg)
                error+=1
                
        #No error occured            
        if error==0:
            msgtitle= "Price for your items at "+str(time.ctime(time.time()))
            current=""
            for i in range(no_of_items):
                current+=title[i]+"=> "+str(oldprice[i])+" $"+"\n"
            tkMessageBox.showinfo(msgtitle,current)
            tkMessageBox.showinfo("Cheers!","You will be notified when the price of any of your item(s) drop(s)\nPlease donot close this window")
            while(1):
                    new_price=[]
                    pric_edrop=[]
                    time.sleep(600)#Checks again after an interval of 10 minutes
                    for i in range(no_of_items):
                            try:
                                    product=amazon.lookup(ItemId=str(idnos[i])) 
                                    new_price.append(product.price_and_currency[0])
                            except Exception as e:
                                    msg="Error: "+(type(e).__name__)
                                    tkMessageBox.showinfo("Oops!",msg)
                                    
                    for i in range(no_of_items):
                            if(new_price[i]<oldprice[i]):
                                    price_drop.append(True)
                            else:
                                    price_drop.append(False)
                    for i in range(no_of_items):
                            if price_drop[i]==True:
                                    msg="The price of your item %s has dropped from %s $ to %s $ "%(title[i],old_price[i],new_price[i])
                                    print (msg)
                                    sendmsg(msg)

########### GUI ############
                                    
root=Tk() #blank window

root.title("Amazon Price Drop Alert")
root.geometry("500x400")

mainlabel=Label(root,text="Enter the ASIN No or ISBN No(for books) in ItemID Field.\n You can enter upto 5 items\n")

l=[None]*6 # a python list 
entry=[None]*6

l[1]=Label(root,text="ItemID\n")
l[2]=Label(root,text="ItemID\n")
l[3]=Label(root,text="ItemID\n")
l[4]=Label(root,text="ItemID\n")
l[5]=Label(root,text="ItemID\n")

entry[1]=Entry(root)
entry[2]=Entry(root)
entry[3]=Entry(root)
entry[4]=Entry(root)
entry[5]=Entry(root)

mainlabel.grid(row=0,column=19,columnspan=3)
l[1].grid(row=1,column=19,sticky=E)
entry[1].grid(row=1,column=20)
l[2].grid(row=5,column=19,sticky=E)
entry[2].grid(row=5,column=20)
l[3].grid(row=8,column=19,sticky=E)
entry[3].grid(row=8,column=20)
l[4].grid(row=13,column=19,sticky=E)
entry[4].grid(row=13,column=20)
l[5].grid(row=17,column=19,sticky=E)
entry[5].grid(row=17,column=20)

button=Button(root,text="Submit")
button.grid(row=19,column=20)
button.bind("<Button-1>",click)

root.mainloop()#window displays constantly       

