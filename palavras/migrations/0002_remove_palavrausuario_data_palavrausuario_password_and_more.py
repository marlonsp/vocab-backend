# Generated by Django 4.1.3 on 2022-12-03 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palavras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palavrausuario',
            name='data',
        ),
        migrations.AddField(
            model_name='palavrausuario',
            name='password',
            field=models.CharField(default='123', max_length=100),
        ),
        migrations.AlterField(
            model_name='palavrausuario',
            name='palavra',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='palavrausuario',
            name='usuario',
            field=models.CharField(max_length=100),
        ),
    ]