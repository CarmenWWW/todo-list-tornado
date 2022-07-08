import tornado.web
from handler import item as item_handlers

HANDLERS = [
    (r"/api/users", item_handlers.ItemListHandler),
     (r"/api/users/", item_handlers.ItemListHandler),
    (r"/api/users/(.+)", item_handlers.ItemHandler)
]

def run():
    app = tornado.web.Application(
        HANDLERS,
        debug = True,
    )
    http_server =tornado.httpserver.HTTPServer(app)
    port = 8000
    http_server.listen(port)
    print('server start on port: {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()