# Generated by Django 3.0.2 on 2023-01-15 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newskg', '0002_auto_20230115_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
            ],
            options={
                'verbose_name': 'Purpose',
                'verbose_name_plural': 'Purposes',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='newskg',
            name='purpose',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='newskg.Purpose'),
        ),
    ]