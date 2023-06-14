# Generated by Django 4.2.2 on 2023-06-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_url', models.TextField(max_length=100)),
                ('next_event_date', models.TimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Under Consideration', 'Under Consideration'), ('Interview', 'Interview'), ('Declined', 'Declined'), ('Accepted', 'Accepted')], default='Applied', max_length=30)),
            ],
        ),
    ]
