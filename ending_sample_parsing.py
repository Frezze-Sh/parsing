import requests
from requests import Session
from bs4 import BeautifulSoup
import xlsxwriter
from concurrent.futures import ThreadPoolExecutor
import time

start_time = time.time()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
work = Session()

# def download_images(img_urls):
##     Скачивание изображений с многопоточностью
#
#     def download_single(img_url):
#         resp = requests.get(img_url, stream=True)
#         filename = img_url.split("/")[-1]
#         with open(f"C:\\Users\\orazl\\Desktop\\image\\{filename}", "wb") as f:
#             for value in resp.iter_content(1024 * 1024):
#                 f.write(value)
#         return True
#
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         results = list(executor.map(download_single, img_urls))
#
#     print(f"Загружено {len(results)} изображений")

def get_card_urls():
    #Получение всех URL карточек товаров
    card_url_list = []
    for count in range(1, 3):
        url = f"https://books.toscrape.com/catalogue/page-{count}.html"
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for i in data:
            card_url = "https://books.toscrape.com/catalogue/" + i.find("a").get("href").replace("../", "")
            card_url_list.append(card_url)

    print(f"Найдено {len(card_url_list)} карточек товаров")
    return card_url_list

def parse_single_card(card_url):
    """Парсинг одной карточки товара"""
    response = requests.get(card_url)
    soup = BeautifulSoup(response.text, "lxml")

    name_price = soup.find("div", class_="col-sm-6 product_main")
    img_link_data = soup.find("div", class_="item active")

    name = name_price.find("h1").text
    price = name_price.find("p", class_="price_color").text
    img_link = "https://books.toscrape.com/" + img_link_data.find("img").get("src").replace("../", "")

    return {
        "name": name,
        "price": price,
        "img_link": img_link,
        "url": card_url
    }

def parse_all_cards_fast():
    #Быстрый парсинг всех карточек с многопоточностью"""

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(parse_single_card, get_card_urls()))

    # img_urls = [result["img_link"] for result in results]
    # download_images(img_urls)

    return results

def write_to_excel(data):
    """Запись всех данных в Excel"""
    book = xlsxwriter.Workbook(r"C:\Users\orazl\Desktop\parsing.xlsx")
    page = book.add_worksheet("товары")

    page.set_column("A:A", 50)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 50)

    page.write(0, 0, "Название")
    page.write(0, 1, "Цена")
    page.write(0, 2, "Ссылка на изображение")
    page.write(0, 3, "Ссылка на товар")

    for row, item in enumerate(data, 1):
        page.write(row, 0, item["name"])
        page.write(row, 1, item["price"])
        page.write(row, 2, item["img_link"])
        page.write(row, 3, item["url"])

    book.close()
    print(f"Сохранено {len(data)} товаров в Excel")

write_to_excel(parse_all_cards_fast())

end_time = time.time()
execution_time = end_time - start_time
print(f"Общее время выполнения: {execution_time:.2f} секунд")