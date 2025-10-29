#IMPORTING PACKAGE

import pandas as pd


#defining a function that adds info 
#into the airways dataframe
def addition():
    df=pd.read_csv(r'C:\Users\User\Desktop\airways.csv',encoding='unicode_escape')
    print("\nThis is the existing table",df)
    c=input("\ndo you want to enter a row? (yes/no) ")

    #get info to update from user if user chooses yes
    if c=='yes':
        cust_id=input("\nenter the customer's id: ")
        name=input("\nenter the customer's name: ")
        age=input("\nenter the customer's age: ")
        gender=input("\nenter the customer's gender: ")
        dep=input("\nenter the departure port: ")
        arl=input("\nenter the arrival port: ")

        #create new dataframe with the user input data
        #then add it to the existing dataframe
        df1=pd.DataFrame([[cust_id,name,age,gender,dep,arl]],columns=["cust_id","name","age","gender","departure port","arrival port"])
        df2=df.append(df1)

        #write the new dataframe to the csv file
        #read it back from the csv file
        #and display it to the user
        df2=df2.to_csv(r'C:\Users\User\Desktop\airways.csv',index=False,header=True)
        df=pd.read_csv(r'C:\Users\User\Desktop\airways.csv',encoding='unicode_escape')
        print("\ntable updated\n",df)

    #exit the function
    elif(c=='no'):
        exit()

#defining a function that deletes info 
#from the airways dataframe
def deletion():

    #getting the data from the csv
    #and displaying it to the user
    df=pd.read_csv (r'C:\Users\User\Desktop\airways.csv')
    print("\nThis is the existing table:")
    print(df)
    
    #get the index number to delete the corresponding row
    c=int(input("\nenter which row you want to delete "))
    df=df.drop(c)
    
    #after deletion, write the updated dataframe to the csv
    #display the new csv to the user
    df.to_csv(r'C:\Users\User\Desktop\airways.csv', index=False,header=True)
    print("\nDeleted successfully")
    print("\ntable updated\n",df)

#defining a function that modifies info 
#from the airways dataframe
def modify():

    #display the current dataframe/info in the csv
    df=pd.read_csv(r'C:\Users\User\Desktop\airways.csv')
    print("\nThis is the existing table: ")
    print(df)
    #get info about the modification from the user
    c=int(input("enter which row you want to modify "))
    d=input("enter the column name which you want to modify ")
    e=input("enter the value to be changed ")
    df.loc[c,d]=e

    #update the data in the csv,
    #inform the user that it is updated
    #and display the new dataframe
    print("Row modified!!!\n",df)
    df.to_csv(r'C:\Users\User\Desktop\airways.csv', index=False, header=True)


#this function helps in finding the row number for
#an user input name of airways
def search():
    df=pd.read_csv(r'C:\Users\User\Desktop\airways.csv')
    a=input("\nenter the name: ")
    for index, row in df.iterrows():
    if a==row['name']:
    print("\n",row)


while True:
    print('\nWelcome to my project')
    print('\nMain Menu')
    print('________')
    print('1. Add a new item')
    print('2. Delete a record')
    print('3. Modify the row')
    print('4. search the table')
    ch=int(input('enter the choice: '))
    if ch==1:
        addition()
    elif ch==2:
        deletion()
    elif ch==3:
        modify()
    elif ch==4:
        search()
