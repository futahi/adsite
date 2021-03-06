# Generated by Django 3.2 on 2021-04-28 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aapp', '0002_remove_comment_islam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family_Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('body', models.TextField(verbose_name='Комментарии')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='aapp.family')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
