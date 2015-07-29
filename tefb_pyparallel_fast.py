import async
class Plaintext:
    http11 = True
    def plaintext(self, transport, data):
        return b'Hello, World!'

server = async.server('0.0.0.0', 8080)
async.register(transport=server, protocol=Plaintext)
async.run()