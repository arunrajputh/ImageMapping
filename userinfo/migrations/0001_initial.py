# Generated by Django 4.1.5 on 2023-02-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/')),
                ('age', models.PositiveIntegerField()),
                ('mail', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
    ]