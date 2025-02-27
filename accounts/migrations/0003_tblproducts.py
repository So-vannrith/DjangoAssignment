# Generated by Django 5.1.2 on 2024-11-08 21:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200, null=True)),
                ('quantity', models.CharField(max_length=200, null=True)),
                ('priceIn', models.CharField(max_length=200, null=True)),
                ('priceOut', models.CharField(max_length=200, null=True)),
                ('instock', models.CharField(max_length=200, null=True)),
                ('productImage', models.CharField(max_length=200, null=True)),
                ('productDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('categoryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
            ],
        ),
    ]
