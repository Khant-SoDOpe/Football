import csv                                    #need to import when using .csv file
from replit import clear                 #for using clear function      

def add(backnumber):                          #using add function when you want to add like backnumber and name into .csv file
    about_player = {}                     

    about_player["backnumber"] = backnumber
    about_player["name"] =  input("Enter name of the player: ")
    about_player["team"] = input('Enter team of the player: ')
    about_player["age"] = input('Enter age of the player: ') 

    fieldnames = []
    for key in about_player:
        fieldnames.append(key)

    with open("About_player.csv", "a") as data_file:
        writer = csv.DictWriter(data_file, fieldnames)
        writer.writerow(about_player)

def search(search_with, search_data):  #using search function if you want to search some in .csv file
    answer = []

    with open("About_player.csv", "r") as data_file:
        players_data = csv.DictReader(data_file)

        for player in players_data:
            if player[search_with] == search_data:
                answer.append(player)

        print(answer['name']) 

def delete(players):     #using delete function if you want to delete some in .csv file
    lines = list()

    with open('About_player.csv', 'r') as readFile:
        reader = csv.reader(readFile)

        for row in reader:
            lines.append(row)

            for field in row:
                if field == players:    
                    lines.remove(row)

    with open('About_player.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

def edit():          #using delete function if you want to edit some in .csv file
    df = input("Enter a player's backnumber you want to edit:")
    delete(df)
    add(df)

ask = input("Do you want to start(yes/no)?:") #ask user to you want to start

while ask == 'yes':  #while user type yes
    clear()          #clear terminal
    final_input = input("Who Are you(coach/fan)?: ")        #ask user that who are you
    if final_input == 'coach':   #if user said coach
        password = input("Enter a password of coach:")   #told user to type password

        if password == '2135647':   #if password was true 
            user_input = input("Do you want to (add/search/delete/edit)player?: ") #ask user what do you want to do

            if  user_input == "add":   #if user type add then ask backnumber,name,team,age and add into .csv file
                clear()
                file = open("About_player.csv")
                reader = csv.reader(file)
                lines= len(list(reader))
                add(lines)
                from prettytable import from_csv
                with open("About_player.csv") as fp:
                    mytable = from_csv(fp)
                    print(mytable)
                print("YOUR PLAYER BACKNUMBER IS",lines)
                print("Done")

            if user_input == 'search':  #if user type search then ask backnumber,name,team,age and print about the backnumber of the player
                clear()
                z = input("What do you want to seach player with?(backnumber/name/team/age): ")
                print("Enter a",z,'of the player')
                o = input(":")
                search(z,o)

            if user_input == 'delete':   #if user type delete then ask backnumber and delete all about backnumber of the player
                clear()
                from prettytable import from_csv
                with open("About_player.csv") as fp:
                    mytable = from_csv(fp)
                    print(mytable)
                finalll = input("Enter a backnumber you want to delete:")
                delete(finalll)
                clear()
                with open("About_player.csv") as fp:
                    mytable = from_csv(fp)
                    print(mytable)
                print("Done")

            if user_input == 'edit': #if user type edit then ask backnumber and edit name,team,age of the player
                clear()
                from prettytable import from_csv
                with open("About_player.csv") as fp:
                    mytable = from_csv(fp)
                    print(mytable)
                edit()
                clear()
                from prettytable import from_csv
                with open("About_player.csv") as fp:
                    mytable = from_csv(fp)
                    print(mytable)
                print("Done")
        
        if password != '2135647':   #if user type wrong password
            print("Wrong Password")  #print Wrong password

    if final_input == 'fan':  #if user type 'fan' then user can only search about the player
        print("YOU CAN ONLY SEARCH IF YOU ARE JUST A FAN")
        z = input("What do you want to seach player with?(backnumber/name/team/age): ")
        print("Enter a",z,'of the player')
        o = input(":")
        search(z,o)                         
   
    ask = input("Do you want to start again?:")  #if all finish then ask user to start again

if ask == 'no': #if user type no 
    print("OK")#print ok