# Generated by Django 4.1.4 on 2022-12-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_ticket_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='number',
            field=models.CharField(default=0, max_length=8, primary_key=True, serialize=False),
        ),
    ]
