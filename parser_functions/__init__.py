import requests
from lxml import html as parser
from mongo import offers
import itertools


def construct_offer(node):
    offer = dict()
    try:
        offer['title'] = node.cssselect('a[data-cy="listing-ad-title"]>strong')[0].text_content().strip()
        offer['link'] = node.cssselect('a[data-cy="listing-ad-title"]')[0].get('href')
        offer['location'] = node.cssselect('i[data-icon="location-filled"]')[0].getparent().text_content().strip()
        offer['date'] = node.cssselect('i[data-icon="clock"]')[0].getparent().text_content().strip()
    except Exception as e:
        print(e)
        offer['title'] = "Для этой квартиры что-то упало, чекай логи."
    return offer


def parse_offers():
    data = {'search[city_id]': (None, 141), 'search[region_id]': (None, 4), 'search[category_id]': (None, 1147),
            'search[filter_float_number_of_rooms:from]': (None, 1), 'search[filter_float_number_of_rooms:to]': (None, 1)}
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    response = requests.post('https://www.olx.ua/ajax/donetsk/search/list/', files=data, headers={"User-Agent": user_agent})
    offer_nodes = parser.fromstring(response.content.decode('utf-8')).cssselect('table#offers_table>tbody>tr.wrap')
    return [construct_offer(node) for node in offer_nodes]


def find_new_offers():
    parsed_offers = parse_offers()
    old_offers = offers.find_all()
    new_offers = list(itertools.filterfalse(lambda x: x in old_offers, parsed_offers))
    if new_offers:
        offers.insert_many(new_offers)
    return new_offers
