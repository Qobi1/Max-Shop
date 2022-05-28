from shop.settings import API_URL
import requests as re


def get_product(page):
    if not page:
        page = 1
    url = API_URL + f'product/?page={page}'
    product = re.get(url)
    if product.status_code == 200:
        return product.json()
    return False


def get_one(pk=None, delete=None):
    url = API_URL + f'product/{pk or delete}'
    if delete:
        product = re.delete(url)
    else:
        product = re.get(url)

    if product.status_code == 200:
        return product.json()
    return False

