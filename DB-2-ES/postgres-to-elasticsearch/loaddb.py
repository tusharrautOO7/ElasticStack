import csv
import psycopg2

conn = psycopg2.connect("host=localhost dbname=test user=postgres password=xxxx")
cur = conn.cursor()
print "Connection Opened !!"
i = 0
with open('contacts.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    i+=1
    for row in reader:
        cur.execute(
            "INSERT INTO contacts(name, email, mob, company, designation) VALUES (%s, %s, %s, %s, %s)",
            row
        )

print "Data Loaded Successfully."
conn.commit()
conn.close()

print "Connection Closed!!"
