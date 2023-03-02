import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('full_name', models.CharField(max_length=128, unique=True, verbose_name='full name')),
                ('short_name', models.CharField(max_length=64, unique=True, verbose_name='short name')),
                ('alpha2', models.CharField(blank=True, max_length=2, null=True, verbose_name='alpha-2 code')),
                ('alpha3', models.CharField(blank=True, max_length=3, null=True, verbose_name='alpha-3 code')),
                ('code', models.CharField(blank=True, max_length=3, null=True, verbose_name='numeric code')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'country',
                'ordering': ('alpha3',),
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('currency', models.CharField(max_length=128, unique=True, verbose_name='full name')),
                ('code', models.CharField(max_length=3, verbose_name='alphabetic code')),
                ('numeric', models.CharField(blank=True, max_length=3, null=True, verbose_name='numeric code')),
                ('digit', models.CharField(blank=True, max_length=8, null=True, verbose_name='minor unit')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currencies',
                                              to='measurement.country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
                'db_table': 'currency',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities',
                                              to='measurement.country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
            },
        ),
    ]
