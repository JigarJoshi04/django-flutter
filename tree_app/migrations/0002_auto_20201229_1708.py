# Generated by Django 3.0.5 on 2020-12-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treemodel',
            name='tree_name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
