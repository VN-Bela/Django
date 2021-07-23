# Generated by Django 3.2.4 on 2021-07-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20210723_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='Account.Tag'),
        ),
    ]
