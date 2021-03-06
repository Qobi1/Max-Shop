from contextlib import closing

from django.db import connection

from shop.settings import PAGINATE_BY
from api.v1.sqlpaginator import *


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
    # To filter ctg
    try:
        params = requests.query_params('product')
    except:
        params = None
    print('\n\n\n',params)
    if params:
        extra_sql = 'where '
        for i in params:
            if i == params[-1]:
                extra_sql += f"(content like '%{i}%')"
            else:
                extra_sql += f"(content like '%{i}%') or "
    # End of filter part
    else:
        extra_sql = ''
    page = requests.query_params.get('page', 1)
    sql = f"""Select pp.*, ctg.content as ctg_content from shop_app_product pp
            inner join shop_app_category ctg on ctg.id = pp.ctg_id
             {extra_sql}
            order by id
            limit %s OFFSET %s
            """

    offset = (int(page) - 1) * PAGINATE_BY
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [PAGINATE_BY, offset])
        result = dictfetchall(cursor)

    with closing(connection.cursor()) as cursor:

        cursor.execute(f'''Select count(1) as cnt from shop_app_product {extra_sql}''')
        root = dictfetchone(cursor)
        if root:
            cnt = root['cnt']
        else:
            cnt = 0
    sqlpaginator = SqlPaginator(requests, page=page, per_page=PAGINATE_BY, count=cnt)
    pagging = sqlpaginator.get_paginated_response(per_page=PAGINATE_BY, current_page=page)

    return OrderedDict([
        ('items', result),
        ('meta', pagging)
    ])


def get_one(requests, pk=None):
    sql = '''Select pp.*, ctg.content as ctg_content from shop_app_product pp
            inner join shop_app_category ctg on ctg.id = pp.ctg_id 
            where id=%s
            '''

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        result = dictfetchone(cursor)
        if result:
            response = _format(result)
        else:
            response = None

    return response


def _format(data):
    return OrderedDict([
        ('content', data['content']),
        ('ctg', data['ctg_content']),
        ('real_price', data['real_price']),
        ('discount_price', data['discount_price']),
        ('image', data['image']),
        ('availibility', data['availibility']),
        ('rate', data['rate']),
        ('short_info', data['short_info']),
        ('color', data['color']),
        ('size', data['size']),
        ('description', data['description']),
    ])