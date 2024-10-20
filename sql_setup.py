import sqlite3

connection = sqlite3.connect("sample.db")


cursor = connection.cursor()

table_info = '''
CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
'''

cursor.execute(table_info)

insert_query = '''
INSERT INTO users (name, age) VALUES
('Alice', 30),
('Bob', 25),
('Charlie', 35);
'''

cursor.execute(insert_query)


data = cursor.execute('''select * from users''')
print("Row data: ")
for row in data:
    print(row)
connection.commit()
connection.close()