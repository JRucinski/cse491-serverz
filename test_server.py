from app import make_app
from webtest import TestApp
from StringIO import StringIO

test_app = TestApp(make_app())

class FakeConnection(object):
    """
    A fake connection class that mimics a real TCP socket for the purpose
    of testing socket I/O.
    """
    def __init__(self, to_recv):
        self.to_recv = to_recv
        self.sent = ""
        self.is_closed = False

    def recv(self, n):
        if n > len(self.to_recv):
            r = self.to_recv
            self.to_recv = ""
            return r

        r, self.to_recv = self.to_recv[:n], self.to_recv[n:]
        return r

    def send(self, s):
        self.sent += s

    def close(self):
        self.is_closed = True

# Test a basic GET call.

<<<<<<< HEAD
def test_root():
    resp = test_app.get('/')
    assert resp.status == '200 OK'

def test_content():
    resp = test_app.get('/content')
    assert resp.status == '200 OK'

def test_image():
    resp = test_app.get('/image')
    assert resp.status == '200 OK'

def test_file():
    resp = test_app.get('/file')
    assert resp.status == '200 OK'

def test_GET_submit():
    resp = test_app.get('/submit?firstname=Joe&lastname=Man')
    assert resp.status == '200 OK'
    assert 'Joe Man' in resp

def test_form():
    resp = test_app.get('/form')
    assert resp.status == '200 OK'
=======
def test_handle_connection():
    conn = FakeConnection("GET / HTTP/1.0\r\n\r\n")
    expected_return = 'HTTP/1.0 200 OK\r\n' + \
                      'Content-type: text/html\r\n' + \
                      '\r\n' + \
		      '<html><body>' + \
                      '<h1>Hello, world.</h1>' + \
                      "This is rucins11's Web server.<br>" + \
		      "<a href='/content'>Content</a><br>" + \
		      "<a href='/file'>Files</a><br>" + \
		      "<a href='/image'>Images</a>" + \
		      '</html></body>'

    server.handle_connection(conn)

    assert conn.sent == expected_return, 'Got: %s' % (repr(conn.sent),)

def test_handle_connection_content():
    conn = FakeConnection("GET /content HTTP/1.0\r\n\r\n")
    expected_return = 'HTTP/1.0 200 OK\r\n' + \
                      'Content-type: text/html\r\n' + \
                      '\r\n' + \
                      '<html><body>' + \
                      '<h1>Content Page</h1>' + \
                      'Stuff about things' + \
                      '</html></body>'

    server.handle_connection(conn)

    assert conn.sent == expected_return, 'Got: %s' % (repr(conn.sent),)

def test_handle_connection_file():
    conn = FakeConnection("GET /file HTTP/1.0\r\n\r\n")
    expected_return = 'HTTP/1.0 200 OK\r\n' + \
                      'Content-type: text/html\r\n' + \
                      '\r\n' + \
                       '<html><body>' + \
                      '<h1>File Page</h1>' + \
                      'Files' + \
                      '</html></body>' 

    server.handle_connection(conn)

    assert conn.sent == expected_return, 'Got: %s' % (repr(conn.sent),)

def test_handle_connection_image():
    conn = FakeConnection("GET /image HTTP/1.0\r\n\r\n")
    expected_return = 'HTTP/1.0 200 OK\r\n' + \
                      'Content-type: text/html\r\n' + \
                      '\r\n' + \
                      '<html><body>' + \
                      '<h1>Image Page</h1>' + \
                      'Images' + \
                      '</html></body>'

    server.handle_connection(conn)

    assert conn.sent == expected_return, 'Got: %s' % (repr(conn.sent),)

def test_handle_connection_submit_get():
    conn = FakeConnection("GET /submit?firstname=Joe&lastname=Man "\
        +"HTTP/1.0\r\n\r\n")
    expected_return = "HTTP/1.0 200 OK\r\n"\
        +"Content-type: text/html\r\n\r\n"\
        +"<html><body>"\
        +"Hello Mr. Joe Man."\
        +"</html></body>"

    server.handle_connection(conn)

    assert conn.sent == expected_return, 'Got: %s' % (repr(conn.sent),)

def test_handle_connection_submit_post():
    conn = FakeConnection("POST /submit "\
        +"HTTP/1.0\r\n\r\n"\
        +"firstname=Joe&lastname=Man")
    expected_return = "HTTP/1.0 200 OK\r\n"\
        +"Content-type: text/html\r\n\r\n"\
        +"<html><body>"\
        +"Hello Mr. Joe Man."\
        +"</html></body>"
>>>>>>> master

def test_POST_submit():
    resp = test_app.get('/form')
    form = resp.form
    form['firstname'] = 'Joe'
    form['lastname'] = 'Man'
    resp2 = form.submit('submit')
    assert resp2.status == '200 OK'
    assert 'Joe Man' in resp2

def test_404():
    resp = test_app.get('/thislinkisgood',status=404)
    assert resp.status_int == 404
