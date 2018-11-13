# Generated by Django 2.1.2 on 2018-11-13 05:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181113_0116'),
        ('conversation', '0002_auto_20181106_0401'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
        ('connection', '0002_auto_20181113_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='User_Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conversation.Conversation')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
