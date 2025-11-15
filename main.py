import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    try:
        if Path(database).exists():
                
            with open(database) as fs:
                data=json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"An exception occure as {err}")

    @classmethod
    def __update(cls):
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        schar=random.choices("!@#$%^&*",k=1)
        id=alpha+num+schar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info={
            "name":input("Tell me your name :-"),
            "age":int(input("Tell your age :-")),
            "emai":input("Tell your email :-"),
            "pin":int(input("Tell your pin:- ")),
            "Accountno":Bank.__accountgenerate(),
            "balance":0
        }
        if info['age']<10 or len(str(info['pin'])) !=6:
            print("sorry does not create your account")
        else:
            print("account has been create sucessfully!!!")
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please note down your account Number")
            Bank.data.append(info)

            Bank.__update()
    
    def depositemoney(self):
        accunumber=input("Plz tell your account number")
        pin=int(input("plz tell your pin"))

        userdata=[i for i in Bank.data if i['Accountno'] ==  accunumber and i['pin'] == pin]
         
        if  userdata == False:
            print("sorry no data fount")
        else:
            amount=int(input("How muchu want to deposite"))
            if amount>10000 or amount<0:
                print("sorry the amount is too much deposite can below 10000 and above 0")
            else:
                  
                userdata[0]['balance']+=amount
                Bank.__update()
                print("Amount deposite sucessfully")
    

    
    def withdrawmoney(self):
        accunumber=input("Plz tell your account number")
        pin=int(input("plz tell your pin"))

        userdata=[i for i in Bank.data if i['Accountno'] ==  accunumber and i['pin'] == pin]
         
        if  userdata == False:
            print("sorry no data fount")
        else:
            amount=int(input("How muchu want to deposite"))
            if userdata[0]['balance']<amount:
                print("Sorry dont have muuch balance")
            else:
                  
                userdata[0]['balance']-=amount
                Bank.__update()
                print("Amount withdrew sucessfully")

    def showdetails(self):
        accunumber=input("Plz tell your account number")
        pin=int(input("plz tell your pin"))

        userdata=[i for i in Bank.data if i['Accountno'] ==  accunumber and i['pin'] == pin] 

        print("Your information are \n\n")
        for i in userdata[0]:
            print(f"{i}:{userdata[0][i]}")
    

    def updatedetails(self):
        accunumber=input("Plz tell your account number")
        pin=int(input("plz tell your pin"))

        userdata=[i for i in Bank.data if i['Accountno'] ==  accunumber and i['pin'] == pin]

        if userdata == False:
            print("No such data found")
        else:
            print("You can not change your age,account number,Balance")

            print("Fill the details for change or leave it empty if no change")

            newdata={
                "name":input("Plz tell new name or press enter :"),
                "emai":input("plz tell your new email or press enter :"),
                "pin":input("Enter new pin or press enter to skip: ")
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]['name']
            if newdata["emai"] == "":
                newdata["emai"] = userdata[0]['emai']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']

            newdata['Accountno'] = userdata[0]['Accountno']
            newdata['balance'] = userdata[0]['balance']
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")


    def Delete(self):
        accunumber=input("Plz tell your account number")
        pin=int(input("plz tell your pin"))

        userdata=[i for i in Bank.data if i['Accountno'] ==  accunumber and i['pin'] == pin]
        if userdata == False:
            print("sorry no such data exist ")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check=='n' or check=="N":
                print("bypassed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("account deleted successfully")
                Bank.__update()
user=Bank()
print("Press 1 for Create an Account")
print("Press 2 for depositing money in bank")
print("Press 3 for withdrawing money from bank")
print("press 4 for details")
print("Press 5 for Updating the details")
print("Press 6 for deleting the account")

check=int(input("Enter your choice: "))

if check==1:
    user.createaccount()

if check==2:
    user.depositemoney()

if check==3:
    user.withdrawmoney()

if check==4:
    user.showdetails()

if check==5:
    user.updatedetails()

if check==6:
    user.Delete()

