# Generated by Django 4.0 on 2022-01-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_group_alter_person_name_membership_group_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(to='polls.Person'),
        ),
    ]
