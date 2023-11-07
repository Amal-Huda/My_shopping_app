# Generated by Django 4.2.6 on 2023-10-26 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('cdescription', models.TextField(blank=True)),
                ('cimage', models.ImageField(blank=True, upload_to='category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('cname',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('pdescription', models.TextField(blank=True)),
                ('pimage', models.ImageField(blank=True, upload_to='product')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('availabile', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('pname',),
            },
        ),
    ]
