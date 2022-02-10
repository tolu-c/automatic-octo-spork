# Generated by Django 4.0.2 on 2022-02-10 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endpoint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='eoi',
            name='skill',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='endpoint.skill'),
            preserve_default=False,
        ),
    ]
