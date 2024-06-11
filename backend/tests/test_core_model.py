from django.test import TestCase

from .factories import DatasetFactory, OsmUserFactory, AoiFactory, LabelFactory


class TestCoreModels(TestCase):

    def setUp(self):
        self.user = OsmUserFactory(username="Test User 2", osm_id=123)
        self.dataset = DatasetFactory(created_by=self.user)
        self.aoi = AoiFactory(dataset=self.dataset)
        self.label = LabelFactory(aoi=self.aoi)

    def test_dataset_creation(self):
        self.assertEqual(self.dataset.name, "Test Dataset")
        self.assertEqual(self.dataset.created_by, self.user)

    def test_aoi_creation(self):
        self.assertEqual(self.aoi.dataset, self.dataset)
        self.assertEqual(self.aoi.label_status, -1)

    def test_label_creation(self):
        self.assertEqual(self.label.aoi, self.aoi)
