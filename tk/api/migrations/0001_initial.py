# Generated by Django 2.1.7 on 2022-04-29 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cclassid', models.IntegerField()),
                ('Ccname', models.CharField(max_length=32)),
                ('Cid', models.IntegerField()),
                ('Tid', models.IntegerField()),
                ('Create_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cid', models.IntegerField()),
                ('Cname', models.CharField(max_length=32)),
                ('Cclassid', models.IntegerField()),
                ('Ccreate_time', models.DateTimeField(default=datetime.datetime.now)),
                ('Cend_time', models.DateTimeField(auto_now=True)),
                ('Tid', models.IntegerField()),
                ('Question_num', models.IntegerField(default=0)),
                ('State', models.IntegerField(default=0)),
                ('Img_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Eid', models.IntegerField()),
                ('Title', models.CharField(max_length=255)),
                ('Total_score', models.CharField(max_length=255)),
                ('Cid', models.CharField(max_length=12)),
                ('Create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('Start_time', models.DateTimeField()),
                ('End_time', models.DateTimeField()),
                ('State', models.IntegerField()),
                ('Students_Exam', models.CharField(max_length=255)),
                ('Questions_Exam', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qid', models.IntegerField()),
                ('Qquestion', models.CharField(max_length=255)),
                ('Qanswer', models.CharField(max_length=255)),
                ('Question_type', models.IntegerField()),
                ('Qoptions_a', models.CharField(max_length=255)),
                ('Qoptions_b', models.CharField(max_length=255)),
                ('Qoptions_c', models.CharField(max_length=255)),
                ('Qoptions_d', models.CharField(max_length=255)),
                ('Qoptions_e', models.CharField(max_length=255)),
                ('Qanalysis', models.CharField(max_length=255)),
                ('Qscore', models.FloatField()),
                ('Qdifficulty', models.IntegerField()),
                ('QTreeName', models.CharField(max_length=128)),
                ('Contest_id', models.IntegerField()),
                ('Qcreate_time', models.DateTimeField(default=datetime.datetime.now)),
                ('State', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sid', models.IntegerField()),
                ('Cid', models.IntegerField()),
                ('Eid', models.IntegerField()),
                ('Degree', models.IntegerField(default=0)),
                ('Auto_result', models.IntegerField(default=0)),
                ('Manul_result', models.IntegerField(default=0)),
                ('Create_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Studentinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sid', models.IntegerField()),
                ('Sname', models.CharField(max_length=32)),
                ('Sphone', models.CharField(max_length=12)),
                ('Spwd', models.CharField(max_length=64)),
                ('Ssex', models.CharField(max_length=12)),
                ('Ccname', models.CharField(max_length=32)),
                ('Cid', models.IntegerField(default=0)),
                ('Create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('Img_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacherinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tid', models.IntegerField()),
                ('Tphone', models.CharField(max_length=12)),
                ('Tname', models.CharField(max_length=32)),
                ('Tpwd', models.CharField(max_length=64)),
                ('Tsex', models.CharField(max_length=12)),
                ('Depart', models.CharField(max_length=32)),
                ('Create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('Img_url', models.CharField(max_length=255)),
            ],
        ),
    ]
