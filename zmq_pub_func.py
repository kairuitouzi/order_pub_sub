#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/29 0029 16:13
# @Author  : Hadrianl 
# @File    : zmq_pub_func.py
# @License : (C) Copyright 2013-2017, 凯瑞投资

import zmq
from datetime import datetime
from zmq.asyncio import Context

class pub():
    def __init__(self, port):
        self.context = Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f"tcp://*:{port}")

    async def send_changed_order(self, d: dict):
        await self.socket.send_pyobj(d)
        print(str(datetime.now()))

    def __enter__(self):
        print('开启订阅推送')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
        print('关闭订阅推送')
