from connect import connect

def create(dbname=None):
    mydb = connect()
    cursor = mydb.cursor()

    try:
        cursor.execute(
            "CREATE DATABASE %s" % dbname
        )
        print("Database %s created." % dbname)
    except Exception as e:
        print(e)

    cursor.execute("SHOW DATABASES")

    for x in cursor:
        print(x)


if __name__ == "__main__":
    create('mysqltutorial')


