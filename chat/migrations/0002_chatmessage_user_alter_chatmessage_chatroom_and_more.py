# Generated by Django 4.2.4 on 2023-08-18 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(db_column='user_id', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='chatroom',
            field=models.ForeignKey(db_column='chatroom_id', on_delete=django.db.models.deletion.CASCADE, related_name='chat_room', to='chat.chatroom'),
        ),
        migrations.AlterField(
            model_name='chatroomjoin',
            name='chatroom',
            field=models.ForeignKey(db_column='chatroom_id', on_delete=django.db.models.deletion.CASCADE, related_name='room_join', to='chat.chatroom'),
        ),
    ]
