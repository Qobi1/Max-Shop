import requests as re
from shop.settings import API_URL


def get_ctg(page):
    print(page)
    if not page:
        page = 1
    url = API_URL + f'category/?page={page}'
    ctg = re.get(url)
    if ctg.status_code == 200:
        return ctg.json()
    return False


def get_one(pk=None, delete=None):
    url = API_URL + f'category/{pk or delete}'
    if delete:
        ctg = re.delete(url)
    else:
        ctg = re.get(url)

    if ctg.status_code == 200:
        return ctg.json()
    return False