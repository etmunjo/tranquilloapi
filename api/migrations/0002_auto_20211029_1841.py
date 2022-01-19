# Generated by Django 3.1.7 on 2021-10-29 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.TextField(max_length=20)),
                ('lastName', models.TextField(max_length=20)),
                ('bio', models.TextField(max_length=124)),
                ('instrument', models.CharField(choices=[('Blank', 'Blank'), ('accordian', 'accordian'), ('air horn', 'air horn'), ('baby grand piano', 'baby grand piano'), ('bagpipe', 'bagpipe'), ('banjo', 'banjo'), ('bass guitar', 'bass guitar'), ('bassoon', 'bassoon'), ('bugle', 'bugle'), ('calliope', 'calliope'), ('cello', 'cello'), ('clarinet', 'clarinet'), ('clavichord', 'clavichord'), ('concertina', 'concertina'), ('didgeridoo', 'didgeridoo'), ('dobro', 'dobro'), ('dulcimer', 'dulcimer'), ('fiddle', 'fiddle'), ('fife', 'fife'), ('flugelhorn', 'flugelhorn'), ('flute', 'flute'), ('French horn', 'French horn'), ('glockenspiel', 'glockenspiel'), ('grand piano', 'grand piano'), ('guitar', 'guitar'), ('harmonica', 'harmonica'), ('harp', 'harp'), ('harpsichord', 'harpsichord'), ('hurdy-gurdy', 'hurdy-gurdy'), ('kazoo', 'kazoo'), ('kick drum', 'kick drum'), ('lute', 'lute'), ('lyre', 'lyre'), ('mandolin', 'mandolin'), ('marimba', 'marimba'), ('mellotran', 'mellotran'), ('melodica', 'melodica'), ('oboe', 'oboe'), ('pan flute', 'pan flute'), ('piano', 'piano'), ('piccolo', 'piccolo'), ('pipe organ', 'pipe organ'), ('saxaphone', 'saxaphone'), ('sitar', 'sitar'), ('sousaphone', 'sousaphone'), ('tambourine', 'tambourine'), ('theremin', 'theremin'), ('trombone', 'trombone'), ('tuba', 'tuba'), ('ukulele', 'ukulele'), ('viola', 'viola'), ('violin', 'violin'), ('vuvuzela', 'vuvuzela'), ('washtub bass', 'washtub bass'), ('xylophone', 'xylophone'), ('zither', 'zither')], default='Blank', max_length=40)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['-dateOfTask']},
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='body',
            new_name='taskDetails',
        ),
        migrations.AddField(
            model_name='tasks',
            name='Status',
            field=models.CharField(choices=[('Not Started', 'Not Started'), ('Starting', 'Starting'), ('On Hold', 'On Hold'), ('Almost Done', 'Almost Done'), ('Done', 'Done')], default='Not Started', max_length=25),
        ),
        migrations.AddField(
            model_name='tasks',
            name='dateOfTask',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
