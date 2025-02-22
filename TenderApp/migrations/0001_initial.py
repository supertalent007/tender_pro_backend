# Generated by Django 5.0.4 on 2024-04-21 12:47

import TenderApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=TenderApp.models.image_advisor_path)),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='DesignPrivacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='ExeTeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=3000)),
                ('social', models.CharField(default='', max_length=3000)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=TenderApp.models.image_name_and_path)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam accumsan felis nec', max_length=255)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to=TenderApp.models.image_custom_path)),
                ('analysis_title', models.CharField(default='Use our data, science and AI to..', max_length=255)),
                ('households', models.CharField(default='30.8m', max_length=255)),
                ('data_sources', models.CharField(default='60+', max_length=255)),
                ('attr_per_record', models.CharField(default='2300+', max_length=255)),
                ('market_listing_coverage', models.CharField(default='81%', max_length=255)),
                ('data_points', models.CharField(default='75b', max_length=255)),
                ('address_match_accuracy', models.CharField(default='90%', max_length=255)),
                ('compliant', models.CharField(default='GDPR', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HomeProcessContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HomeProcessHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to=TenderApp.models.image_custom_path)),
                ('sub_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=TenderApp.models.image_news_path)),
            ],
        ),
        migrations.CreateModel(
            name='OurValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=3000)),
                ('image', models.FileField(blank=True, null=True, upload_to=TenderApp.models.image_svg_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=3000)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to=TenderApp.models.image_custom_path)),
                ('product_section_title', models.CharField(default='', max_length=255)),
                ('product_section_content', models.CharField(default='', max_length=3000)),
                ('product_description_title', models.CharField(default='', max_length=3000)),
                ('product_description_content', models.CharField(default='', max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('social', models.CharField(max_length=255)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=TenderApp.models.image_team_path)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=3000)),
                ('company', models.ImageField(blank=True, default='', null=True, upload_to=TenderApp.models.image_name_and_path)),
            ],
        ),
    ]
