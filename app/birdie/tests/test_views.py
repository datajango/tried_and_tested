# test_views.py

from django.test import RequestFactory

from birdie import views

class TestHomeView:

    def test_anobymous(self):
        req = RequestFactory().get('/')
        resp = views.HomeView.as_view()(req)
        assert resp.status_code == 200, 'Should be callable by anyone'