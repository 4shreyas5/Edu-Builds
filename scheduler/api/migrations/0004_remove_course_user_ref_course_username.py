# Generated by Django 4.1.5 on 2023-01-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_rename_user_id_course_user_ref"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="user_ref",
        ),
        migrations.AddField(
            model_name="course",
            name="username",
            field=models.CharField(default="root", max_length=20),
        ),
    ]