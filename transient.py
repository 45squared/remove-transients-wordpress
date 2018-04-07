import datetime
import mysql.connector
import sys

# define variables
cnx = mysql.connector.connect(user='DB_USERNAME', host='DB_ADDRESS', database='DB_NAME', password='DB_USER_PASSWORD')
cursor = cnx.cursor()
now = datetime.datetime.now()
query = ("DELETE FROM `wp_options` WHERE `autoload` = 'yes' AND `option_name` LIKE '%transient%';")
sys.stdout = open("transient_delete_log.log", "a")

#execute query
cursor.execute(query)


#commit changes
cnx.commit()

print now, "Deleted", cursor.rowcount, "lines."

cnx.close