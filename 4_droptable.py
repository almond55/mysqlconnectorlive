from connectdb import connect

def drop(table=None):
    mydb = connect()
    cursor = mydb.cursor()

    try:
        cursor.execute(
            "DROP TABLE %s" % table
        )
        print("Table %s has been dropped." % table)
    except Exception as e:
        print(e)

    cursor.execute("SHOW TABLES")

    for x in cursor:
        print(x)


if __name__ == "__main__":
    drop('staff')


