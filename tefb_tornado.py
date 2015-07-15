import os
import sys
import tornado.ioloop
import tornado.web
import tornado.httpserver

class BaseHandler(tornado.web.RequestHandler):
    def compute_etag(self):
        return None

class JsonHandler(BaseHandler):
    def get(self):
        obj = { 'message': 'Hello, World!' }
        self.write(obj)

class PlaintextHandler(BaseHandler):
    def get(self):
        self.set_header('Content-Type', 'text/plain')
        self.write(b'Hello, World!')

app = tornado.web.Application((
    ('/json', JsonHandler),
    ('/plaintext', PlaintextHandler),
))

def main():
    server = tornado.httpserver.HTTPServer(app)
    if os.name == 'nt' or ('dofork' not in sys.argv):
        server.listen(8085)
    else:
        server.bind(8085)
        server.start(0)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
