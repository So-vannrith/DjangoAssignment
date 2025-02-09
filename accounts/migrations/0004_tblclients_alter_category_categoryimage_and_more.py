# Generated by Django 5.1.2 on 2024-12-06 23:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_tblproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=200, null=True)),
                ('clientImage', models.ImageField(upload_to='pics')),
                ('clientDescription', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='CategoryImage',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tblproducts',
            name='productImage',
            field=models.ImageField(upload_to='ProductImages/'),
        ),
    ]
