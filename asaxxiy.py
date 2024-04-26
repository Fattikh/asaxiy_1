import requests
import bs4

def scrapper(product):
    url = f"https://asaxiy.uz/product?key={product}"

    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml)

    products = soup.select('body > main > section > div > div > div.col-lg-9.col-md-12 > div.row.custom-gutter.mb-40')

    for product in products:
        name = product.find('h2', class_='product-name').text.strip()

    # Находим цену товара
        price = product.find('span', class_='product-price').text.strip()

    # Выводим информацию о товаре
        print("Название товара:", name)
        print("Цена товара:", price)
        print("-----------------------------------")
        else:
        print("Ошибка при запросе к веб-сайту")


scrapper('iphone')
