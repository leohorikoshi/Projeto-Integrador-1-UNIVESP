# Generated by Django 2.2.28 on 2024-05-17 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20191005_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='ncm',
        ),
    ]