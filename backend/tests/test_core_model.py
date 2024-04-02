from django.test import TestCase

from .factories import DatasetFactory, OsmUserFactory


class TestCoreModels(TestCase):

    def test_dataset_creation(self):
        user = OsmUserFactory(username="Test User 2", osm_id=123)
        dataset = DatasetFactory(created_by=user)

        self.assertEqual(dataset.name, "Test Dataset")
        self.assertEqual(dataset.created_by, user)
