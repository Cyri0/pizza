# Generated by Django 4.2.5 on 2023-10-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/pizzas/'),
        ),
    ]
