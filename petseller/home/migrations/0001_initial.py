# Generated by Django 3.2.16 on 2022-12-29 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('animal_views', models.IntegerField(default=0)),
                ('animal_likes', models.IntegerField(default=1)),
                ('animal_name', models.CharField(max_length=100)),
                ('animal_description', models.TextField()),
                ('animal_slug', models.SlugField(max_length=1000, unique=True)),
                ('animal_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
            ],
            options={
                'ordering': ['animal_name'],
            },
        ),
        migrations.CreateModel(
            name='AnimalBreed',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('animal_breed', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalColor',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('animal_color', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalLocation',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='home.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalImages',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('animal_images', models.ImageField(upload_to='animals')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_breed',
            field=models.ManyToManyField(null=True, to='home.AnimalBreed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.category'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_color',
            field=models.ManyToManyField(null=True, to='home.AnimalColor'),
        ),
        migrations.AddField(
            model_name='animal',
            name='animal_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to=settings.AUTH_USER_MODEL),
        ),
    ]