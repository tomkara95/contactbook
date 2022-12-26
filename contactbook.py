import mysql.connector


mydb = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='contacts')

mycursor = mydb.cursor()




exitflag = False
choiceflag = True
while exitflag == False:
    while choiceflag==True:
        print("MENU")
        print("1.New Entry")
        print("2.Call Entry")
        print("3.Modify Entry")
        print("4.Delete Entry")
        print("5.Show all contacts")
        choice = int (input("Select 1 2 3 4 or 5: "))
        if (choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice ==5):
            choiceflag=False 
        else:
            print("Not accepted choice, ")    
        


        if choice == 1:
            print("New contact : ")
            x = input("LastName : ")
            y = input("FirstName : ")
            x1 = x.capitalize()
            y1 = y.capitalize()
            sqlentry = "SELECT * FROM contactsbook WHERE Lastname = %s and Firstname = %s"
            dr = (x,y, )
            mycursor.execute(sqlentry,dr)
            myresult = mycursor.fetchall()
            if myresult:
                print('already exists')
            else:
                z = input("PhoneNumber : ")
                c = input("Email : ")
                c1 = c.lower()
                sqlentry1 = "INSERT INTO contactsbook(Lastname,Firstname,Phonenumber,Email) VALUES (%s , %s, %s, %s)"
                val = (x1,y1,z,c1)
                mycursor.execute(sqlentry1,val)
                mydb.commit()
                print("new entry made successfully!")

        
        
        if choice == 2:
            flag2 = True
            while flag2== True:
                user_input = input ("Contact search Lastname : ")
                user_input2 = input ("Contact's Firstname: ")
                u1 = user_input.capitalize()
                u2 = user_input.capitalize()
                sql = "SELECT * FROM contactsbook WHERE Lastname = %s and Firstname = %s "
                old = (u1,u2, )
                mycursor.execute(sql,old)
                myresult2 = mycursor.fetchall()
                if not myresult2:
                    print ('It does not exist ')
                for i in myresult2:
                    print(i)
                flag2 = False

        if choice ==3:
            print('give an existing account: ')
            x = input("Lastname: ")
            y = input("Firstname: ")
            x2 = x.capitalize()
            y2 = y.capitalize()
            sql = "SELECT * FROM contactsbook WHERE Lastname = %s and Firstname= %s"
            adr = (x2,y2, )

            mycursor.execute(sql, adr)

            myresult3 = mycursor.fetchall()

            if myresult3:
                z = input("NewPhonenumber: ")
                sql = "UPDATE contactsbook SET Phonenumber = %s  WHERE Lastname = %s and Firstname= %s "
                val = (z,x2,y2)
                mycursor.execute(sql, val)
                mydb.commit()
                print("Phone changed! ")
                c = input("New Email: ")
                c1 = c.lower()
                sql1 = "UPDATE contactsbook SET Email = %s  WHERE Lastname = %s and Firstname= %s "
                val2 = (c1,x2,y2)
                mycursor.execute(sql1, val2)
                mydb.commit()
                print("Email changed! ")
            else:
                print('Account does not exist! ')
            

        if choice ==4:
            print("Delete contact : ")
            x = input("LastName : ")
            y = input("FirstName : ")
            x1 = x.capitalize()
            y1 = y.capitalize()
            sqlentry = "SELECT * FROM contactsbook WHERE Lastname = %s and Firstname = %s"
            dr = (x1,y1, )
            mycursor.execute(sqlentry,dr)
            myresult4 = mycursor.fetchall()
            if myresult4:
                print("contact exists")
                sqldel = "DELETE FROM contactsbook WHERE Lastname = %s and Firstname = %s "
                de = (x1,y1)
                mycursor.execute(sqldel,de)
                mydb.commit()
                print("Contact Deleted! ")

            else:
                print("Contact Not Found!")

        if choice == 5:
            print("ALL CONTACTS :  \n")   
            sqlall = "SELECT * FROM contactsbook" 
            mycursor.execute(sqlall)
            myresult = mycursor.fetchall()
            for row in myresult:
                print(row)
                print("\n")


    exittemp= True
    while exittemp==True:
        exit = input("exit? y/n _")
        if exit == "y" or exit=="Y":
            exittemp = False
            exitflag = True
            choiceflag= False
        elif exit == "n" or exit == "N":
            exittemp = False
            #exitflag == False
            choiceflag = True
        else:
            print("not accepted answer,try again : ")