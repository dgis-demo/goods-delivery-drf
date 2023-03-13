import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PushTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('template', models.TextField(
                    help_text='Please, use the following template as example: '
                              '<b>Order {order_id} for {order_sum}{order_currency} is {order_status}.<b/>',
                    validators=[django.core.validators.RegexValidator(
                        message='Template must contain at least one of the following parameters in curly brackets: '
                                'order_id, order_sum, order_currency, order_status.',
                        regex='{order_id}|{order_sum}|{order_currency}|{order_status}')], verbose_name='template')),
                ('template_pl', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'push notification template',
                'verbose_name_plural': 'push notification templates',
                'db_table': 'push_template',
            },
        ),
        migrations.CreateModel(
            name='DeviceToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('token', models.CharField(max_length=255, verbose_name='token')),
                ('device', models.JSONField(blank=True, null=True, verbose_name='device')),
                ('device_id', models.CharField(max_length=50, verbose_name='device ID')),
                ('device_type', models.CharField(choices=[('IOS', 'IOS'), ('ANDROID', 'Android')], max_length=10,
                                                 verbose_name='device type')),
                ('is_enabled', models.BooleanField(default=False, verbose_name='is enabled')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_tokens',
                                           to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'device token',
                'verbose_name_plural': 'device tokens',
                'db_table': 'device_token',
            },
        ),
    ]
