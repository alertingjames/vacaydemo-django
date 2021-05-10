# Generated by Django 3.0.7 on 2020-06-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('cohort', models.CharField(max_length=20)),
                ('registered_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=11)),
                ('member_id', models.CharField(max_length=11)),
                ('comment_text', models.CharField(max_length=2000)),
                ('image_url', models.CharField(max_length=1000)),
                ('commented_time', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('group_id', models.CharField(max_length=11)),
                ('cohort', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('video_url', models.CharField(max_length=1000)),
                ('participants', models.CharField(max_length=11)),
                ('event_time', models.CharField(max_length=50)),
                ('created_time', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('likes', models.CharField(max_length=11)),
                ('status', models.CharField(max_length=20)),
                ('gname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('contact_email', models.CharField(max_length=80)),
                ('contacted_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=100)),
                ('member_count', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('created_time', models.CharField(max_length=50)),
                ('last_connected_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GroupConnect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('group_id', models.CharField(max_length=11)),
                ('last_connected_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=11)),
                ('member_id', models.CharField(max_length=11)),
                ('invited_time', models.CharField(max_length=50)),
                ('last_connected_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=11)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=30)),
                ('fb_photo', models.CharField(max_length=1000)),
                ('gl_photo', models.CharField(max_length=1000)),
                ('photo_url', models.CharField(max_length=1000)),
                ('phone_number', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
                ('cohort', models.CharField(max_length=100)),
                ('registered_time', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
                ('playerID', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('sender_id', models.CharField(max_length=11)),
                ('message', models.CharField(max_length=5000)),
                ('notified_time', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=5000)),
                ('picture_url', models.CharField(max_length=1000)),
                ('video_url', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=11)),
                ('posted_time', models.CharField(max_length=100)),
                ('likes', models.CharField(max_length=11)),
                ('liked', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=11)),
                ('member_id', models.CharField(max_length=11)),
                ('liked_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=11)),
                ('picture_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Received',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('sender_id', models.CharField(max_length=11)),
                ('noti_id', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Replied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('root_id', models.CharField(max_length=11)),
                ('noti_id', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Sent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=11)),
                ('sender_id', models.CharField(max_length=11)),
                ('noti_id', models.CharField(max_length=11)),
            ],
        ),
    ]
