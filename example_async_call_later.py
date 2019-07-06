#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import datetime


"""
An example of a callback displaying the current date every second. The callback
uses the loop.call_later() method to reschedule itself after 5 seconds, and then
stops the event loop:

1. イベントループの取得 loop = asyncio.get_event_loop()
2. イベントループへのスケジューリング loop.call_soon(callback)
3. イベントループの実行 loop.run_forever()
4. イベントループの停止 loop.stop()
5. イベントループを閉じる loop.close()

ループがブロッキングI/Oを上手くこなしてくれる
"""

def display_date(end_time, loop):
    print(datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)
    else:
        loop.call_soon(loop.stop) # 単にloop.stop()でもいい


def display_date2(loop):
    print(datetime.datetime.now())
    try:
        loop.call_later(1, display_date, end_time, loop)
    except KeyboardInterrupt:
        loop.stop()


loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()


