def test_notfound(testapp):
    response = testapp.get("/does-not-exist/", status=404)
    assert response.status_code == 404
