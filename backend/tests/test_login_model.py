from django.test import TestCase
from login.models import OsmUser


class TestLoginModels(TestCase):

    def test_OsmUser_creation(self):
        osm_user = OsmUser.objects.create(username="Test User", osm_id=123456)

        self.assertEqual(str(osm_user), "Test User")
        self.assertEqual(osm_user.osm_id, 123456)
