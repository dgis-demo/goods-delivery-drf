from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetoken',
            name='is_enabled',
            field=models.BooleanField(default=True, verbose_name='is enabled'),
        ),
    ]
