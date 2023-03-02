import factory
from django.contrib.auth import get_user_model
from faker import Faker


fake = Faker(['en-US'])


class UserFactory(factory.django.DjangoModelFactory):
    """"""
    class Meta:
        model = get_user_model()

    username = factory.LazyAttribute(lambda x: fake.unique.word())
    is_superuser = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=50))
    password = factory.LazyAttribute(lambda x: fake.unique.word())
    email = factory.LazyAttribute(lambda x: fake.unique.company_email())
    phone = factory.LazyAttribute(lambda x: fake.unique.phone_number()[:21])
    role = factory.LazyAttribute(lambda x: fake.unique.word())
