# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comments'
        db.create_table(u'comments_comments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=50)),
        ))
        db.send_create_signal(u'comments', ['Comments'])


    def backwards(self, orm):
        # Deleting model 'Comments'
        db.delete_table(u'comments_comments')


    models = {
        u'comments.comments': {
            'Meta': {'object_name': 'Comments'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['comments']