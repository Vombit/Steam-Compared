from bs4 import BeautifulSoup
import requests
import json
import re

# START STEAM
url_skin = input('Enter steam url: ')
# url_skin = "https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Phantom%20Disruptor%20%28Field-Tested%29"
url_req = requests.get(url_skin)
name_page_skin = str(BeautifulSoup(url_req.text, 'html.parser').title.text)[39:]

regular_result = re.findall(r'Market_LoadOrderSpread\(\s*(\d+)\s*\)', str(url_req.content))
response = requests.get(f"https://steamcommunity.com/market/itemordershistogram?country=RU&language=russian&currency=5&item_nameid={regular_result[0]}&two_factor=0")
parsed_string = json.loads(response.content)

parsed_str_buy = parsed_string['buy_order_table']
soup_buy = str(BeautifulSoup(parsed_str_buy, 'html.parser').table.td.text)

parsed_str_sell = parsed_string['sell_order_table']
soup_sell = str(BeautifulSoup(parsed_str_sell, 'html.parser').table.td.text)
coefSteam = 100*87
print('\nSteam\n\n', 
        name_page_skin, '\n', 
        url_skin, 
        '\n\nBuy by:', soup_buy, float((soup_buy[:-5]).replace(',','.'))*0.87,
        '\nSell by:', soup_sell, float((soup_sell[:-5]).replace(',','.'))*0.87,
        '\n\n')
# END STEAM
# START MARKET CS_GO
url_skin_market = f"https://market.csgo.com/?s=price&search={name_page_skin}&sd=asc"
url_req_market  = requests.get(url_skin_market)
name_page_skin_market = BeautifulSoup(url_req_market.content, 'html.parser')

results = name_page_skin_market.find(id="applications")
low_price = results.find("div", class_="price")
# https://market.csgo.com/sell/minprice/4639215245-480085569

print('\nMarket CS-GO\n\n', 
        name_page_skin, '\n', 
        url_skin_market.replace(' ','%20'), 
        '\n\nBuy by:', 'NONE',
        '\nSell by:', low_price.text,
        '\n\n')
# END MARKET CS_GO
# STEAM INVENTORY
nickname = " "
url_steam_inventory = f"https://steamcommunity.com/id/{nickname}/inventory/json/730/2"

inventory_req = requests.get(url_steam_inventory)
inventory_data = BeautifulSoup(inventory_req.content, 'html.parser')

# print(inventory_data)

# STEAM INVENTORY