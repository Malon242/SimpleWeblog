# Generated by Django 3.1 on 2020-08-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0004_auto_20200828_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
    ]
