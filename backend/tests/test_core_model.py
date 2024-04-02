from django.test import TestCase

from .factories import (
    DatasetFactory,
    OsmUserFactory,
    AoiFactory,
    LabelFactory,
    ModelFactory,
    TrainingFactory,
    FeedbackFactory,
    FeedbackAoiFactory,
    FeedbackLabelFactory,
)


class TestCoreModels(TestCase):

    def setUp(self):
        self.user = OsmUserFactory(username="Test User 2", osm_id=123)
        self.dataset = DatasetFactory(created_by=self.user)
        self.aoi = AoiFactory(dataset=self.dataset)
        self.label = LabelFactory(aoi=self.aoi)
        self.model = ModelFactory(dataset=self.dataset, created_by=self.user)
        self.training = TrainingFactory(model=self.model, created_by=self.user)
        self.feedback = FeedbackFactory(training=self.training, user=self.user)
        self.feedbackAoi = FeedbackAoiFactory(training=self.training, user=self.user)
        self.feedbackLabel = FeedbackLabelFactory(feedback_aoi=self.feedbackAoi)

    def test_dataset_creation(self):
        self.assertEqual(self.dataset.name, "Test Dataset")
        self.assertEqual(self.dataset.created_by, self.user)

    def test_aoi_creation(self):
        self.assertEqual(self.aoi.dataset, self.dataset)
        self.assertEqual(self.aoi.label_status, -1)

    def test_label_creation(self):
        self.assertEqual(self.label.aoi, self.aoi)

    def test_model_creation(self):
        self.assertEqual(self.model.name, "Test Model")
        self.assertEqual(self.model.dataset, self.dataset)
        self.assertEqual(self.model.created_by, self.user)
        self.assertEqual(self.model.status, -1)

    def test_training_creation(self):
        self.assertEqual(self.training.model, self.model)
        self.assertEqual(self.training.status, "SUBMITTED")
        self.assertEqual(self.training.zoom_level, [20, 21])
        self.assertEqual(self.training.created_by, self.user)
        self.assertEqual(self.training.epochs, 3)
        self.assertEqual(self.training.batch_size, 24)

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.training, self.training)
        self.assertEqual(self.feedback.zoom_level, 19)
        self.assertEqual(self.feedback.feedback_type, "TP")
        self.assertEqual(self.feedback.user, self.user)
        self.assertEqual(self.feedback.source_imagery, "https://test_data/hotosm/fAIr/")

    def test_feedbackAoi_creation(self):
        self.assertEqual(self.feedbackAoi.training, self.training)
        self.assertEqual(self.feedbackAoi.label_status, -1)
        self.assertEqual(self.feedbackAoi.source_imagery, "https://test_data/hotosm/")
        self.assertEqual(self.feedbackAoi.user, self.user)

    def test_feedbackLabel_creation(self):
        self.assertEqual(self.feedbackLabel.feedback_aoi, self.feedbackAoi)
