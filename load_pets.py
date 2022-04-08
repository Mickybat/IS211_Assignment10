import sqlite3

con = sqlite3.connect('pets.db')

with con:

    c = con.cursor()

    c.execute("DROP TABLE IF EXISTS person")
    c.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
    c.execute("INSERT INTO person VALUES(1, 'James', 'Smith', 41)")
    c.execute("INSERT INTO person VALUES(2, 'Diana', 'Greene', 23)")
    c.execute("INSERT INTO person VALUES(3, 'Sara', 'White', 27)")
    c.execute("INSERT INTO person VALUES(4, 'William', 'Gibson', 23)")

    c.execute("DROP TABLE IF EXISTS pet")
    c.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY, name TEXT, breed TEXT, years INTEGER, dead INTEGER)")
    c.execute("INSERT INTO pet VALUES(1, 'Rusty', 'Dalmation', 4, 1)")
    c.execute("INSERT INTO pet VALUES(2, 'Bella', 'Alaskan Malute', 3, 0)")
    c.execute("INSERT INTO pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0)")
    c.execute("INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0)")
    c.execute("INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0)")
    c.execute("INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1)")

    c.execute("DROP TABLE IF EXISTS person_pet")
    c.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGER)")
    c.execute("INSERT INTO person_pet VALUES(1, 1)")
    c.execute("INSERT INTO person_pet VALUES(1, 2)")
    c.execute("INSERT INTO person_pet VALUES(2, 3)")
    c.execute("INSERT INTO person_pet VALUES(2, 4)")
    c.execute("INSERT INTO person_pet VALUES(3, 5)")
    c.execute("INSERT INTO person_pet VALUES(4, 6)")

"""PART 2 QUESTION 2: 
The Purpose of the pet_person table is to show the link between the pets with their respective owners."""

