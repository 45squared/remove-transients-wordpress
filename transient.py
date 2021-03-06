import datetime
import mysql.connector
import sys

def usage():
    print('transient.py DB_USERNAME DB_ADDRESS DB_NAME DB_USER_PASSWORD | Pass database credentials as system arguments.')
    print('View README.md for more information. USE AT YOUR OWN RISK')

def main(argv):
    if sys.argv[1] == "help":
        usage()
    elif sys.argv[1] == "-h":
        usage()
    else:
        DB_USERNAME = sys.argv[1]
        DB_ADDRESS = sys.argv[2]
        DB_NAME = sys.argv[3]
        DB_USER_PASSWORD = sys.argv[4]
# Create databse connection
        cnx = mysql.connector.connect(user=DB_USERNAME, host=DB_ADDRESS, database=DB_NAME, password=DB_USER_PASSWORD)
        cursor = cnx.cursor()
        now = datetime.datetime.now()
        query = ("DELETE FROM `wp_options` WHERE `autoload` = 'yes' AND `option_name` LIKE '%transient%';")
        sys.stdout = open("transient_delete_log.log", "a")
#execute query
        cursor.execute(query)
#commit changes
        cnx.commit()
        print(now, "Deleted", cursor.rowcount, "lines.")
        cnx.close
if __name__=='__main__':
    main(sys.argv[1:])
