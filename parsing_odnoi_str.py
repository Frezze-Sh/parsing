import requests
from requests import Session
from bs4 import BeautifulSoup
import xlsxwriter
from concurrent.futures import ThreadPoolExecutor
import time

start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

work = Session()

def parsing_one_product(iter):
    list_data_product = []

    url = f"https://books.toscrape.com/catalogue/page-{iter}.html"
    response = work.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    data_products_in_page = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for product in data_products_in_page:
        name = product.find("h3").text
        price = product.find("p", class_="price_color").text
        link_img = "https://books.toscrape.com/" + product.find("img").get("src").replace("../", "")
        link_product = "https://books.toscrape.com/catalogue" + product.find("a").get("href")

        list_data_product.append({
            "name": name,
            "price": price,
            "link_img": link_img,
            "link_product": link_product
        })

    return list_data_product

def save_to_excel(products):
    book = xlsxwriter.Workbook(r"\Users\orazl\Desktop\parsing.xlsx")
    page = book.add_worksheet("товары")

    page.write(0, 0, "Название")
    page.write(0, 1, "Цена")
    page.write(0, 2, "Ссылка на изображение")
    page.write(0, 3, "Ссылка на товар")

    # Данные
    row = 1
    for item in products:
        page.write(row, 0, item["name"])
        page.write(row, 1, item["price"])
        page.write(row, 2, item["link_img"])
        page.write(row, 3, item["link_product"])
        row += 1

    # Настройки колонок
    page.set_column("A:A", 40)
    page.set_column("B:B", 15)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    book.close()

# with ThreadPoolExecutor(max_workers=5) as executor:
#     list_with_data_products = list(executor.map(all_info_products_in_pages,range(1,11)))

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(parsing_one_product, range(1,50)))

all_products = []

for product in results:
    all_products.extend(product)
save_to_excel(all_products)

end_time = time.time()
execution_time = end_time - start_time

print(f"Время выполнения: {execution_time:.2f} секунд")
print(f"Спаршено товаров: {len(all_products)}")