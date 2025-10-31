#IMPORTING PACKAGE

import pandas as pd

#defining a function that adds info 
#into the hotel dataframe
def addition():
    df=pd.read_csv(r'C:\Users\User\Desktop\hotel.csv',encoding=
    'unicode_escape')
    print("\nThis is the existing table")
    print(df)

    #get info to update from user if user chooses yes
    c=input("\ndo you want to enter a row? (yes/no) ")
    if c=='yes':
        cust_id=input("\nenter the customer id: ")
        hotel=input("\nenter the hotel name: ")
        hotel_id=input("\nenter the hotel id: ")
        city=input("\nenter the city: ")
        room_type_id=input("\nenter the id of room type: ")
        price_in_dhs=input("\nenter the price (dhs): ")

        #create new dataframe with the user input data
        #then add it to the existing dataframe
        df1=pd.DataFrame([[cust_id,hotel,hotel_id,city,room_type_id,price_in_dhs]],co
        lumns=["cust_id","hotel","hotel_id","city","room_type_id","price_in_dhs"])
        df2=df.append(df1)

        #write the new dataframe to the csv file
        #read it back from the csv file
        #and display it to the user
        df2=df2.to_csv(r'C:\Users\User\Desktop\hotel.csv',index=False,
        header=True)
        df=pd.read_csv(r'C:\Users\User\Desktop\hotel.csv',encoding=
        'unicode_escape')
        print("\ntable updated\n",df)

    #exit the function
    elif(c=='no'):
        exit()

#defining a function that deletes info 
#from the hotel dataframe
def deletion():
    #getting the data from the csv
    #and displaying it to the user
    df=pd.read_csv (r'C:\Users\User\Desktop\hotel.csv')
    print("\nThis is the existing table:")
    print(df)

    #get the index number to delete the corresponding row
    c=int(input("\nenter which row you want to delete "))
    df=df.drop(c)

    #after deletion, write the updated dataframe to the csv
    #display the new csv to the user
    df.to_csv(r'C:\Users\User\Desktop\hotel.csv', index=False,header=True)
    print("\nDeleted successfully")
    print("\ntable updated\n",df)

#defining a function that modifies info 
#from the hotel dataframe
def modify():

    #display the current dataframe/info in the csv
    df=pd.read_csv(r'C:\Users\User\Desktop\hotel.csv')
    print("\nThis is the existing table: ")
    print(df)

    #get info about the modification from the user
    c=int(input("enter which row you want to modify: "))
    d=input("enter the column name which you want to modify: " )
    e=input("enter the value to be changed: ")
    df.loc[c,d]=e
    
    #update the data in the csv,
    #inform the user that it is updated
    #and display the new dataframe
    print("Row modified!!!\n",df)
    df.to_csv(r'C:\Users\User\Desktop\hotel.csv', index=False, header=True)

    
#this function helps in finding the row number for
#an user input name of hotel
def search():
    df=pd.read_csv(r'C:\Users\User\Desktop\hotel.csv')
    a=int(input("\nenter the customer id\n"))
    for index, row in df.iterrows():
        if a==row['cust_id']:
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