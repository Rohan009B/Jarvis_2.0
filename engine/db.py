import _sqlite3
import csv

con = _sqlite3.connect("jarvis2_0.db")
cursor = con.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'bing','C:\\Users\\DC\\OneDrive\\Desktop\\Bing.lnk')"
# cursor.execute(query)
# con.commit()

# query = "INSERT INTO sys_command VALUES (null,'notepad++','C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++.lnk')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'love pdf','https://www.ilovepdf.com/index.php')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)"
# cursor.execute(query)

#impoerting The CSV file Here

desired_colomns_indices = [0 ,20]

#Read Data From THe CSV FILE
with open('contacts.csv','r',encoding='utf-8') as csvfile:
    csvrender = csv.render(s=csvfile)
    for row in csvrender:
        selected_data = [row[i] for i in desired_colomns_indices]
        cursor.execute(''' INSERT INTO contacts ('id', 'name', 'mobile_no') VALUES (null, ?, ?); ''', tuple(selected_data))

#commiit Changes and CLose COnnection
con.commit()
con.close()