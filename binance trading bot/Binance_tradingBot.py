import websocket
import json
import pprint
import talib
import numpy


SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_30m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUANTITY = 0.05

closes = []
in_position = False


def on_open(ws):
    print('opened connection')


def on_close(ws):
    print('closed connection')


def on_message(ws, message):
    global closes
    print('received message')
    print(message)
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

    if len(closes) > RSI_PERIOD:
        np_closes = numpy.array(closes)
        rsi = talib.RSI(np_closes, RSI_PERIOD)
        print("all rsis calculated so far")
        print(rsi)
        last_rsi = rsi(-1)
        print("the current rsi is {}".format(last_rsi))

    if last_rsi > RSI_OVERBOUGHT:
        print("sell! sell! sell!")
        # put binance sell logic here
    else:
        print("It is overbought but we don't own any nothing to do")

    if last_rsi < RSI_OVERSOLD:
        if in_position:
            print("It is oversold but you already own it nothing to do")
        else:
            print("buy! buy! buy!")
            # binance buy order logic here


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)


ws.run_forever()
