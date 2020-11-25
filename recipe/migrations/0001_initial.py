# Generated by Django 2.2.15 on 2020-11-25 22:17

from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import recipe.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('featured_image', models.ImageField(default=recipe.models.default_featured_image, max_length=255, upload_to=recipe.models.default_featured_image_filepath)),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('source_url', models.URLField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(max_length=500)),
                ('cooking_intructions', models.TextField(blank=True, null=True)),
                ('ingredients', django.contrib.postgres.fields.jsonb.JSONField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
