# Generated by Django 3.2.12 on 2022-02-27 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_course_score_teacherinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qid', models.CharField(max_length=12)),
                ('Qquestion', models.CharField(max_length=255)),
                ('Qanswer', models.CharField(max_length=255)),
                ('Qoptions', models.CharField(max_length=255)),
                ('Qanalysis', models.CharField(max_length=255)),
                ('Qscore', models.IntegerField(max_length=3)),
                ('Qdifficulty', models.CharField(max_length=2)),
                ('QTreeName', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='Cno',
            new_name='Cid',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='Cno',
            new_name='Cid',
        ),
        migrations.RenameField(
            model_name='score',
            old_name='Sno',
            new_name='Sid',
        ),
        migrations.RenameField(
            model_name='studentinfo',
            old_name='Sno',
            new_name='Sid',
        ),
        migrations.RenameField(
            model_name='teacherinfo',
            old_name='Tno',
            new_name='Tid',
        ),
    ]
