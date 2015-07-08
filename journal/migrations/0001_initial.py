# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=2, choices=[(b'C', b'Cricket'), (b'H', b'Hockey'), (b'F', b'Football')])),
                ('hero_image', models.ImageField(default=b'pic_folder/None/hero-no-img.jpg', upload_to=b'pic_folder/')),
                ('optional_image', models.ImageField(default=b'pic_folder/None/opt-no-img.jpg', upload_to=b'pic_folder/')),
                ('body', models.CharField(default=b'', max_length=1000)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pub_date',),
            },
            bases=(models.Model,),
        ),
    ]
