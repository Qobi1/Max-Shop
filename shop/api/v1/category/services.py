




def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_list(requests):
    params = requests.query_params('ctg')
    print('>>>>>>>>>', params)
    if params:
        extra_sql = 'where '
        for i in params:
            if i == params[-1]:
                extra_sql += f"(content like '%{i}%')"
            else:
                extra_sql += f"(content like '%{i}%') or "
    else:
        extra_sql += ''







