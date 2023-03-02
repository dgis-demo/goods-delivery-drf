import factory.fuzzy
from faker import Faker

from apps.measurement.models import Country


fake = Faker(['en-US'])


class CountryFactory(factory.django.DjangoModelFactory):
    """"""
    class Meta:
        model = Country

    full_name = factory.LazyAttribute(lambda x: fake.unique.word()[:128])
    short_name = factory.LazyAttribute(lambda x: fake.unique.word()[:64])
    alpha2 = factory.fuzzy.FuzzyText(length=2)
    alpha3 = factory.fuzzy.FuzzyText(length=3)
    code = factory.fuzzy.FuzzyText(length=3)
