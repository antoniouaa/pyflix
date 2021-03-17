def test_index(app):
    response = app.get("/api")

    assert response.status_code == 200
    assert b"title" in response.data


def test_form(app):
    response = app.post("/api/click")

    assert response.status_code == 302
