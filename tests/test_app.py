def test_login_required(testapp):
    response = testapp.get("/", status=200)
    assert b"Sambal Login" in response.body


def test_notfound(testapp):
    response = testapp.get("/does-not-exist/", status=404)
    assert response.status_code == 404
