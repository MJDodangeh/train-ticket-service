# Generated by Django 4.1.4 on 2022-12-22 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passenger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userpassenger', to=settings.AUTH_USER_MODEL),
        ),
    ]
