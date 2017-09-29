# -*- coding: utf-8 -*-

import argparse
import sys

import bittrex

API_KEY = None
API_KEY_SECRET = None



def command_parser():
    parser = argparse.ArgumentParser(description="Find out how much BTC we'll get.")
    parser.add_argument('currency', help='The currency we want to sell')
    parser.add_argument('amount', type=int, help='The amount we want to sell')

    return parser

def get_orderbook(currency):
    my_bittrex = bittrex.Bittrex(API_KEY, API_KEY_SECRET)
    market = "BTC-{}".format(currency)

    try:
        result = my_bittrex.get_orderbook(market, bittrex.BUY_ORDERBOOK)
    except:
        print "Error connecting to bittrex, please try again after a few seconds"
        sys.exit(1)

    if result['success']:
        return result['result']
    else:
        print "Something is wrong. Error message from bittrex: {}".format(result['message'])
        sys.exit(1)

def do_calculate(offers, amount):
    amount_left = amount
    total_get = 0

    for offer in offers:
        if amount_left >= offer['Quantity']:
            total_get += offer['Quantity'] * offer['Rate']
            amount_left -= offer['Quantity']
        else:
            total_get += amount_left * offer['Rate']
            amount_left = 0

    return total_get, amount_left

if __name__ == "__main__":
    parser = command_parser()
    args = parser.parse_args()

    offers = get_orderbook(args.currency)
    total_get, amount_left = do_calculate(offers, args.amount)

    if amount_left:
        print "We'll get {} BTC, and still have {} {} left".format(total_get, amount_left, args.currency)
    else:
        print "We'll get {} BTC".format(total_get)
