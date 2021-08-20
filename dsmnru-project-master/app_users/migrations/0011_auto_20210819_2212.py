# Generated by Django 3.2.6 on 2021-08-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0010_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=500)),
                ('message', models.TextField()),
                ('postDate', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name_plural': 'Logo'},
        ),
        migrations.AlterModelOptions(
            name='query',
            options={'verbose_name_plural': 'Query'},
        ),
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name_plural': 'User Profile Info'},
        ),
    ]