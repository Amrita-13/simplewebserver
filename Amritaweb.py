from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        Device Specification(Amrita B.S)
    </head>
    <body>
     <table border="5" cellpadding="10" cellspacing="10">
        <tr>
        <th> S.No </th>
        <th>Device Specification</th>
        <th>Type</th>
        </tr>
        <tr>
          <td>1</td>  
          <td>Device Name</td>
          <td>TMP215-75-G2</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Processor</td>
            <td>Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Installed RAM</td>
            <td>16.0 GB (15.5 GB usable)</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Device ID</td>
            <td>81E0E665-78B3-427B-9E84-B7DE0E9AAE6F</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Product Id</td>
            <td>00342-42784-66177-AAOEM</td>
        </tr>

        
     </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()