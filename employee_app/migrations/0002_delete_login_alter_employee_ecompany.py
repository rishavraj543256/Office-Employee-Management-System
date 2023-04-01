# Generated by Django 4.1.3 on 2023-04-01 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.AlterField(
            model_name='employee',
            name='eCompany',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.company'),
        ),
    ]
