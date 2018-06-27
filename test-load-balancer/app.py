import time
import logging

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class LoadHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/plain; charset=UTF-8")

        loadtime = int(self.get_query_argument('time', 10))

        logging.warn(f"Starting load maximizer for {loadtime}s")
        self.write(f"Max load for {loadtime}s\r\n")

        start = time.time()
        while time.time() - start < loadtime:
            5 + 5

        logging.info("Done with load")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/load", LoadHandler),
    ])

if __name__ == "__main__":
    logging.basicConfig(level=10)
    logging.info("Starting app")

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
