from connectdb import connect

def delete(table=None, where=None):
    # table=str
    # where=dict
    mydb = connect()
    cursor = mydb.cursor()

    sql = "DELETE FROM %s" % table

    if where:
        for lookup in where:
            if '%' in where[lookup]:
                operator = 'LIKE'
            else:
                operator = '='
            if 'WHERE' not in sql:
                sql += " WHERE %s %s '%s'" % (
                    lookup, operator, where[lookup]
                )
            else:
                sql += " %s %s %s '%s'" % (
                    condition, lookup, operator, where[lookup]
                )
    try:
        cursor.execute(sql)
        mydb.commit()
    except Exception as e:
        print(e)

    print(cursor.rowcount, "row(s) deleted from %s" % table)


if __name__ == "__main__":
    table = 'staff'
    where = {
        'name': 'Ahmad',
    }
    delete(table=table, where=where)



# DELETE FROM staff WHERE name = 'Ahmad' AND 