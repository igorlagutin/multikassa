# Generated by Django 2.2.3 on 2019-07-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('sell', models.CharField(max_length=2048)),
                ('code', models.CharField(max_length=2048)),
            ],
            options={
                'verbose_name_plural': 'Курсы криптовалют',
                'verbose_name': 'Курс криптовалюты',
            },
        ),
        migrations.RenameField(
            model_name='rate',
            old_name='value',
            new_name='pursage',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='from_online',
        ),
        migrations.AddField(
            model_name='rate',
            name='sell',
            field=models.CharField(default='0', max_length=2048),
            preserve_default=False,
        ),
    ]
