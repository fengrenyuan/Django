# Generated by Django 2.1.5 on 2019-01-28 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='abstract',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Abstract'),
            preserve_default=False,
        ),
    ]
