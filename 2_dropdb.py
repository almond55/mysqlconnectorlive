from connect import connect

def drop(dbname=None):
    mydb = connect()
    cursor = mydb.cursor()

    try:
        cursor.execute(
            "DROP DATABASE %s" % dbname
        )
        print("Database %s has been dropped." % dbname)
    except Exception as e:
        print(e)

    cursor.execute("SHOW DATABASES")

    for x in cursor:
        print(x)


if __name__ == "__main__":
    drop('mysqltutorial')


