import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

TOKEN = '6058611210:AAERgNFPmY5dZzNOE4ulhdQUyzPeOAfwWcU'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1 = types.KeyboardButton(text="🧖‍♀️Косметики для женщины")
    keyboard2 = types.KeyboardButton(text="👨🏻Дезодоранты для мужчины")
    keyboard3 = types.KeyboardButton(text="👦Подгузники для детей")
    keyboard4 = types.KeyboardButton(text="👩🏼Краска для волос")
    keyboard5 = types.KeyboardButton(text="🧖🏽‍♂️Шампуни и гели для мужчины")
    keyboard6 = types.KeyboardButton(text="👦🏻Детская зубная паста")
    markup.add(keyboard1, keyboard2, keyboard3, keyboard4, keyboard5, keyboard6)
    bot.send_message(chat_id, f"Привет {first_name} !\nДобро пожаловать! в магазин Aloe.kg\nЧто хотите выбрать?",
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def text(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == '🧖‍♀️Косметики для женщины':
            link = "http://www.aloe.kg"
            url = "http://www.aloe.kg/catalog/category/view/54.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            section = soup.find_all("div", class_="jshop list_product")
            for products in section:
                product = products.find_all("div", class_="sblock4")
                for item in product:
                    product_name = item.find("div", class_="name").get_text(strip=True)
                    product_price = item.find("div", class_="jshop_price").get_text(strip=True)
                    product_link = link + item.find("a").get("href")
                    all_products = f"Название товара: {product_name}\nЦена: {product_price}\nСсылка на продукт: {product_link}\nСсылка на сайт:{link}"
                    bot.send_message(chat_id, all_products)

        if message.text == '👨🏻Дезодоранты для мужчины':
            link = "http://www.aloe.kg"
            url = "http://www.aloe.kg/catalog/category/view/59.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            section = soup.find_all("div", class_="jshop list_product")
            for products in section:
                product = products.find_all("div", class_="sblock4")
                for item in product:
                    product_name = item.find("div", class_="name").get_text(strip=True)
                    product_price = item.find("div", class_="jshop_price").get_text(strip=True)
                    product_link = link + item.find("a").get("href")
                    all_products = f"Название товара: {product_name}\nЦена: {product_price}\nСсылка на продукт: {product_link}\nСсылка на сайт:{link}"
                    bot.send_message(chat_id, all_products)

        if message.text == '👦Подгузники для детей':
            link = "http://www.aloe.kg"
            url = "http://www.aloe.kg/catalog/category/view/103.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            section = soup.find_all("div", class_="jshop list_product")
            for products in section:
                product = products.find_all("div", class_="sblock4")
                for item in product:
                    product_name = item.find("div", class_="name").get_text(strip=True)
                    product_price = item.find("div", class_="jshop_price").get_text(strip=True)
                    product_link = link + item.find("a").get("href")
                    all_products = f"Название товара: {product_name}\nЦена: {product_price}\nСсылка на продукт: {product_link}\nСсылка на сайт:{link}"
                    bot.send_message(chat_id, all_products)

        if message.text == '👩🏼Краска для волос':
            link = "http://www.aloe.kg"
            url = "http://www.aloe.kg/catalog/category/view/61.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            section = soup.find_all("div", class_="jshop list_product")
            for products in section:
                product = products.find_all("div", class_="sblock4")
                for item in product:
                    product_name = item.find("div", class_="name").get_text(strip=True)
                    product_price = item.find("div", class_="jshop_price").get_text(strip=True)
                    product_link = link + item.find("a").get("href")
                    all_products = f"Название товара: {product_name}\nЦена: {product_price}\nСсылка на продукт: {product_link}\nСсылка на сайт:{link}"
                    bot.send_message(chat_id, all_products)

        if message.text == '🧖🏽‍♂️Шампуни и гели для мужчины':
            link = "http://www.aloe.kg"
            url = "http://www.aloe.kg/catalog/category/view/62.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            section = soup.find_all("div", class_="jshop list_product")
            for products in section:
                product = products.find_all("div", class_="sblock4")
                for item in product:
                    product_name = item.find("div", class_="name").get_text(strip=True)
                    product_price = item.find("div", class_="jshop_price").get_text(strip=True)
                    product_link = link + item.find("a").get("href")
                    all_products = f"Название товара: {product_name}\nЦена: {product_price}\nСсылка на продукт: {product_link}\nСсылка на сайт:{link}"
                    bot.send_message(chat_id, all_products)

        if message.text == '👦🏻Детская зубная паста':
            link = "http://www.aloe.kg"
            url = "http://www.aloe.kg/catalog/category/view/19.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            section = soup.find_all("div", class_="jshop list_product")
            for products in section:
                product = products.find_all("div", class_="sblock4")
                for item in product:
                    product_name = item.find("div", class_="name").get_text(strip=True)
                    product_price = item.find("div", class_="jshop_price").get_text(strip=True)
                    product_link = link + item.find("a").get("href")
                    all_products = f"Название товара: {product_name}\nЦена: {product_price}\nСсылка на продукт: {product_link}\nСсылка на сайт:{link}"
                    bot.send_message(chat_id, all_products)


bot.polling(none_stop=True)
