import requests
from requests import Session
from bs4 import BeautifulSoup
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

work = Session()# Можно и без него (можно, как обычно, до этого с помощью запросов (get и.д.)),
# но с ним не нужно париться по поводу файлов куки

work.get("https://quotes.toscrape.com", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")
data = {"csrf_token":token,"username":"noname","password":"password"}
result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)


# def download(url):
#     resp = requests.get(url, stream=True)
#     filename = url.split("/")[-1]
#     r = open(f"C:\\Users\\orazl\\Desktop\\image\\" + url.split("/")[-1], "wb")
#     for value in resp.iter_content(1024*1024):
#         r.write(value)
#     r.close()


def get_url():
    count_page = 1
    while True:# for count in range(1,count_page):
        sleep(1)
        url = f"https://quotes.toscrape.com/page/{count_page}"
        response1 = work.get(url, headers=headers)  # для ответа от сайта
        soup = BeautifulSoup(response1.text, "lxml")
        data = soup.find_all("div", class_="quote")
        if not data:
            print(f"На странице {count_page} нет цитат. Завершаем.")
            break

        print(f"Обрабатываем страницу {count_page}, найдено {len(data)} цитат")

        for i in data:
            citate = i.find("span").text
            author = i.find("small").text
            count_page += 1

            yield citate, author

        # for i in data:
        #     card_url = "https://books.toscrape.com/catalogue/"+i.find("a").get("href").replace("../","")
        #     yield card_url

# def array():
#     for card_url in get_url():
#         response = requests.get(card_url)  # для ответа от сайта
#         soup = BeautifulSoup(response.text, "lxml")
#         name_price = soup.find("div", class_="col-sm-6 product_main")
#         # description_data = soup.find("div", id="product_description")
#         img_link_data = soup.find("div", class_="item active")
#
#         name = name_price.find("h1").text
#         price = name_price.find("p").text
#         # description = description_data.find_next_sibling("p").text
#         img_link = "https://books.toscrape.com/" + img_link_data.find("img").get("src").replace("../", "")
#         # download(img_link)
#         yield name, price, img_link
