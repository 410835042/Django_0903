# Generated by Django 3.2.9 on 2022-04-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('summary', models.TextField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=7)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]