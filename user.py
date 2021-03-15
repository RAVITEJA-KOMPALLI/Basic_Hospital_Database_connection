#from DB_connect import DBconnect
from patient_DB_con import DBconnect as p
from doctor_DB_con import DBconnect as d
from medicine_DB_con import DBconnect as m
def main():

    while True:
        print("\n***********************************************\n")
        print("Select the DataBase that you want to connect.")
        print("1.Patient")
        print("2.Doctor")
        print("3.Medicine")
        print("Press any other number key to exit")
        choice = int(input("Enter your Choice :"))
        if choice == 1:
            dbcon = p()
            dbcon.patient()
        elif choice == 2:
            dbcon = d()
            dbcon.doctor()
        elif choice == 3:
            dbcon = m()
            dbcon.medicine()
        else: break

    '''while True:
        print("***********************")
        print("Press 1 to create Account")
        print("Press 2 to check your Balance")
        print("Press 3 to Deposit Money")
        print("Press 4 to Withdraw Money")
        print("Press 5 to Exit")
        print("Enter your Choice")
        try:
            choice=int(input())
            if(choice==1):
                name=input("Enter your Name")
                addr=input("Enter your Address")
                phno=int(input("Enter your Mobile Number"))
                emaild=input("Enter your Email ID")
                res=dbcon.create_account(name,addr,phno,emaild)
                print(" Your New Account created Successfully! Your Account Number is ",res)

            elif choice==2:
                acno=int(input("Enter your Account Number"))
                res=dbcon.check_balance(acno)
                print("Your current Balance is ",res)

            elif choice==3:
                acno = int(input("Enter your Account Number"))
                amount=int(input("Enter Amount"))
                res=dbcon.update_balance(acno,amount,"D")
                print("Your current Balance is ",res)

            elif choice==4:
                acno = int(input("Enter your Account Number"))
                amount = int(input("Enter Amount"))
                res = dbcon.update_balance(acno, amount, "W")
                print("Your current Balance is ", res)

            elif choice==5:
                dbcon.closeDB()
                break
            else:
                print("Invalid Input")
        except Exception as ex:
            print(ex)
'''





if __name__ == '__main__':
    main()