def test_login_required(testapp):
    response = testapp.get("/", status=200)
    assert b"Sambal Login" in response.body
