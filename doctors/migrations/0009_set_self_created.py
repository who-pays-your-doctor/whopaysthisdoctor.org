# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for doctor in orm.Doctor.objects.all():
            doctor.self_created = True
            doctor.save()
        for decl in orm.Declaration.objects.all():
            decl.self_created = True
            decl.save()

    def backwards(self, orm):
        for doctor in orm.Doctor.objects.all():
            doctor.self_created = False
            doctor.save()
        for decl in orm.Declaration.objects.all():
            decl.self_created = False
            decl.save()

    models = {
        u'doctors.declaration': {
            'Meta': {'object_name': 'Declaration'},
            'date_created': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2019, 6, 16, 0, 0)'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Doctor']"}),
            'dt_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 6, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_declarations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'past_declarations': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'self_created': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'doctors.declarationlink': {
            'Meta': {'object_name': 'DeclarationLink'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'expires': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 6, 30, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'cbcd30a2'", 'unique': 'True', 'max_length': '64'})
        },
        u'doctors.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'employment_address': ('django.db.models.fields.TextField', [], {}),
            'gmc_number': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'primary_employer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'self_created': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'doctors.feebenefit': {
            'Meta': {'object_name': 'FeeBenefit'},
            'band': ('django.db.models.fields.IntegerField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Declaration']", 'null': 'True', 'blank': 'True'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'doctors.grantbenefit': {
            'Meta': {'object_name': 'GrantBenefit'},
            'band': ('django.db.models.fields.IntegerField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Declaration']", 'null': 'True', 'blank': 'True'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'doctors.importeddoctorcompanylink': {
            'Meta': {'object_name': 'ImportedDoctorCompanyLink'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'company_link': ('django.db.models.fields.URLField', [], {'max_length': '300'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'officer_link': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        },
        u'doctors.othermedicalbenefit': {
            'Meta': {'object_name': 'OtherMedicalBenefit'},
            'band': ('django.db.models.fields.IntegerField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Declaration']", 'null': 'True', 'blank': 'True'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'doctors.pharmabenefit': {
            'Meta': {'object_name': 'PharmaBenefit'},
            'band': ('django.db.models.fields.IntegerField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'declaration': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Declaration']", 'null': 'True', 'blank': 'True'}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['doctors.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['doctors']
    symmetrical = True
