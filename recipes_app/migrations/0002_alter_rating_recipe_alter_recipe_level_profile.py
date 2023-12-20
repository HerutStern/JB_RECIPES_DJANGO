# Generated by Django 5.0 on 2023-12-19 16:44

import django.db.models.deletion
import recipes_app.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='recipe',
            field=models.ForeignKey(db_column='recipe', on_delete=django.db.models.deletion.RESTRICT, related_name='rating', to='recipes_app.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='level',
            field=models.CharField(blank=True, db_column='level', max_length=10, null=True, validators=[recipes_app.validators.validate_level]),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(blank=True, db_column='profession', max_length=50, null=True)),
                ('address', models.CharField(blank=True, db_column='address', max_length=256, null=True)),
                ('user', models.OneToOneField(db_column='user', on_delete=django.db.models.deletion.RESTRICT, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]