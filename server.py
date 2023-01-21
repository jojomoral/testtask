import json
import wsgiref.simple_server
import urllib.parse
import os

import pages
import DB
from CONFIG import DATABASE_PATH

def application(environ, start_response):
    # requested path
    path = environ["PATH_INFO"]
    # requested method
    method = environ["REQUEST_METHOD"]

    # content type of response
    content_type = "text/html"

    if path == "/":
        pass
    elif path == "/users/":
        # reading html file
        index = pages.show_users()
        response = index.encode()
        status = "200 OK"
    elif path == "/users/add/":
        # reading html file
        index = pages.add_user()
        response = index.encode()
        status = "200 OK"


    else:
        # 404 - path not found
        response = b"<h1>Not found</h1><p>Entered path not found</p>"
        status = "404 Not Found"

    # response headers
    headers = [
        ("Content-Type", content_type),
        ("Content-Length", str(len(response)))
    ]

    start_response(status, headers)
    return [response]


if __name__ == "__main__":
    if not os.path.exists(DATABASE_PATH):
        with open(DATABASE_PATH, 'w'):
            DB.create_tables()
    w_s = wsgiref.simple_server.make_server(
        host="localhost",
        port=8080,
        app=application
    )
    w_s.serve_forever()