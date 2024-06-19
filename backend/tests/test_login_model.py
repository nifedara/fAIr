from django.test import TestCase

from .factories import OsmUserFactory


class TestLoginModels(TestCase):

    def test_OsmUser_creation(self):
        osm_user = OsmUserFactory()

        self.assertEqual(str(osm_user), "Test User")
        self.assertEqual(osm_user.osm_id, 123456)
