# Generated by Django 4.2.2 on 2023-10-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='profiles.profile', verbose_name='Likes'),
        ),
        migrations.AlterField(
            model_name='post',
            name='score',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='評価'),
        ),
    ]
