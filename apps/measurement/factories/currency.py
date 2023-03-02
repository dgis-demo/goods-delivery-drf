import factory.fuzzy
from faker import Faker

from apps.measurement.models import Currency

from .country import CountryFactory


fake = Faker(['en-US'])


class CurrencyFactory(factory.django.DjangoModelFactory):
    """"""
    class Meta:
        model = Currency

    currency = factory.LazyAttribute(lambda x: fake.unique.word()[:128])
    code = factory.LazyAttribute(lambda x: fake.unique.word()[:3])
    numeric = factory.fuzzy.FuzzyText(length=3)
    digit = factory.fuzzy.FuzzyText(length=8)
    country = factory.SubFactory(CountryFactory)
