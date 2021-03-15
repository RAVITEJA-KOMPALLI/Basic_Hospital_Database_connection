import mysql.connector
class DBconnect:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Raviteja@01",
                                         database="Hospital"
                                        )
        print("DB connected")
    def add_patient(self):
        name = input("Name:")
        age = int(input("Age:"))
        gender = input("Gender:")
        email = input("Email:")
        phoneno = int(input("Mobile No:"))
        address = input("Address:")
        visiting_for = input("Reason for visiting:")
        amount_paid = int(input("Amount paid:"))
        cur = self.con.cursor()
        sql = "insert into patient(name ,age ,gender ,email,phoneno, address, visiting_for,total_amount_paid) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(
            name, age, gender, email, phoneno, address, visiting_for, amount_paid)
        cur.execute(sql)
        self.con.commit()


    def visit_again(self):
        cur = self.con.cursor(dictionary=True)

        while True:
            phoneno = int(input("Enter the Mobile Number that you have registered:"))
            sql = "select * from patient where phoneno = '{}' ".format(phoneno)
            cur.execute(sql)

            results = cur.fetchall()
            row_count = cur.rowcount
            print("number of affected rows: {}".format(row_count))
            c=0
            if row_count == 0:
                print('\n*************************************************************')
                print('               No Entry Exists!!!                ')
                print('*************************************************************\n')

            else:
                print('\n*************************************************************')
                print('               Select the Patient You are Searching for                ')
                print('*************************************************************\n')

                for i in results:
                    print('\n*************************************************************\n')

                    print('+ ID : ', i["id"])
                    print('+ Name : ', i["name"])
                    print('+ Age : ', i["age"])
                    print('+ Gender : ', i["gender"])
                    print('+ Email : ', i["email"])
                    print('+ Phone_no : ', i["phoneno"])
                    print('+ Address : ', i["address"])
                    print('+ Registered_On : ', i["created_on"])
                    print('+ No_of_Times_Visited : ', i["no_of_times_visited"])
                    print('+ Reason_For_Visiting : ', i["visiting_for"])
                    print('+ Amount_Paid_Till_Date:', i["total_amount_paid"])
                    print('\n*************************************************************\n')
                    id = int(input("Select the Patient ID that you are searching for:"))
                    cur.execute("select * from patient where id = '{}' ".format(id))
                    result = cur.fetchone()
                    no_of_times_visited = result['no_of_times_visited'] + 1
                    visiting_for = result["visiting_for"] + ', ' + input("Enter the reason you are Visiting again : ")

                    cur.execute(
                        "update Patient set no_of_times_visited  = '{}' ,visiting_for = '{}' where id='{}' ".format(
                            no_of_times_visited, visiting_for, id))
                    self.con.commit()
                    return


    def UpdateCash(self):
        cur = self.con.cursor(dictionary=True)

        while True:
            phoneno = int(input("Enter the Mobile Number that you have registered:"))
            sql = "select * from patient where phoneno = '{}' ".format(phoneno)
            cur.execute(sql)

            results = cur.fetchall()
            row_count = cur.rowcount
            print("number of affected rows: {}".format(row_count))
            if row_count == 0:
                print('\n*************************************************************')
                print('               No Entry Exists!!!                ')
                print('*************************************************************\n')

            else:
                print('\n*************************************************************')
                print('               Select the Patient You are Searching for                ')
                print('*************************************************************\n')

                for i in results:
                    print('\n*************************************************************\n')

                    print('+ ID : ', i["id"])
                    print('+ Name : ', i["name"])
                    print('+ Age : ', i["age"])
                    print('+ Gender : ', i["gender"])
                    print('+ Email : ', i["email"])
                    print('+ Phone_no : ', i["phoneno"])
                    print('+ Address : ', i["address"])
                    print('+ Registered_On : ', i["created_on"])
                    print('+ No_of_Times_Visited : ', i["no_of_times_visited"])
                    print('+ Reason_For_Visiting : ', i["visiting_for"])
                    print('+ Amount_Paid_Till_Date:', i["total_amount_paid"])
                    print('\n*************************************************************\n')
                    id = int(input("Select the Patient ID that you are searching for:"))
                    cur.execute("select * from patient where id = '{}' ".format(id))
                    result = cur.fetchone()
                    total_amount_paid =  result["total_amount_paid"] + int(input("Enter the amount: "))
                    cur.execute(
                        "update Patient set total_amount_paid  = '{}'  where id='{}' ".format(
                            total_amount_paid,  id))
                    self.con.commit()
                    return


    def patient(self):
        while True:
            print('Enter the Operation that you want to perform:')
            print('1. Add New Patient')
            print('2. Visiting again')
            print('3. Update the Cash')
            print('What operation do you want to do:')
            n = int(input())
            if n==1:
                self.add_patient()
                print('\n*************************************************************')
                print('               Database is saved successfully                ')
                print('*************************************************************\n')
            elif n==2:
                self.visit_again()
                print('\n*************************************************************')
                n = int(input("               Are you willing to update the Cash? 1.Yes 2.No"))
                print('*************************************************************\n')
                if n==1:
                    self.UpdateCash()
                    break



