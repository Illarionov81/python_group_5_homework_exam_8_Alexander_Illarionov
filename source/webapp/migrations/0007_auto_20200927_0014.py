# Generated by Django 2.2 on 2020-09-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20200926_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Товар'),
        ),
    ]
