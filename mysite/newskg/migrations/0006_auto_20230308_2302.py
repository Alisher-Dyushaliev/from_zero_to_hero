# Generated by Django 3.0.2 on 2023-03-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newskg', '0005_auto_20230214_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='newskg',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='get_langs', to='newskg.Tag'),
        ),
    ]
