import SimpleHTTPServer, SocketServer
from urlparse import urlparse, parse_qs
import subprocess

class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/tasks"):
            query_components = parse_qs(urlparse(self.path).query)
            cmd = ["task", "export"]
            if "filter" in query_components:
                filter_param = query_components.get("filter")[0]
                cmd.append(filter_param)
            output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
            self.wfile.write(output)             
        else:
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

handler = Handler
server = SocketServer.TCPServer(("", 9001), handler)
server.serve_forever()

