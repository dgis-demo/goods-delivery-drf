import django.utils.timezone
from django.db import migrations, models

import apps.accounts.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              max_length=150, unique=True,
                                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                              verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=21, null=True, unique=True, validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: '+999999999'. Up to 21 digits allowed.",
                        regex='^\\+\\d{9,20}$')])),
                ('is_phone_verified', models.BooleanField(default=False, verbose_name='is phone verified')),
                ('role', models.CharField(
                    choices=[('customer', 'Customer'), ('courier', 'Courier'), ('store', 'Store worker'),
                             ('bo_country', 'Backoffice country employee'),
                             ('bo_company', 'Backoffice company employee'), ('admin', 'Administrator'),
                             ('support', 'Support')], max_length=20, null=True, verbose_name='user role')),
                ('country', models.CharField(blank=True, max_length=3, null=True, verbose_name='country')),
                ('groups', models.ManyToManyField(blank=True,
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_name='user_set', related_query_name='user', to='auth.Group',
                                                  verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                                                            related_name='user_set', related_query_name='user',
                                                            to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAdminProxy',
            fields=[
            ],
            options={
                'verbose_name': 'administrator',
                'verbose_name_plural': 'administrators',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserAdminProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserBOCompanyProxy',
            fields=[
            ],
            options={
                'verbose_name': 'backoffice company employee',
                'verbose_name_plural': 'backoffice company workers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserBaseProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserBOCountryProxy',
            fields=[
            ],
            options={
                'verbose_name': 'backoffice country employee',
                'verbose_name_plural': 'backoffice country workers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserBaseProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserCourierProxy',
            fields=[
            ],
            options={
                'verbose_name': 'courier',
                'verbose_name_plural': 'couriers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserBaseProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserCustomerProxy',
            fields=[
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserBaseProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserStoreProxy',
            fields=[
            ],
            options={
                'verbose_name': 'store worker',
                'verbose_name_plural': 'store workers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserBaseProxyManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserSupportProxy',
            fields=[
            ],
            options={
                'verbose_name': 'support',
                'verbose_name_plural': 'supports',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
            managers=[
                ('objects', apps.accounts.managers.UserBaseProxyManager()),
            ],
        ),
    ]
