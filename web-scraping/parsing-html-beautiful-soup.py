import bs4
import requests


# res = requests.get('https://nostarch.com/automatestuff2')
# res.raise_for_status()
#
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup.select( 'div.form-type-radio:nth-child(1) > label:nth-child(1)'))
# elems = soup.select('div.form-type-radio:nth-child(1) > label:nth-child(1)')
# print(elems[0].text.strip().split(', ')[1])


def get_book_price(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('div.form-type-radio:nth-child(1) > label:nth-child(1)')
    print('The price is ' + elems[0].text.strip().split(', ')[1])


get_book_price('https://nostarch.com/automatestuff2')
get_book_price('https://nostarch.com/beyond-basic-stuff-python')
