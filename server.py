#!/usr/bin/env python
import random
import socket
import time
import urlparse

<<<<<<< HEAD
from wsgiref.simple_server import make_server

from app import make_app

def main():
    the_wsgi_app = make_app()

    host = socket.getfqdn() # Get local machine name
    port = random.randint(8000, 9999)
    httpd = make_server('', port, the_wsgi_app)
    print "Serving at http://%s:%d/..." % (host, port,)
    httpd.serve_forever()

if __name__ == "__main__":
    main()
=======
def main():
    s = socket.socket()         # Create a socket object
    host = socket.getfqdn() # Get local machine name
    port = random.randint(8000, 9999)
    s.bind((host, port))        # Bind to the port
	
    print 'Starting server on', host, port
    print 'The Web server URL for this would be http://%s:%d/' % (host, port)
    s.listen(5)                 # Now wait for client connection.
	
    print 'Entering infinite loop; hit CTRL-C to exit'
    while True:
        # Establish connection with client.    
        c, (client_host, client_port) = s.accept()
	handle_connection(c)

        print 'Got connection from', client_host, client_port

def handle_connection(c):
    req = c.recv(1000)
    lineSplit = req.split('\r\n')
    req = lineSplit[0].split(' ')
    reqType = req[0]
    path = req[1]
    if reqType == 'GET':
        url = urlparse.urlparse(path)
        handle_get(c,url)
    elif reqType == 'POST':
        content = lineSplit[-1]
        handle_post(c,content)
    c.close()

def handle_submit(c,path):
    query = urlparse.parse_qs(path.query)
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send("Hello Mr. ")
    c.send(query['firstname'][0])
    c.send(" ")
    c.send(query['lastname'][0])
    c.send('.')
    c.send('</html></body>')

def handle_form(c,path):
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send("<form action='/submit' method='POST'>")
    c.send("First name:")
    c.send("<input type='text' name='firstname'>")
    c.send("Last name:")
    c.send("<input type='text' name='lastname'>")
    c.send("<input type='submit'>")
    c.send("</form>")
    c.send('</html></body>')

def handle_root(c,path):
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send('<h1>Hello, world.</h1>')
    c.send("This is rucins11's Web server.<br>")
    c.send("<a href='/content'>Content</a><br>")
    c.send("<a href='/file'>Files</a><br>")
    c.send("<a href='/image'>Images</a>")
    c.send('</html></body>')

def handle_content(c,path):
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send('<h1>Content Page</h1>')
    c.send('Stuff about things')
    c.send('</html></body>')

def handle_file(c,path):
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send('<h1>File Page</h1>')
    c.send('Files')
    c.send('</html></body>')

def handle_image(c,path):
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send('<h1>Image Page</h1>')
    c.send('Images')
    c.send('</html></body>')

def handle_404(c,path):
    c.send('HTTP/1.0 404 Not Found\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send('<h1>404</h1>')
    c.send('This page does not exist')
    c.send('</html></body>')

def handle_get(c,url):
    path = url.path
    # send a response
    #if main directory
    if path == '/':
        handle_root(c,url)
    #if form
    elif path == '/form':
        handle_form(c,url)
    #if submit
    elif path == '/submit':
        handle_submit(c,url)
    #if content directory
    elif path == '/content':
        handle_content(c,url)
    #if file directory
    elif path == '/file':
        handle_file(c,url)
    #if image directory
    elif path == '/image':
        handle_image(c,url)
    else:
        handle_404(c,url)

def handle_post(c,content):
    query = urlparse.parse_qs(content)
    c.send('HTTP/1.0 200 OK\r\n')
    c.send('Content-type: text/html\r\n\r\n')
    c.send('<html><body>')
    c.send("Hello Mr. ")
    c.send(query['firstname'][0])
    c.send(" ")
    c.send(query['lastname'][0])
    c.send('.')
    c.send('</html></body>')

if __name__== '__main__':
	main()
>>>>>>> master
