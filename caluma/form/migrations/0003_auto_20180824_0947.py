# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-24 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("form", "0002_auto_20180823_1514")]

    operations = [
        migrations.CreateModel(
            name="FormQuestion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.PositiveIntegerField(
                        db_index=True, default=0, editable=False
                    ),
                ),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="form.Form"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="form.Question"
                    ),
                ),
            ],
            options={"ordering": ("-sort_order", "id")},
        ),
        migrations.AddField(
            model_name="form",
            name="questions",
            field=models.ManyToManyField(
                related_name="forms", through="form.FormQuestion", to="form.Question"
            ),
        ),
    ]
