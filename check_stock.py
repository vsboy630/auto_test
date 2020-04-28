import requests


def available():
    url = "https://www.supremenewyork.com/shop/shoes/hosvthyi8/uieqsjb60?alt=0"
    html = requests.get(url).text
    print(html)
    w = 'data-sold-out="true"'
    if w in html:
        print("AirForce Restock：{}".format(str))
        return False
    else:
        print("你要找的字符串没有出现在该网站！")
        return True
