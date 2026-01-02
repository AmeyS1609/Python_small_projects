import Data
from prettytable import PrettyTable
import mysql.connector as m
mydatabase=m.connect(host=Data.DB_HOST,user=Data.DB_USER,password=Data.DB_PASSWORD)
cur=mydatabase.cursor()
cur.execute("create database if not exists bank")
cur.execute("use bank")
cur.execute("create table if not exists signup(username varchar(30),password varchar(30))")
cur.execute("DESCRIBE signup")
print(cur.fetchall())
def signup():
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    try:
        cur.execute("INSERT INTO signup (username, password) VALUES (%s, %s)", (username, password))
        mydatabase.commit()
        print("\t\t\t**********+++SIGNUP SUCCESSFUL+++**********")
        print("Now please login to continue")
        login()
    except m.errors.IntegrityError: #Checks if any Data base rule is violated, here it checks for duplicate username
        print("Username already exists. Please choose a different username.")
        return
def login():
    while True:
        username = input("USERNAME: ")
        password = input("PASSWORD: ")
        cur.execute("SELECT 1 FROM signup WHERE username=%s AND password=%s",(username, password))
        result = cur.fetchone()
        if result is not None:
            break  
        print("Wrong username or password")
        choice = input("Enter 1 to retry else any other key to go back: ")
        if choice != "1":
            return  
    while True:
        print("Press 1 to open new account")
        print("Press 2 to deposit amount")
        print("Press 3 to withdraw money")
        print("Press 4 for balance enquiry")
        print("Press 5 for customer details")
        print("Press 6 for contact info updation")
        print("Press 7 to close account")
        print("Press 8 to see information")
        print("Press 9 to exit")

        try:
            a = int(input("Enter what to do: "))
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if a == 1:
            openacc()
        elif a == 2:
            dep()
        elif a == 3:
            withdraw()
        elif a == 4:
            bal_enq()
        elif a == 5:
            det()
        elif a == 6:
            update()
        elif a == 7:
            close()
        elif a == 8:
            show()
        elif a == 9:
            print("\t\t\tThankyou")
            print("\t\t\tHave a nice day")
            cur.close()
            mydatabase.close()
            return
        else:
            print("Invalid choice. Enter 1 to 9.")

def openacc():
    name=input("enter full name of owner:")
    acc_no=int(input("enter account number:"))
    address=input("enter permanent address of owner:")
    contact_no=int(input("enter contact number of owner:"))
    total_balance=int(input("enter how much balance ypu want to deposit:"))
    data1=(name,acc_no,address,contact_no,total_balance)
    data2=(name,acc_no,total_balance)
    cur.execute("""CREATE TABLE IF NOT EXISTS acc(name VARCHAR(30),acc_no INT PRIMARY KEY,address VARCHAR(30),contact_no BIGINT,total_balance INT)""")
    cur.execute("create table if not exists amount(name varchar(30),acc_no int,total_balance int)")
    sql1="INSERT INTO acc(name, acc_no, address, contact_no, total_balance) VALUES (%s, %s, %s, %s, %s)"
    sql2="INSERT INTO amount(name, acc_no, total_balance) VALUES (%s, %s, %s)"
    cur.execute(sql1,data1)
    cur.execute(sql2,data2)
    mydatabase.commit()
    print("")
    print("\t\t\t---****data entered successfully and account is open****---")
def dep():
    acc_no = int(input("enter account number: "))
    dep_am = int(input("enter amount you want you want deposit: "))
    cur.execute("UPDATE acc SET total_balance = total_balance + %s WHERE acc_no = %s",(dep_am, acc_no))
    mydatabase.commit()
    if cur.rowcount == 0:
        print("Account not found.")
        return
    cur.execute("SELECT total_balance FROM acc WHERE acc_no=%s", (acc_no,))
    row = cur.fetchone()
    t = PrettyTable(['total_balance'])
    t.add_row([row[0]])
    print("\t\t\t---****Available balance after deposit****---")
    print(t)
def withdraw():
    acc_no = int(input("enter account number: "))
    withdraw_amt = int(input("enter amount you want to withdraw: "))
    cur.execute("SELECT total_balance FROM acc WHERE acc_no=%s", (acc_no,))
    row = cur.fetchone()
    if row is None:
        print("Account not found.")
        return
    current_balance = row[0]
    if withdraw_amt > current_balance:
        print("Insufficient funds.")
        print("Available balance:",current_balance)
        return
    cur.execute("UPDATE acc SET total_balance = total_balance - %s WHERE acc_no=%s",(withdraw_amt, acc_no))
    mydatabase.commit()
    cur.execute("SELECT total_balance FROM acc WHERE acc_no=%s", (acc_no,))
    result = cur.fetchall()
    t = PrettyTable(['total_balance'])
    for total_balance in result:
        t.add_row([total_balance[0]])
    print("\t\t\t---****Avail total balance after withdrawal****---")
    print(t)
def bal_enq():
    acc_no = int(input("enter account number: "))
    cur.execute("SELECT total_balance FROM acc WHERE acc_no=%s", (acc_no,))
    row = cur.fetchone()
    if row is None:
        print("Account not found.")
        return
    t = PrettyTable(['total_balance'])
    t.add_row([row[0]])
    print("\t\t\t---****Balance enquiry successfully printed****---")
    print(t)
def det():
    acc_no = int(input("enter account number: "))
    cur.execute("SELECT * FROM acc WHERE acc_no=%s", (acc_no,))
    row = cur.fetchone()
    if row is None:
        print("Account not found.")
        return
    t = PrettyTable(['name','acc_no','address','contact_no','total_balance'])
    t.add_row([row[0], row[1], row[2], row[3], row[4]])
    print("\t\t\t---****Customer details****---")
    print(t)
def update():
    acc_no=int(input("enter account number:"))
    new_cont=int(input("enter new contact number:"))
    cur.execute("UPDATE acc SET contact_no=%s WHERE acc_no = %s",(new_cont, acc_no))
    mydatabase.commit()
    if cur.rowcount == 0:
        print("Account not found.")
        return
    cur.execute("SELECT * FROM acc WHERE acc_no=%s", (acc_no,))
    result=cur.fetchall()
    t=PrettyTable(['name','acc_no','address','contact_no','total_balance'])
    for row in result:
        t.add_row([row[0], row[1], row[2], row[3], row[4]])
    print("\t\t\t---****Updated Customer details****---")
    print(t)
def close():
    acc_no = int(input("enter account number: "))
    cur.execute("DELETE FROM acc WHERE acc_no=%s", (acc_no,))
    mydatabase.commit()
    if cur.rowcount == 0:
        print("Account not found.")
        return
    print("\t\t\t---****Account closed successfully****---")
def show():
    cur.execute("select * from acc")
    t=PrettyTable(['name','acc_no','address','contact_no','total_balance'])
    result=cur.fetchall()
    for row in result:
        t.add_row([row[0], row[1], row[2], row[3], row[4]])
    print("\t\t\t---****All information****---")
    print(t)
print("\t1:Signup\n\n\t2:Login")
ch=int(input("Enter choice:"))
if ch==1:
    signup()
elif ch==2:
    login()
else:
    print("Wrong entry")