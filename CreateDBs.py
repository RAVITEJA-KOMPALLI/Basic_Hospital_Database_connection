import mysql.connector as m
mydb = m.connect(
                host="localhost",
                user="root",
                password="Raviteja@01"
                )
mycursor  = mydb.cursor()
#mycursor.execute("create database hospital")
mycursor.execute("use hospital")
mycursor.execute("create table patient(id bigint auto_increment primary key,name varchar(100),age int,gender varchar(10),email varchar(100),phoneno bigint,address varchar(200),created_on DATETIME NULL DEFAULT CURRENT_TIMESTAMP,no_of_times_visited int default 1,visiting_for varchar(1000),total_amount_paid bigint default 0)")
mycursor.execute("create table doctor(id bigint auto_increment primary key,name varchar(100),age int,gender varchar(10),email varchar(100),phoneno bigint,address varchar(200),speciality varchar(50),experience_in_years int,salary bigint,created_on DATETIME NULL DEFAULT CURRENT_TIMESTAMP,available_time_duration varchar(50))")
mycursor.execute("create table medicine(id bigint auto_increment primary key,name varchar(30),price DECIMAL(18,12),Mfd date,date_in_stock DATETIME NULL DEFAULT CURRENT_TIMESTAMP,expiry_date date,no_of_strips int(15),power varchar(30))")
mydb.commit()
