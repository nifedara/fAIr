import factory

from login.models import OsmUser
from core.models import Dataset


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
