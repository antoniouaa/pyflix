def test_landing(app):
    response = app.get("/")

    assert response.status_code == 302
