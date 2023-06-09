# Generated by Django 4.2 on 2023-04-26 20:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('species', models.CharField(choices=[('DO', 'Dog'), ('CA', 'Cat'), ('CO', 'Cow'), ('PI', 'Pig'), ('HO', 'Horse'), ('GP', 'Guinea Pig'), ('HA', 'Hamster'), ('RA', 'Rabbit'), ('FE', 'Ferret')], max_length=2)),
                ('age', models.IntegerField(verbose_name=django.core.validators.MinValueValidator(0))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
