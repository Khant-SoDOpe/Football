import csv
import os
from prettytable import from_csv

FILE_NAME = "About_player.csv"
COACH_PASSWORD = '2135647'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(backnumber):
    about_player = {
        "backnumber": backnumber,
        "name": input("Enter name of the player: "),
        "team": input('Enter team of the player: '),
        "age": input('Enter age of the player: ')
    }

    fieldnames = list(about_player.keys())

    try:
        with open(FILE_NAME, "a", newline='') as data_file:
            writer = csv.DictWriter(data_file, fieldnames)
            writer.writerow(about_player)
    except Exception as e:
        print(f"Error writing to file: {e}")


def search(search_with, search_data):
    results = []

    try:
        with open(FILE_NAME, "r") as data_file:
            players_data = csv.DictReader(data_file)
            for player in players_data:
                if player[search_with] == search_data:
                    results.append(player)
    except Exception as e:
        print(f"Error reading file: {e}")

    if results:
        for player in results:
            print(player)
    else:
        print("No matching player found.")


def delete(backnumber):
    lines = []

    try:
        with open(FILE_NAME, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row and row[0] != backnumber:
                    lines.append(row)
    except Exception as e:
        print(f"Error reading file: {e}")

    try:
        with open(FILE_NAME, 'w', newline='') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    except Exception as e:
        print(f"Error writing to file: {e}")


def edit():
    backnumber = input("Enter a player's backnumber you want to edit: ")
    delete(backnumber)
    add(backnumber)


def display_table():
    try:
        with open(FILE_NAME) as fp:
            mytable = from_csv(fp)
            print(mytable)
    except Exception as e:
        print(f"Error reading file: {e}")


def main():
    ask = input("Do you want to start(yes/no)?: ").strip().lower()

    while ask == 'yes':
        clear()
        user_role = input("Who Are you(coach/fan)?: ").strip().lower()

        if user_role == 'coach':
            password = input("Enter the coach's password: ")

            if password == COACH_PASSWORD:
                action = input(
                    "Do you want to (add/search/delete/edit) player?: ").strip(
                    ).lower()

                if action == "add":
                    clear()
                    with open(FILE_NAME) as file:
                        reader = csv.reader(file)
                        lines = len(list(reader))
                    add(lines)
                    display_table()
                    print("YOUR PLAYER BACKNUMBER IS", lines)
                    print("Done")

                elif action == 'search':
                    clear()
                    search_with = input(
                        "What do you want to search player with? (backnumber/name/team/age): "
                    ).strip().lower()
                    search_data = input(
                        f"Enter the {search_with} of the player: ").strip()
                    search(search_with, search_data)

                elif action == 'delete':
                    clear()
                    display_table()
                    backnumber = input(
                        "Enter the backnumber you want to delete: ").strip()
                    delete(backnumber)
                    clear()
                    display_table()
                    print("Done")

                elif action == 'edit':
                    clear()
                    display_table()
                    edit()
                    clear()
                    display_table()
                    print("Done")

                else:
                    print("Invalid action")

            else:
                print("Wrong Password")

        elif user_role == 'fan':
            print("YOU CAN ONLY SEARCH IF YOU ARE JUST A FAN")
            search_with = input(
                "What do you want to search player with? (backnumber/name/team/age): "
            ).strip().lower()
            search_data = input(
                f"Enter the {search_with} of the player: ").strip()
            search(search_with, search_data)

        else:
            print("Invalid role")

        ask = input("Do you want to start again? (yes/no): ").strip().lower()

    if ask == 'no':
        print("OK")


if __name__ == "__main__":
    main()
