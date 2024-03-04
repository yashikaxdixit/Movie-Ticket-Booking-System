import pymysql as ps
import math
import os
from pyfiglet import figlet_format
import time
sqlpass=input()
    
os.system('cls')
s="insert into userinfo values(%s,%s,%s,%s)"

Movie1="83"
Movie2="Spider-man:No way home"
Movie3="Encanto"
Movie4="The house of dead"

available_seats1=[1,2,3,7,8,9,10,11,12,13,14,17,18,19,20]
booked_seats1=[]
available_seats2=[1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20]
booked_seats2=[]
available_seats3=[1,2,3,4,5,6,7,8,9,10,19,20]
booked_seats3=[]
available_seats4=[8,9,10,11,12,13,14,15,1]
booked_seats4=[]

def ticket(name,age,phonenumber,seats_booked,MOVIE):
    print()
    print("----------- PVR  DUBAI -----------")
    print("------------ E-TICKET ------------")
    print("MOVIE --",MOVIE)
    print("1:45pm SUN 24/03/22")
    print("Your seat number: ",end=" ")
    for i in seats_booked:
        if seats_booked.index(i)==(len(seats_booked)-1):
            print("E"+str(math.ceil(i//5)),i,sep="-")
        else:
            print("E"+str(math.ceil(i//5)),i,sep="-",end=",")
    print("Your tickets will be sent through SMS on your registered mobile number.")
    time.sleep(10)
    print()

def tandc():
    print("""**************************************  TERMS & CONDITIONS  *****************************************
Pre-booked Food & Beverages have to be collected by the patron from the F&B counter by showing the Booking ID.
1. Ticket is compulsory for children of 3 years & above.
2. Incase the ticket is lost or misplaced, duplicate ticket will not be issued.
3. Outside food & beverages are not allowed inside the cinema premises.
4. Decision(s) taken by Cinepolis management is final & abiding.
5. For 3D movies, ticket price includes charges towards usage of 3D glasses.
6. Patrons below the age of 18 years will not be allowed to watch the 'A' rated movie.""")

def welcome_screen():
    print("********************************")
    print("********************************")
    print("******Welcome to PVR DUBAI******")
    print("!!!Get tickets on your mobile!!!")
    print("********************************")
    print("********************************")
    time.sleep(5)
    os.system('cls')
    main()

def status_bar(movie_number):
    if movie_number==1:

        for i in range(1,21):
            if i==1:
                print("E1",end=" ")
            elif i==6:
                print("E2",end=" ")
            elif i==11:
                print("E3",end=" ")
            elif i==16:
                print("E4",end=" ")

            if i not in available_seats1:
                print("[XX]",end=" ")
            else:
                if i<10:
                    print("[0"+str(i)+"]",end=" ")
                else:
                    print("["+str(i)+"]",end=" ")
            if i%5==0:
                print()
    elif movie_number==2:
        for i in range(1,21):
            if i==1:
                print("E1",end=" ")
            elif i==6:
                print("E2",end=" ")
            elif i==11:
                print("E3",end=" ")
            elif i==16:
                print("E4",end=" ")

            if i not in available_seats2:
                print("[XX]",end=" ")
            else:
                if i<10:
                    print("[0"+str(i)+"]",end=" ")
                else:
                    print("["+str(i)+"]",end=" ")
            if i%5==0:
                print()
    elif movie_number==3:
        for i in range(1,21):
            if i==1:
                print("E1",end=" ")
            elif i==6:
                print("E2",end=" ")
            elif i==11:
                print("E3",end=" ")
            elif i==16:
                print("E4",end=" ")

            if i not in available_seats3:
                print("[XX]",end=" ")
            else:
                if i<10:
                    print("[0"+str(i)+"]",end=" ")
                else:
                    print("["+str(i)+"]",end=" ")
            if i%5==0:
                print()
    elif movie_number==4:
        for i in range(1,21):
            if i==1:
                print("E1",end=" ")
            elif i==6:
                print("E2",end=" ")
            elif i==11:
                print("E3",end=" ")
            elif i==16:
                print("E4",end=" ")

            if i not in available_seats4:
                print("[XX]",end=" ")
            else:
                if i<10:
                    print("[0"+str(i)+"]",end=" ")
                else:
                    print("["+str(i)+"]",end=" ")
            if i%5==0:
                print()


    """
    E1 [01] [02] [03] [04] [05]
    E2 [06] [XX] [08] [XX] [10]
    E3 [11] [12] [13] [14] [XX]
    E4 [16] [17] [18] [18] [20]

    """

def main():
    print(figlet_format('USER        ADMIN', font='digital'))
    design=input("Select who you want to continue as: ")

    #admin
    if design=="admin" or design=="Admin" or design=="2" or design=="ADMIN":
        myconnector=ps.connect(host="localhost",user="root",password=sqlpass,database="pvr")
        mycursor=myconnector.cursor()
        passs=input("Enter you password: ")
        if passs=="PVRROCKS" or passs=="pvrrocks":
            os.system('cls')
            time.sleep(5)
            print("""
    1.View spreadsheet
    2.Search for records
    3.Delete records
    4.Delete the table""")
            option=int(input("Select your option: "))
            if option==1:
                mycursor.execute("select * from userinfo")
                output=mycursor.fetchall()
                for i in output:
                    for j in i:
                        print(j,end=" ")
                    print()
                time.sleep(10)


            elif option==2:
                
                print("""
    1.Search by name
    2.Search by age
    3.Search by phone number
    4.Search by email """)
                search=int(input("Select an option: "))
                if search==1:
                    name=input("Enter the name: ")
                    name="%"+name+"%"
                    mycursor.execute("select * from userinfo where NAME like %s",name)
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10)
                    
                elif search==2:
                    age=input("Enter the age: ")
                    mycursor.execute("select * from userinfo where AGE= %s",age)
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10)
                elif search==3:
                    phno=input("Enter the phone number: ")
                    mycursor.execute("select * from userinfo where PHONENUMBER= %s",phno)
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10)
                elif search==4:
                    em=input("Enter the email: ")
                    em="%"+em+"%"
                    mycursor.execute("select * from userinfo where EMAIL like %s",em)
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10)
            elif option==3:
                
                print("""
    1.Delete by name
    2.Delete by age
    3.Delete by phone number
    4.Delete by email """)
                delete=int(input("Select an option: "))
                if delete==1:
                    name=input("Enter the name: ")
                    name="%"+name+"%"
                    mycursor.execute("delete from userinfo where name like %s",name)
                    print("The Updated table is as follows:")
                    mycursor.execute("select * from userinfo")
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10) 
                elif delete==2:
                    age=input("Enter the age: ")
                    mycursor.execute("delete from userinfo where age=%s",age)
                    print("The Updated table is as follows:")
                    mycursor.execute("select * from userinfo")
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10) 
                elif delete==3:
                    phnum=input("Enter the phonenumber: ")
                    mycursor.execute("delete from userinfo where phonenumber=%s",phnum)
                    print("The Updated table is as follows:")
                    mycursor.execute("select * from userinfo")
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10) 
                elif delete==4:
                    em=input("Enter the email: ")
                    em="%"+em+"%"
                    mycursor.execute("delete * from userinfo where email=%s",em)
                    print("The Updated table is as follows:")
                    mycursor.execute("select * from userinfo")
                    output=mycursor.fetchall()
                    for i in output:
                        for j in i:
                            print(j,end=" ")
                        print()
                    time.sleep(10) 

            elif option==4:
                mycursor.execute("drop table userinfo")
    #user
    else:
        username=input("Enter username: ")

        while True:
            print()
            myconnector=ps.connect(host="localhost",user="root",password=sqlpass,database="pvr")
            mycursor=myconnector.cursor()
            name=input("Enter your full name: ")
            age=int(input("Enter your age: "))
            phn=input("Enter your phone number: ")
            email=input("Enter your email: ")
            while len(phn)!=10 and phn[0]=="0":
                phn=input("Please enter a valid phone number: ")
            phn=int(phn)

            time.sleep(3)
            os.system('cls')
            print("Movie's available:")
            print("1. 83")
            print("2. Spider-man:No way home")
            print("3. Encanto")
            print("4. The house of the dead")
            print()
            movie_number=int(input("Select your movie number: "))
            tandc()
            time.sleep(5)
            print()
            x=input("If you accept the terms, press enter ")
            if x=="":
                os.system('cls')
                total_number_seats=int(input("How many seats? "))
                seats_booked=[]
                if movie_number==1:
                    if total_number_seats<=len(available_seats1):
                        print("---SELECT SEATS---")
                        status_bar(1)
                        seats_booked=[]
                        while len(seats_booked)<total_number_seats:
                            select_seats=int(input("Select seats number: "))
                            if select_seats in available_seats1:
                                seats_booked.append(select_seats)
                                booked_seats1.append(select_seats)
                                available_seats1.remove(select_seats)
                            else:
                                print("This seat is sold!!!, Please select some other seat.")
                        ticket(name,age,phn,seats_booked,Movie1)



                    else:
                        print("We don't have enough seats available.")

                elif movie_number==2:
                    if total_number_seats<=len(available_seats2):
                        print("---SELECT SEATS---")
                        status_bar(2)
                        seats_booked=[]
                        while len(seats_booked)<total_number_seats:
                            select_seats=int(input("Select seats number: "))
                            if select_seats in available_seats2:
                                seats_booked.append(select_seats)
                                booked_seats2.append(select_seats)
                                available_seats2.remove(select_seats)
                            else:
                                print("This seat is sold!!!, Please select some other seat.")
                        ticket(name,age,phn,seats_booked,Movie2)

                    else:
                        print("We don't have enough seats available.")
                elif movie_number==3:
                    if total_number_seats<=len(available_seats3):
                        print("---SELECT SEATS---")
                        status_bar(3)
                        seats_booked=[]
                        while len(seats_booked)<total_number_seats:
                            select_seats=int(input("Select seats number: "))
                            if select_seats in available_seats3:
                                seats_booked.append(select_seats)
                                booked_seats3.append(select_seats)
                                available_seats3.remove(select_seats)
                            else:
                                print("This seat is sold!!!, Please select some other seat.")
                        ticket(name,age,phn,seats_booked,Movie3)

                    else:
                        print("We don't have enough seats available.")

                elif movie_number==4:
                    if total_number_seats<=len(available_seats4):
                        print("---SELECT SEATS---")
                        status_bar(4)
                        seats_booked=[]
                        while len(seats_booked)<total_number_seats:
                            select_seats=int(input("Select seats number: "))
                            if select_seats in available_seats4:
                                seats_booked.append(select_seats)
                                booked_seats4.append(select_seats)
                                available_seats4.remove(select_seats)
                            else:
                                print("This seat is sold!!!, Please select some other seat.")
                        ticket(name,age,phn,seats_booked,Movie4)
                        mycursor.execute(s,(name,age,phn,email))
                        myconnector.commit()
                    else:
                        print("We don't have enough seats available.")

                else:
                    print("This movie doesn't exist. Please select some other movie.")
                mycursor.execute(s,(name,age,phn,email))
                myconnector.commit()
                myconnector.close()
            else:
                print()
                print("Have a nice day :)")
                time.sleep(5)

welcome_screen()
