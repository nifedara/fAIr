import factory

from login.models import OsmUser
from core.models import Dataset, AOI

from django.contrib.gis.geos import GEOSGeometry


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

    geom = GEOSGeometry("POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))", srid=4326)
    dataset = factory.SubFactory(DatasetFactory)
    label_status = -1
