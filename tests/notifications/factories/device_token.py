import factory
from faker import Faker

from apps.notifications.models import DeviceToken
from tests.accounts.factories import UserFactory


fake = Faker(['en-US'])


class DeviceTokenFactory(factory.django.DjangoModelFactory):
    """"""
    class Meta:
        model = DeviceToken

    user = factory.SubFactory(UserFactory)
    token = factory.LazyAttribute(lambda x: fake.unique.word())
    device = factory.LazyAttribute(lambda x: {f"{fake.unique.word()}": fake.unique.word()})
    device_id = factory.LazyAttribute(lambda x: fake.unique.word())
    device_type = factory.LazyAttribute(lambda x: DeviceToken.DeviceType.IOS)
    is_enabled = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=50))
