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

if __name__ == '__main__':
    main()