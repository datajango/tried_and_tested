# test_admin.py

import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from birdie import admin
from birdie import models

class TestPostAdmin:

    def test_excerpt(self):

        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, site)

        obj = mixer.blend('birdie.Post', body='Hello World')
        results = post_admin.excerpt(obj)
        assert results == 'Hello', 'Should return first first few characters.'