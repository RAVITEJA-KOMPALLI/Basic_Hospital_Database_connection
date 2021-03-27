import mysql.connector
class DBconnect:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Raviteja@01",
                                         database="Hospital"
                                        )
        print("\nDB connected\n")

    def add_doctor(self):
        name = input("Name:")
        age = int(input("Age:"))
        gender = input("Gender:")
        email = input("Email:")
        phoneno = int(input("Mobile No:"))
        address = input("Address:")
        #qualification = input("Qualification:")
        speciality = input("Speciality:")
        experience_in_years = int(input("Experience in years :"))
        salary = int(input("Salary :"))
        available_time_duration = input("Available time duration:")

        cur = self.con.cursor()
        sql = "insert into doctor(name ,age ,gender ,email,phoneno, address, speciality,experience_in_years,salary,available_time_duration) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(
            name, age, gender, email, phoneno, address, speciality, experience_in_years, salary, available_time_duration)
        cur.execute(sql)
        self.con.commit()


    def Update(self):
        cur = self.con.cursor(dictionary=True)

        while True:
            phoneno = int(input("Enter the Mobile Number that you have registered:"))
            sql = "select * from doctor where phoneno = '{}' ".format(phoneno)
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
                print('               Select the Doctor You are Searching for                ')
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
                    print('+ speciality : ', i["speciality"])
                    print('+ experience_in_years : ', i["experience_in_years"])
                    print('+ salary : ', i["salary"])
                    print('+ available_time_duration:', i["available_time_duration"])
                    print('\n*************************************************************\n')


                id = int(input("Select the Doctor ID that you are searching for:"))
                cur.execute("select * from Doctor where id = '{}' ".format(id))

                results = cur.fetchall()

                row_count = cur.rowcount

                while row_count == 0:
                    print('\n*************************************************************')
                    print('               Oops You have selected an ID that is not valid  ')
                    print('*************************************************************\n')
                    id = int(input('               Enter the ID you are looking for... Enter 0 come back to menu  '))
                    if id == 0:
                        return
                    cur.execute("select * from Doctor where id = '{}' ".format(id))

                    results = cur.fetchall()
                    row_count = cur.rowcount

                cur.execute("select * from Doctor where id = '{}' ".format(id))
                result = cur.fetchone()

                ans = input("Please enter the Email ID if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update Doctor set email  = '{}' where id='{}' ".format(ans, id))
                self.con.commit()

                ans = input("Please enter the Experience if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update Doctor set experience_in_years  = '{}' where id='{}' ".format(ans, id))
                self.con.commit()

                ans = input("Please enter the salary if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update Doctor set salary  = '{}' where id='{}' ".format(int(ans), id))
                self.con.commit()

                ans = input("Please enter the available time duration if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update Doctor set available_time_duration  = '{}' where id='{}' ".format(ans, id))
                self.con.commit()
                return


    def delDoctor(self):
        cur = self.con.cursor(dictionary=True)

        while True:
            phoneno = int(input("Enter the Mobile Number that you have registered:"))
            sql = "select * from Doctor where phoneno = '{}' ".format(phoneno)
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
                print('               Select the Doctor You are Searching for                ')
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
                    print('+ speciality : ', i["speciality"])
                    print('+ experience_in_years : ', i["experience_in_years"])
                    print('+ salary : ', i["salary"])
                    print('+ available_time_duration:', i["available_time_duration"])
                    print('\n*************************************************************\n')
                id = int(input("Select the Doctor ID that you are searching for:"))


                sql = "select * from Doctor where id = '{}' ".format(id)
                cur.execute(sql)
                results = cur.fetchall()

                row_count = cur.rowcount

                while row_count==0:
                    print('\n*************************************************************')
                    print('               Oops You have selected an ID that is not valid  ')
                    print('*************************************************************\n')
                    id=int(input('               Enter the ID you are looking for... Enter 0 come back to menu  '))
                    if id==0:
                        return
                    cur.execute("select * from Doctor where id = '{}' ".format(id))

                    results = cur.fetchall()
                    row_count = cur.rowcount



                cur.execute("delete from doctor where id='{}' ".format(id))
                self.con.commit()
                return


    def doctor(self):
        while True:
            print('Enter the Operation that you want to perform:')
            print('1. Add New Doctor')
            print('2. Update Doctor details')
            print('3. Delete a doctor entry')
            print("Press any other number key to exit")
            n = int(input('What operation do you want to do:'))
            if n==1:
                self.add_doctor()
                print('\n*************************************************************')
                print('               Database is saved successfully                ')
                print('*************************************************************\n')
            elif n==2:
                self.Update()
                print('\n*************************************************************')
                print('               Details Updated successfully                ')
                print('*************************************************************\n')

            elif n==3:
                self.delDoctor()
                print('\n*************************************************************')
                print('               Doctor record deleted successfully                ')
                print('*************************************************************\n')
            else:break




