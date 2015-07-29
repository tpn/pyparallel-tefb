var http = require('http'),
    url = require('url'),
    cluster = require('cluster'),
    numCPUs = require('os').cpus().length;

if (cluster.isMaster) {
  for (var i = 0; i < numCPUs; i++) {
      cluster.fork();
  }
} else {
  http.createServer(function(req, res) {
      var path = url.parse(req.url).pathname;

      switch (path) {
          case '/json':
              res.writeHead(200, { 'Content-Type': 'application/json; charset=UTF-8' });
              res.end(JSON.stringify({ message: 'Hello, World!' }));
              break;
          case '/plaintext':
              res.writeHead(200, { 'Content-Type': 'text/plain; charset=UTF-8' });
              res.end('Hello, World!');
              break;
          default:
              res.writeHead(501, { 'Content-Type': 'text/plain; charset=UTF-8' });
              res.end('NOT IMPLEMENTED');
              break;
      }
  }).listen(8085);
}