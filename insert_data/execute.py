import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="noisebook",
    user="postgres",
    password="islam.31"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()



localisation = input("Enterer la localisation: ")

cursor.execute("""
    SELECT *
    FROM Concert
    WHERE idLieu IN (
        SELECT id
        FROM Lieu
        WHERE localisation = %s
    );
""", (localisation,))

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
conn.close()
