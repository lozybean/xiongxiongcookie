#!/usr/bin/env python
# -*- coding: utf-8 -*- \#
"""
@author = 'liangzb'
@date = '2017/3/28 0028'

"""
from app import app
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

app.secret_key = 'AAAAB3NzaC1yc2EAAAABIwAAAQEAvvLEse9VX9huurvaVaILlZCkItumksM1e6njLsQC4ZN80cZ/Ddl/O0z' \
                 '/sOnO3nMRVY16dkUflq6k3A/2ygz57yNHUDwElg2l+zGtR2QorjtC' \
                 '/8EvIveXcKa0OvgmLRbGLbFz70In1jjiOGPhvnt38IqVPzL6x32m3M7VxeQW2wOc4FNTPyp6yKhgHPTqrxWaupTovScCJPRrY' \
                 '/B6I/bgPP6KMvRYDcbWgHNBLR84dD0DuLMphbZMOXVUD/lmYXTImWD8muMmgSPypOcvq4wtj61DJ9Xh8aQ6E2JDE4qKlQ' \
                 '/EacqqgBcV8EKLoxlV6+FEC3Nkj5tJzFE4mXqI2tkaHw'
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000, address='0.0.0.0')
IOLoop.instance().start()
# app.run(debug=True, host='0.0.0.0', port=5000)
