import factory

from login.models import OsmUser
from core.models import (
    Dataset,
    AOI,
    Label,
    Model,
    Training,
    Feedback,
    FeedbackAOI,
    FeedbackLabel,
)


class OsmUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OsmUser

    username = "Test User"
    osm_id = 123456


class DatasetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Dataset

    name = "Test Dataset"
    created_by = factory.SubFactory(OsmUserFactory)
    status = -1


class AoiFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AOI

    geom = "POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))"
    dataset = factory.SubFactory(DatasetFactory)
    label_status = -1


class LabelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Label

    aoi = factory.SubFactory(AoiFactory)
    geom = "POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))"


class ModelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Model

    dataset = factory.SubFactory(DatasetFactory)
    name = "Test Model"
    created_by = factory.SubFactory(OsmUserFactory)
    status = -1


class TrainingFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Training

    model = factory.SubFactory(ModelFactory)
    status = "SUBMITTED"
    zoom_level = [20, 21]
    created_by = factory.SubFactory(OsmUserFactory)
    epochs = 3
    batch_size = 24


class FeedbackFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Feedback

    geom = "POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))"
    training = factory.SubFactory(TrainingFactory)
    zoom_level = 19
    feedback_type = "TP"
    user = factory.SubFactory(OsmUserFactory)
    source_imagery = "https://test_data/hotosm/fAIr/"


class FeedbackAoiFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FeedbackAOI

    training = factory.SubFactory(TrainingFactory)
    geom = "POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))"
    label_status = -1
    source_imagery = "https://test_data/hotosm/"
    user = factory.SubFactory(OsmUserFactory)


class FeedbackLabelFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = FeedbackLabel

    feedback_aoi = factory.SubFactory(FeedbackAoiFactory)
    geom = "POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))"
