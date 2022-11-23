# Generated by Django 4.1.3 on 2022-11-22 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_alter_users_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='data',
        ),
        migrations.AddField(
            model_name='documents',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='documents',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
