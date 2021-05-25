from connectdb import connect

def select(
        table=None, 
        fields=None, 
        where=None, 
        condition='OR', 
        orderby=None,
        limit=None
    ):
    # table=str
    # fields=list
    # where=dict
    # condition=str ('AND'/ 'OR')
    # orderby=str
    # limit=int
    mydb = connect()
    cursor = mydb.cursor()

    if not fields:
        fields = "*"
    else:
        fields = (',').join(fields)

    sql = "SELECT %s FROM %s" % (fields, table)

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

    if orderby:
        sql += " ORDER BY %s" % orderby 

    if limit:
        sql += " LIMIT %s" % limit

    print(sql)
    
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)
    
    try:
        result = cursor.fetchall()
        for x in result:
            print(x)
    except Exception:
        pass


if __name__ == "__main__":
    fields = ['department']
    where = {
        'name': 'Lee',
        'department': 'HR',
    }
    condition = 'AND'
    orderby = 'staffid'
    limit = 1
    select(table='staff')






#SELECT * FROM staff LIMIT 2
