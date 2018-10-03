# Generated by Django 2.1.2 on 2018-10-03 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cummun_name', models.CharField(max_length=50)),
                ('sc_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classe_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('famille_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ordre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordre_name', models.CharField(max_length=30)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Classe')),
            ],
        ),
        migrations.AddField(
            model_name='famille',
            name='ordre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Ordre'),
        ),
        migrations.AddField(
            model_name='animal',
            name='famille',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifap.Famille'),
        ),
    ]