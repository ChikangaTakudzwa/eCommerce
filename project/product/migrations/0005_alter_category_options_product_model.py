# Generated by Django 4.1.4 on 2022-12-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='X XR', max_length=4, unique=True),
        ),
    ]
