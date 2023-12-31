# Generated by Django 4.2.3 on 2023-07-24 14:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service_name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "service_secret",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("task_description", models.CharField(max_length=100)),
                ("request_url", models.URLField()),
                (
                    "request_type",
                    models.IntegerField(choices=[(1, "GET"), (2, "POST")], default=1),
                ),
                ("request_body", models.JSONField(blank=True, null=True)),
                ("datatime", models.TextField(blank=True, null=True)),
                (
                    "task_status",
                    models.IntegerField(
                        choices=[(1, "ACTIVE"), (2, "BLOCK")], default=1
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.service"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("response", models.TextField(blank=True, null=True)),
                ("status", models.IntegerField(default=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.task"
                    ),
                ),
            ],
        ),
    ]
