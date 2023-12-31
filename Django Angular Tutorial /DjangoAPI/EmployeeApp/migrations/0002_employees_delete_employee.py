# Generated by Django 4.2.3 on 2023-07-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("EmployeeApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                ("EmployeeID", models.AutoField(primary_key=True, serialize=False)),
                ("EmployeeName", models.CharField(max_length=100)),
                ("Department", models.CharField(max_length=100)),
                ("DateOfJoining", models.DateField()),
                ("PhotoFileName", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
    ]
