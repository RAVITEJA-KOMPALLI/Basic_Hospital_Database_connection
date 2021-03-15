import pytest
import mysql.connector as mysql

def test_mysql():

    mydb = mysql.connect(host="localhost", user="root", password="Raviteja@01", database="Hospital")
    cur = mydb.cursor(dictionary=True)
    cur.execute("select * from patient where id=1")
    results = cur.fetchall()
    assert results[0]["phoneno"] == 9652792097
