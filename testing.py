from flask import Flask, Response
from requests import get

IP = "54.175.87.239" # The actual IP of the server
HOST = "httpbin.org" # The actual dn of the server
HTTPS = False # True to use HTTPs

app = Flask(__name__, static_folder=None)

@app.route("/", defaults={"req_path": ''})
@app.route("/<path:req_path>")
def dir_listing(req_path=''):
    BASE_URL = f"http{'s' if HTTPS else ''}://{IP}/"
    URL = BASE_URL + req_path
    r = get(URL, headers={"Host": HOST})
    r.apparent_encoding

    resp = app.make_response(r.content)
    resp.headers.remove("Strict-Transport-Security")
    resp.headers.set("Content-Type", r.headers.get("Content-Type"))
    for k, v in r.cookies.items():
        print(f"Cookie {k} : {v}")
        resp.set_cookie(key=k, value=v)
    resp.status_code = r.status_code

    return resp

app.run(host="0.0.0.0", port=80, debug=False)
