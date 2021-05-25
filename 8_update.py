from connectdb import connect

def update(table=None, alter=None, where=None):
    # table=str
    # alter=dict
    # where=dict
    mydb = connect()
    cursor = mydb.cursor()

    sql = "UPDATE %s" % table

    values = []

    for lookup in alter:
        if 'SET' not in sql:
            sql += " SET %s =" % lookup
        else:
            sql += ", %s =" % lookup
        sql += "%s"
        values.append(alter[lookup])

    if where:
        for lookup in where:
            if '%' in where[lookup]:
                operator = 'LIKE'
            else:
                operator = '='
            if 'WHERE' not in sql:
                sql += " WHERE %s %s " % (
                    lookup, operator
                )
            else:
                sql += " %s %s %s " % (
                    condition, lookup, operator
                )
            sql += "%s"
            values.append(where[lookup])

    try:
        cursor.execute(sql, values)
        mydb.commit()
    except Exception as e:
        print(e)

    print(cursor.rowcount, "entries updated in %s" % table)


if __name__ == "__main__":
    table = 'staff'
    alter = {
        'name': 'Bob',
        'department': 'HR',
    }
    where = {
        'name': 'Lee',
    }
    update(table=table, alter=alter, where=where)


# UPDATE staff SET name = 'Bob', department = 'HR' WHERE name = 'Lee';