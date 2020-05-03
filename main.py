from send_mail import sendmail
import check_stock
import requests
import json


def search(keyword):

    url = 'https://www.supremenewyork.com/mobile_stock.json'

    requests_result = requests.get(url)
    all_categories = json.loads(requests_result.content)

    for category in all_categories['products_and_categories']:

        #skip the category "new"
        if category == "new":
            continue

        for element in all_categories['products_and_categories'][category]:
            name_split = element["name"].lower().split()
            #print(name_split)
            if keyword in name_split:
                print("Product Found!")
                #print(element)
                product_name = element["name"]
                product_id = element["id"]
                product_price = element["price"]/100
                prodcut_category_name = element["category_name"]

                print(product_name)
                #print(product_id)

                url2 = f"https://www.supremenewyork.com/shop/{product_id}.json"

                product_detail = requests.get(url2)
                product_page = json.loads(product_detail.content)
                #print(product_page)

                for product in product_page['styles']:
                    if product['name'] == 'Purple':
                        for item in product['sizes']:
                            if item['name'] == 'Small' and item['stock_level'] == 1:
                                print(item['name'])
                                print(item['stock_level'])
                                return True

    return False


keyword = input("Input the keyword, seperate with ',' ::").lower()
#keyword = "Quilted"

keylist = keyword.split(",")

for keyword in keylist:
    if(search(keyword)):
        sendmail()




