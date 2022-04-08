import sqlite3

con = sqlite3.connect('pets.db')

with con:

    c = con.cursor()


def user_input():
    id_number = 0

    while id_number <= 0:
        try:
            id_number = int(input("What is your ID number?"))
            if id_number < 1:
                print("Please enter a valid ID number")
        except ValueError:
            print("Please enter a number for ID number")
        if id_number == -1:
            break

    return id_number


def data_base():
    user = 0

    while(user != -1):
        user = user_input()
        if user == 1:
            c.execute("SELECT first_name, last_name, age, name, breed, years FROM person, pet WHERE person.id = 1 and pet.id = 1")
            user1 = c.fetchall()
            for row in user1:
                print(row[0], row[1], 'is the owner of', row[3], 'a,', row[4], 'that is', row[5], 'years old')

        elif user == 2:
            c.execute("SELECT first_name, last_name, age, name, breed, years FROM person, pet WHERE person.id = 1 and pet.id = 2")
            user1 = c.fetchall()
            for row in user1:
                print(row[0], row[1], 'is the owner of', row[3], 'an,', row[4], 'that is', row[5], 'years old')

        elif user == 3:
            c.execute("SELECT first_name, last_name, age, name, breed, years FROM person, pet WHERE person.id = 2 and pet.id = 3")
            user1 = c.fetchall()
            for row in user1:
                print(row[0], row[1], 'is the owner of', row[3], 'a,', row[4], 'that is', row[5], 'years old')

        elif user == 4:
            c.execute("SELECT first_name, last_name, age, name, breed, years FROM person, pet WHERE person.id = 2 and pet.id = 4")
            user1 = c.fetchall()
            for row in user1:
                print(row[0], row[1], 'is the owner of', row[3], 'a,', row[4], 'that is', row[5], 'years old')

        elif user == 5:
            c.execute("SELECT first_name, last_name, age, name, breed, years FROM person, pet WHERE person.id = 3 and pet.id = 5")
            user1 = c.fetchall()
            for row in user1:
                print(row[0], row[1], 'is the owner of', row[3], 'a,', row[4], 'that is', row[5], 'years old')

        elif user == 6:
            c.execute("SELECT first_name, last_name, age, name, breed, years FROM person, pet WHERE person.id = 4 and pet.id = 6")
            user1 = c.fetchall()
            for row in user1:
                print(row[0], row[1], 'is the owner of', row[3], 'a,', row[4], 'that is', row[5], 'years old')
        else:
            print("ID NOT FOUND")


if __name__ == "__main__":
    data_base()



