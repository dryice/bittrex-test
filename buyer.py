# -*- coding: utf-8 -*-

import argparse

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
    offers = my_bittrex.get_orderbook(market, bittrex.BUY_ORDERBOOK)['result']

    return offers
    


if __name__ == "__main__":
    parser = command_parser()
    args = parser.parse_args()

    offers = get_orderbook(args.currency)
    print offers[:20]
