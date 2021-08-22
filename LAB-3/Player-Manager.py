from tabulate import tabulate
import sqlite3
conn = sqlite3.connect('players_Data.db')
#print("Database opened successfully")
print("Player Manager\n")
#conn.execute("drop table if exists Player")
# create table Player
conn.execute('''CREATE TABLE if not exists Player (
                name text NOT NULL PRIMARY KEY, wins INT NOT NULL,
                losses INT NOT NULL, ties INT NOT NULL)''')
conn.commit()

VIEW = "view"
ADD = "add"
DELETE = "del"
UPDATE = "update"
EXIT = "exit"
def main():
    choice = None
    display_menu()
    try:
        while choice != EXIT:
            choice = str(input('Command: '))
            if choice == VIEW:
                view()
            elif choice == ADD:
                add()
            elif choice == DELETE:
                delete()
            elif choice == UPDATE:
                update()
            elif choice == EXIT:
                conn.close()
                print('Exiting the program...')
            else:
                print('Error: invalid selection.')

    except :
        print("Error: Wrong Datatype - Try again with string value!!! \n")
    
def display_menu():
    print("---------------------")
    print('COMMAND MENU')
    print("---------------------")
    print('view - View players')
    print('add - Add a player')
    print('del - Delete a player')
    print('update - Update a player')
    print('exit - Exit a program')

def view():    
    try:
        cursor = conn.execute("SELECT *, sum(wins + losses + ties) as Games FROM Player GROUP BY name")      
        print('------------------------------------------')
        data=[]
        for c in cursor:
            data.append(c)
            #print('{:10}{:10}{:10}{:10}{:10}'.format(c[0],c[1],c[2],c[3],c[4]))
        print(tabulate(data, headers=["Name", "Wins", "Losses", "Ties", "Games"]))
    except Exception as err:
        print(err)
        
def add():
    try:
        name = input("Name: ")
        wins = int(input("Wins: "))
        losses = int(input("Losses: "))
        ties = int(input("Ties: "))

        sql = "INSERT INTO Player (name, wins, losses, ties) VALUES (?,?,?,?)"
        conn.execute(sql, (name, wins, losses, ties))
        conn.commit()
        #conn.close()
        print(name,"is added succesfully in Player Database")
    except Exception as err:
        print(err)    

def delete():
    try:
        name = input("Name: ")
        sql = "DELETE FROM Player WHERE name=?"
        conn.execute(sql, (name,))
        conn.commit()
        print(name,"was deleted from database succesfully")
    except Exception as err:
        print(err) 
    
def update():
    try:
        cursor = conn.execute("SELECT name as NAME FROM Player")
        data=[]
        for c in cursor:
            data.append(c[0])
        #print(data)
        name = input("Name: ")
        if name in data:
            print("\nPLEASE ENTER UPDATED VALUES:")
            print("----------------------------")
            wins = int(input("Wins: "))
            losses = int(input("Losses: "))
            ties = int(input("Ties: "))

            sql = "UPDATE Player set wins=?,losses=?,ties=? where name=?"
            conn.execute(sql, (wins, losses, ties, name))
            conn.commit()
            print(name,"is updated succesfully")
        else:
         print("Name not found!!!")   
        #conn.close()        
    except Exception as err:
        print(err)     
    
        
main()
