# Programming Test
- Background
  - Bittrex.com is a site for trading crypto currency
  - https://github.com/ericsomdahl/python-bittrex is a python API that let's you get market data

- Task
  - Make a python script that uses the "python-bittrex" api
  - use the get_orderbook method from the file:
     - https://github.com/ericsomdahl/python-bittrex/blob/master/bittrex/bittrex.py
     - You get a list of orders - people buying and selling different amounts for different prices

- Inputs
  - currency name (like "ETH")
  - amount to sell (like 16)

- Outputs
  - The function returns how much bitcoin you would get for selling that amount, by looking at the current buy offers
  - buy offers look like this (click below to expand)
        "buy" : [
        {
                "Quantity" : 12.00000000,
                "Rate" : 0.02525000
            },
        {
                "Quantity" : 15.37000000,
                "Rate" : 0.02515000
            },
        {
                "Quantity" : 11.37000000,
                "Rate" : 0.02505000
            },
        ],
  - Selling 16 units into this orderbook would sell 12 at 0.02525000 and 4 at 0.02515000
  - result would be 0.4036
