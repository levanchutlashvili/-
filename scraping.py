from bs4 import BeautifulSoup
import requests
import json

url = "https://www.home.ge/saxlebi-agarakebi/iyideba-saxlebi-agarakebi/iyideba-sakhli-308793.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="col-md-8")
print(lists)

for listing in lists:
    map = listing.find('span', class_="map-group").text
    price = listing.find('span', class_="converted-price")
    m2 = listing.find('span', class_="price_m2").text
    price_m2 = listing.find('span', class_="converted-price")
    hide_m2 = listing.find('span', class_="tmp hide")
    icon_arrow = listing.find('span', class_="arrow").text
    District = listing.find('div', class_="value").text
    title_of_location = listing.find('div', class_="სათაური")
    dasAxeleba = listing.find('div', class_="value").text
    ID_of_statement = listing.find('div', class_="განცხადების ID")
    ID = listing.find('div', class_="value").text
    mob_tel = listing.find('div', class_="მობ. ტელ.")
    phone_number = listing.find('a', href_="tel:(597) 600-009")
    title_of_cadastral_code = listing.find('div', class_="საკადასტრო კოდი")
    cadastral_code = listing.find('div', class_="value").text
    title_location = listing.find('div', class_="ადგილმდებარეობა/მისამართი")
    location = listing.find('div', class_="value").text
    title_of_status = listing.find('div', class_="სტატუსი")
    status = listing.find('div', class_="value").text
    title_of_area = listing.find('div', class_="ფართობი")
    area = listing.find('div', class_="value").text
    title_of_yard_area = listing.find('div', class_="ეზოს ფართობი")
    yard_area = listing.find('div', class_="value").text
    title_of_amount_room = listing.find('div', class_="ოთახების რ-ბა")
    amount_of_room = listing.find('div', class_="value").text
    title_of_bedroom = listing.find('div', class_="საძინებელი")
    bedroom = listing.find('div', class_="value").text
    title_of_bathroom = listing.find('div', class_="სველი წერტილი")
    bathroom = listing.find('div', class_="value").text
    title_of_kitchen_type = listing.find('div', class_="სამზარეულოს ტიპი")
    kitchen_type = listing.find('div', class_="value").text
    title_of_amount_floors = listing.find('div', class_="სართულების რაოდენობა")
    amount_of_floors = listing.find('div', class_="value").text
    title_of_condition = listing.find('div', class_="მდგომარეობა")
    condition = listing.find('div', class_="value").text
    title_of_balcony_terrace = listing.find('div', class_="აივანი/ტერასა")
    balcony_terrace = listing.find('div', class_="value").text
    title_of_lojia = listing.find('div', class_="ლოჯია")
    lojia = listing.find('div', class_="value").text
    title_of_building_material = listing.find('div', class_="სამშენებლო მასალა")
    building_material = listing.find('div', class_="value").text
    title_of_shmp_adapted = listing.find('div', class_="შშმპ ადაპტირებული")
    shmp_adapted = listing.find('div', class_="value").text
    title_of_fireplace = listing.find('div', class_="ბუხარი")
    fireplace = listing.find('div', class_="value").text
    title_of_sauna = listing.find('div', class_="საუნა")
    sauna = listing.find('div', class_="value").text
    title_of_pool = listing.find('div', class_="აუზი")
    pool = listing.find('div', class_="value").text
    title_of_heating = listing.find('div', class_="გათბობა")
    heating = listing.find('div', class_="value").text
    title_of_hot_water = listing.find('div', class_="ცხ. წყალი")
    hot_water = listing.find('div', class_="value").text
    title_of_store_room = listing.find('div', class_="სათავსო")
    wardrobe = listing.find('li', class_="col-xs-12 col-sm-4 active").text
    outdoor_storage = listing.find('li', class_="col-xs-12 col-sm-4 active").text
    shared_storage = listing.find('li', class_="col-xs-12 col-sm-4 active").text
    storage_on_balcony = listing.find('li', class_="col-xs-12 col-sm-4 active").text
    info = [map, price, m2, price_m2, hide_m2, icon_arrow, District, title_of_location, 
dasAxeleba, ID_of_statement, ID, mob_tel, phone_number, 
title_of_cadastral_code,cadastral_code,
title_location, location, status, 
title_of_area, area, title_of_yard_area, 
yard_area, title_of_amount_room, 
amount_of_room, title_of_bedroom, bedroom, title_of_bathroom, bathroom, 
title_of_kitchen_type, kitchen_type, title_of_amount_floors, 
amount_of_floors, title_of_condition, condition, title_of_balcony_terrace, 
 balcony_terrace,title_of_lojia, lojia, title_of_building_material, building_material, 
 title_of_shmp_adapted, shmp_adapted, title_of_fireplace, fireplace, title_of_sauna, sauna, 
 title_of_pool, pool, title_of_heating, heating, title_of_hot_water, hot_water, 
 title_of_store_room, wardrobe, outdoor_storage, shared_storage, storage_on_balcony]
    print(info)
    break

property_info = {
    'map-group':map,
    'converted-price':price,
    'price_m2':m2,
    'converted-price':price_m2,
    'tmp hide':hide_m2,
    'arrow':icon_arrow, 
    'value':District, 
    'სათაური':title_of_location,
    'value':dasAxeleba,
    'განცხადების ID':ID_of_statement,
    'value':ID ,
    'მობ. ტელ.':mob_tel,
    'tel:(597) 600-009':phone_number, 
    'საკადასტრო კოდი':title_of_cadastral_code,
    'value':cadastral_code,
    'ადგილმდებარეობა/მისამართი':title_location,
    'value':location,
    'სტატუსი':title_of_status,
    'value':status,
    'ფართობი':title_of_area,
    'value':area,
    'ეზოს ფართობი':title_of_yard_area,
    'value':yard_area,
    'ოთახების რ-ბა':title_of_amount_room,
    'value':amount_of_room,
    'საძინებელი':title_of_bedroom,
    'value':bedroom,
    'სველი წერტილი':title_of_bathroom, 
    'value':bathroom,
    'სამზარეულოს ტიპი':title_of_kitchen_type,
    'value':kitchen_type,
    'სართულების რაოდენობა':title_of_amount_floors,
    'value':amount_of_floors,
    'მდგომარეობა':title_of_condition,
    'value':condition, 
    'აივანი/ტერასა':title_of_balcony_terrace,
    'value':balcony_terrace,
    'ლოჯია':title_of_lojia,
    'value':lojia,
    'სამშენებლო მასალა':title_of_building_material,
    'value':building_material, 
    'შშმპ ადაპტირებული':title_of_shmp_adapted,
    'value':shmp_adapted,
    'ბუხარი':title_of_fireplace,
    'value':fireplace,
    'საუნა':title_of_sauna,
    'value':sauna,
    'აუზი':title_of_pool, 
    'value':pool, 
    'გათბობა':title_of_heating,
    'value':heating,
    'ცხ. წყალი':title_of_hot_water,
    'value':hot_water ,
    'სათავსო':title_of_store_room,
    'col-xs-12 col-sm-4 active':wardrobe,
    'col-xs-12 col-sm-4 active':outdoor_storage, 
    'col-xs-12 col-sm-4 active':shared_storage,
    'col-xs-12 col-sm-4 active':storage_on_balcony
}

with open('property_info.json', 'w') as file:
    json.dump(property_info, file, indent=57)





   