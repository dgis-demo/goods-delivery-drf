import factory
from faker import Faker

from apps.measurement.models import City

from .country import CountryFactory


fake = Faker(['en-US'])


class CityFactory(factory.django.DjangoModelFactory):
    """"""
    class Meta:
        model = City

    name = factory.LazyAttribute(lambda x: fake.unique.city())
    country = factory.SubFactory(CountryFactory)
