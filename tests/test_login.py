from html.parser import HTMLParser


class LoginHTMLParser(HTMLParser):
    """Simple HTML parser to extract csrf token using the standard library."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.csrf_token = None
        self.return_url = None

    def handle_starttag(self, tag, attrs):
        if tag == "input":
            tag_attrs = dict(attrs)

            if tag_attrs["name"] == "csrf_token":
                self.csrf_token = tag_attrs["value"]

            if tag_attrs["name"] == "return_url":
                self.return_url = tag_attrs["value"]


def test_login(testapp, settings):
    response = testapp.get("/login/", status=200)
    parser = LoginHTMLParser()
    parser.feed(response.text)

    login_form = {
        "host": settings["samba.host"],
        "username": settings["samba.username"],
        "password": settings["samba.password"],
        "realm": settings["samba.realm"],
        "csrf_token": parser.csrf_token,
        "return_url": parser.return_url,
    }

    response = testapp.post("/login/", login_form, status=302)
    assert response.headers["location"] == parser.return_url

    response = testapp.get("/", status=200)
    assert "Sambal Login" not in response.text


def test_login_required(testapp):
    response = testapp.get("/", status=200)
    assert "Sambal Login" in response.text
