import json 
import random
import string 
from pathlib import Path

class Bank:
    
    database = "data.json"
    data = []
    try:
        if Path(database).exists():   # FIXED exists()
            with open(database, "r") as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occurred: {err}")

    @staticmethod
    def _update():
        with open(Bank.database, "w") as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountGenerator(cls):
        alpha = random.choices(string.ascii_letters, k=4)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    def createAccount(self):
        print("\nPlease provide following details\n")
        info = {
            "name": input("Name : "),
            "age": int(input("Age : ")),
            "email": input("Email : "),
            "pin": int(input("Pin : ")),
            "accountNo.": Bank.__accountGenerator(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, you cannot create your account")
        else:
            print("Account has been successfully created")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank._update()
    

    def depositeMoney(self):
        accountNo = input("Please tell your account number : ")
        pin = int(input("Please enter your pin : "))
        userData = [i for i in Bank.data if i['accountNo.'] == accountNo and i['pin'] == pin]

        if not userData:
            print("Sorry, no data found")
            return
        
        amount = int(input("Enter amount you want to deposit (0–10,000) : "))
        userData[0]['balance'] += amount

        Bank._update()
        print("Amount deposited successfully")

    def withDrawmoney(self):
        accountNo = input("Please tell your account number : ")
        pin = int(input("Please enter your pin : "))
        userData = [i for i in Bank.data if i['accountNo.'] == accountNo and i['pin'] == pin]

        if not userData:
            print("Sorry, no data found")
            return
        
        amount = int(input("Enter amount you want to withdraw : "))
        if userData[0]['balance'] < amount:
            print("Insufficient balance")
        else:
            userData[0]['balance'] -= amount
            print("Money withdrawn successfully")

        Bank._update()

    def userDetail(self):
        accountNo = input("Please tell your account number : ")
        pin = int(input("Please enter your pin : "))

        userData = [i for i in Bank.data if i['accountNo.'] == accountNo and i['pin'] == pin]

        if not userData:
            print("No record found")
            return
        
        for key in userData[0]:
            print(f"{key} : {userData[0][key]}")

    def updateDetails(self):
        accountNo = input("Please tell your account number : ")
        pin = int(input("Please enter your pin : "))

        userData = [i for i in Bank.data if i['accountNo.'] == accountNo and i['pin'] == pin]

        if not userData:
            print("No record found")
            return

        print("You cannot change account number and age")
        print("Fill the details for change or leave empty to skip")

        newData = {
            "name": input("New name or press enter to skip: "),
            "email": input("New email or press enter to skip: "),
            "pin": input("New pin or press enter to skip: ")
        }
        
        if newData["name"] != "":
            userData[0]["name"] = newData["name"]

        if newData["email"] != "":
            userData[0]["email"] = newData["email"]

        if newData["pin"] != "":
            userData[0]["pin"] = int(newData["pin"])

        Bank._update()
        print("Details updated successfully")

    def deleteAccout(self):
        accountNo = input("Please tell your account number : ")
        pin = int(input("Please enter your pin : "))

        userData = [i for i in Bank.data if i['accountNo.'] == accountNo and i['pin'] == pin]

        if not userData:
            print("No record found")
            return

        res = input("If you want to delete your account press Y or N : ")

        if res.lower() == "n":
            return

        index = Bank.data.index(userData[0])
        Bank.data.pop(index)        # FIXED pop()
        Bank._update()

        print("Your account was successfully deleted")


user = Bank()

print("Press 1 for creating an account")
print("Press 2 for depositing money")
print("Press 3 for withdrawing money")
print("Press 4 for viewing details")
print("Press 5 for updating details")
print("Press 6 for deleting account")

check = int(input("Enter your response : "))

if check == 1:
    user.createAccount()
elif check == 2:
    user.depositeMoney()
elif check == 3:
    user.withDrawmoney()
elif check == 4:
    user.userDetail()
elif check == 5:
    user.updateDetails()
elif check == 6:
    user.deleteAccout()
