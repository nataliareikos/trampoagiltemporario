# Generated by Django 2.1.7 on 2019-03-15 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_trampo_agil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vagas',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='Vagas',
        ),
    ]