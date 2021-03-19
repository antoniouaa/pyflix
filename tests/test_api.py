def test_index(app):
    resp = app.get("/api")

    assert resp.status_code == 200
    assert b"title" in resp.data


def test_post_request(app):
    resp = app.post("/api/pages/netflix/click", data={})

    assert resp.status_code == 302


def test_form_netflix(app, keys):
    url = "/api/pages/netflix/click"
    for key in keys:
        resp = app.post(url, data={key: ""})

        assert resp.status_code == 302


def test_form_prime(app, keys):
    url = "/api/pages/prime/click"
    for key in keys:
        resp = app.post(url, data={key: ""})

        assert resp.status_code == 302


def test_form_youtube(app, keys):
    url = "/api/pages/youtube/click"
    for key in keys:
        resp = app.post(url, data={key: ""})

        assert resp.status_code == 302


def test_index_redirect(app):
    resp = app.post("/api/pages/")

    assert resp is not None
    assert b"pyflix" in resp.data


def test_pages_redirect(app, pages):
    for page in pages:
        url = f"/api/pages/{page}"
        resp = app.get(url)

        assert resp is not None
        assert resp.status_code == 200
        assert bytes(page, encoding="utf-8") in resp.data
