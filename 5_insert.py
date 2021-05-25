from connectdb import connect

def insert(table=None, fields=None, values=None):
    # table = str
    # fields = list
    mydb = connect()
    cursor = mydb.cursor()

    val_list = []
    for x in fields:
        val_list.append("%s")

    fields = (',').join(fields)

    sql = "INSERT INTO %s (%s) VALUES " % (table, fields)
    sql += " (%s)" % (',').join(val_list)

    try:
        cursor.executemany(sql, values)
        mydb.commit()
        print(cursor.rowcount, "record(s) inserted into %s" % table)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    fields = ['name', 'staffid', 'department']
    values = [
        ('Ahmad', 2303, 'IT'),
        ('Maria', 3009, 'HR'),
        ('Lee', 2444, 'Marketing'),
    ]
    insert(table='staff', fields=fields, values=values)
