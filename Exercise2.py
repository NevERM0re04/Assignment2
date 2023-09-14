import sqlite3

def create_database_and_table():
    # Establish a connection with a new SQLite database
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
                      (movieID TEXT, movieName TEXT, movieYear INTEGER, imdbRating REAL)''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_data_from_file():
    # Read the content from stephen_king_adaptations.txt and copy it to the database
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    with open('stephen_king_adaptations.txt', 'r') as file:
        for line in file:
            movie_id, movie_name, movie_year, imdb_rating = line.strip().split(',')
            cursor.execute('INSERT INTO stephen_king_adaptations_table VALUES (?, ?, ?, ?)',
                           (movie_id, movie_name, int(movie_year), float(imdb_rating)))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def search_movie_by_name():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    movie_name = input("Enter the name of the movie: ")
    cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?', (movie_name,))
    result = cursor.fetchone()

    if result:
        print("Movie Found:")
        print(f"Movie Name: {result[1]}")
        print(f"Movie Year: {result[2]}")
        print(f"IMDB Rating: {result[3]}")
    else:
        print("No such movie exists in our database")

    conn.close()

def search_movie_by_year():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    movie_year = int(input("Enter the year: "))
    cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?', (movie_year,))
    results = cursor.fetchall()

    if results:
        print("Movies Found:")
        for result in results:
            print(f"Movie Name: {result[1]}")
            print(f"Movie Year: {result[2]}")
            print(f"IMDB Rating: {result[3]}")
    else:
        print("No movies were found for that year in our database.")

    conn.close()

def search_movie_by_rating():
    conn = sqlite3.connect('stephen_king_adaptations.db')
    cursor = conn.cursor()

    rating_limit = float(input("Enter the minimum rating: "))
    cursor.execute('SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?', (rating_limit,))
    results = cursor.fetchall()

    if results:
        print("Movies Found:")
        for result in results:
            print(f"Movie Name: {result[1]}")
            print(f"Movie Year: {result[2]}")
            print(f"IMDB Rating: {result[3]}")
    else:
        print("No movies at or above that rating were found in the database.")

    conn.close()

if __name__ == "__main__":
    create_database_and_table()
    insert_data_from_file()

    while True:
        print("\nOptions:")
        print("1. Search by Movie Name")
        print("2. Search by Movie Year")
        print("3. Search by Movie Rating")
        print("4. STOP")

        choice = input("Enter your choice: ")

        if choice == '1':
            search_movie_by_name()
        elif choice == '2':
            search_movie_by_year()
        elif choice == '3':
            search_movie_by_rating()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")