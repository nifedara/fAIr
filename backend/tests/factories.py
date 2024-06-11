import factory

from login.models import OsmUser
from core.models import Dataset, AOI, Label


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
