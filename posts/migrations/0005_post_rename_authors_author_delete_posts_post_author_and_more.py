# Generated by Django 4.2.1 on 2023-05-16 10:37

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('posts', '0004_posts_rename_author_authors_delete_post_posts_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField()),
                ('content', models.TextField(max_length=15000)),
                ('image', models.ImageField(upload_to='posts')),
            ],
        ),
        migrations.RenameModel(
            old_name='authors',
            new_name='author',
        ),
        migrations.DeleteModel(
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='posts.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]