from connectdb import connect

def create(table=None, data=None):
    # table = str
    # data = dict {'key':'value'}
    mydb = connect()
    cursor = mydb.cursor()

    schema = None
    for item in data:
        if not schema:
            schema = "%s %s" % (item, data[item])
        else:
            schema += ", %s %s" % (item, data[item])

    sql = "CREATE TABLE %s (%s)" % (table, schema)

    try:
        cursor.execute(sql)
        print("Table %s created." % table)
    except Exception as e:
        print(e)

    try:
        cursor.execute("DESCRIBE %s" % table)
        for x in cursor:
            print(x)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    data = {
        'name': 'VARCHAR(255)',
        'staffid': 'INT',
        'department': 'VARCHAR(255)',
    }
    create(table='staff', data=data)
