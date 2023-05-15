# Generated by Django 4.2.1 on 2023-05-15 18:30

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('posts', '0003_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField()),
                ('content', models.TextField(max_length=15000)),
                ('image', models.ImageField(upload_to='posts')),
            ],
        ),
        migrations.RenameModel(
            old_name='author',
            new_name='authors',
        ),
        migrations.DeleteModel(
            name='post',
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_authors', to='posts.authors'),
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
