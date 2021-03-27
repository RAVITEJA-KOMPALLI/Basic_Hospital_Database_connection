import mysql.connector
class DBconnect:
    def __init__(self):
        self.con=mysql.connector.connect(host="localhost",
                                         user="root",
                                         password="Raviteja@01",
                                         database="Hospital"
                                        )
        print("DB connected")

    def add_medicine(self):
        name = input("Name:")
        price = int(input("price:"))
        Mfd = input("Mfd:")
        #date_in_stock = input("date_in_stock:")
        expiry_date = input("expiry_date:")
        no_of_strips = int(input("no_of_strips:"))
        power = input("power/dosage (in mg):")


        cur = self.con.cursor()
        sql = "insert into medicine(name ,price ,Mfd ,expiry_date, no_of_strips, power) values('{}','{}','{}','{}','{}','{}')".format(
            name.lower(), price, Mfd, expiry_date, no_of_strips, power)
        cur.execute(sql)
        self.con.commit()


    def Update(self):
        cur = self.con.cursor(dictionary=True)

        while True:
            name = input("Enter the Medicine you are searching for:")
            sql = "select * from medicine where name = '{}' ".format(name.lower())
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
                print('               Medicine you are Searching for                ')
                print('*************************************************************\n')

                for i in results:
                    print('\n*************************************************************\n')

                    print('+ ID : ', i["id"])
                    print('+ Name : ', i["name"])
                    print('+ price : ', i["price"])
                    print('+ Mfd : ', i["Mfd"])
                    print('+ date_in_stock : ', i["date_in_stock"])
                    print('+ expiry_date : ', i["expiry_date"])
                    print('+ no_of_strips : ', i["no_of_strips"])
                    print('+ power/dosage (in mg) : ', i["power"])

                    print('\n*************************************************************\n')



                cur.execute("select * from medicine where name = '{}' ".format(name))
                result = cur.fetchone()

                ans = input("Please enter the name if you are willing to change, else ignore :")
                if len(ans) != 0:
                    name = ans.lower()
                    cur.execute("update medicine set name  = '{}' where name='{}' ".format(ans.lower(), name))
                self.con.commit()

                ans = input("Please enter the MFD if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update medicine set Mfd  = '{}' where name='{}' ".format(ans, name))
                self.con.commit()

                ans = input("Please enter the Price if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update medicine set price  = '{}' where name='{}' ".format(float(ans), name))
                self.con.commit()

                ans = input("Please enter the no_of_strips if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update medicine set no_of_strips  = '{}' where name='{}' ".format(ans, name))
                self.con.commit()

                ans = input("Please enter the power/dosage (in mg) if you are willing to change, else ignore :")
                if len(ans) != 0:
                    cur.execute("update medicine set power  = '{}' where name='{}' ".format(ans, name))
                self.con.commit()

                return


    def delMedicine(self):
        cur = self.con.cursor(dictionary=True)

        while True:
            name = input("Enter the Medicine you are searching for:")
            sql = "select * from medicine where name = '{}' ".format(name.lower())
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
                print('               Select the ID id the result obtained is correct                ')
                print('*************************************************************\n')

                for i in results:
                    print('\n*************************************************************\n')

                    print('+ ID : ', i["id"])
                    print('+ Name : ', i["name"])
                    print('+ price : ', i["price"])
                    print('+ Mfd : ', i["Mfd"])
                    print('+ date_in_stock : ', i["date_in_stock"])
                    print('+ expiry_date : ', i["expiry_date"])
                    print('+ no_of_strips : ', i["no_of_strips"])
                    print('+ power/dosage (in mg) : ', i["power"])

                    print('\n*************************************************************\n')
            id = int(input("Select the medicine ID if you are tring to delete the record:"))

            sql = "select * from medicine where id = '{}' ".format(id)
            cur.execute(sql)
            results = cur.fetchall()

            row_count = cur.rowcount

            while row_count == 0:
                print('\n*************************************************************')
                print('               Oops You have selected an ID that is not valid  ')
                print('*************************************************************\n')
                id = int(input('               Enter the ID you are looking for... Enter 0 come back to menu  '))
                if id == 0:
                    return
                cur.execute("select * from medicine where id = '{}' ".format(id))

                results = cur.fetchall()
                row_count = cur.rowcount

            cur.execute("delete from medicine where id='{}' ".format(id))
            self.con.commit()
            return


    def medicine(self):
        while True:
            print('Enter the Operation that you want to perform:')
            print('1. Add New Medicine')
            print('2. Update Medicine details')
            print('3. Delete a Medicine entry')
            print("Press any other number key to exit")
            n = int(input('What operation do you want to do:'))
            if n == 1:
                self.add_medicine()
                print('\n*************************************************************')
                print('               Database is saved successfully                ')
                print('*************************************************************\n')
            elif n == 2:
                self.Update()
                print('\n*************************************************************')
                print('               Details Updated successfully                ')
                print('*************************************************************\n')

            elif n == 3:
                self.delMedicine()
                print('\n*************************************************************')
                print('               medicine record deleted successfully                ')
                print('*************************************************************\n')
            else:
                break
