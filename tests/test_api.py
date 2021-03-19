def test_index(app):
    resp = app.get("/api")

    assert resp.status_code == 200
    assert b"title" in resp.data


def test_post_request(app):
    resp = app.post("/api/click", data={})

    assert resp.status_code == 302


def test_form_keys(app, keys):
    for key in keys:
        resp = app.post("/api/click", data={key: ""})

        assert resp.status_code == 302
        assert "Option-Clicked" in resp.headers
        assert resp.headers["Option-Clicked"] == key
