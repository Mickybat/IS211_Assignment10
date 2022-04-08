import sqlite3

con = sqlite3.connect('artist.db')

with con:

    c = con.cursor()

    c.execute("DROP TABLE IF EXISTS artist")
    c.execute("CREATE TABLE artist(name TEXT)")
    c.execute("INSERT INTO artist VALUES('Drake')")
    c.execute("INSERT INTO artist VALUES('Justin Bieber')")
    c.execute("INSERT INTO artist VALUES('Giveon')")
    c.execute("INSERT INTO artist VALUES('Olivia Rodrigo')")
    c.execute("INSERT INTO artist VALUES('Taylor Swift')")

    c.execute("DROP TABLE IF EXISTS albums")
    c.execute("CREATE TABLE albums(album TEXT, singer TEXT)")
    c.execute("INSERT INTO albums VALUES('Certified Lover Boy','Drake')")
    c.execute("INSERT INTO albums VALUES('Justice','Justin Bieber')")
    c.execute("INSERT INTO albums VALUES('Take Time','Giveon')")
    c.execute("INSERT INTO albums VALUES('Sour','Olivia Rodrigo')")
    c.execute("INSERT INTO albums VALUES('Red','Taylor Swift')")

    c.execute("DROP TABLE IF EXISTS songs")
    c.execute("CREATE TABLE songs(song TEXT, album TEXT, track INTEGER, play time INTEGER)")
    c.execute("INSERT INTO songs VALUES('No Friends In The Industry', 'Certified Lover Boy', 12, 204)")
    c.execute("INSERT INTO songs VALUES('2 Much', 'Justice', 1, 152)")
    c.execute("INSERT INTO songs VALUES('Heartbreak Anniversary', 'Take Time', 6, 198)")
    c.execute("INSERT INTO songs VALUES('Drivers License', 'Sour', 3,241)")
    c.execute("INSERT INTO songs VALUES('All Too Well', 'Red', 5, 329)")


def get_songs():

    c.execute("SELECT * FROM songs")
    print(c.fetchall())

get_songs()
