# Generated by Django 4.0.5 on 2022-06-25 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='Password',
            new_name='password',
        ),
    ]