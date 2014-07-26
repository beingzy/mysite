import datetime
from mongoengine import *

class Blog(Document):
	title   = StringField(max_length=256, required=True)
	created = DateTimeField(default=datetime.datetime.now,   required=True)
	updated = DateTimeField(default=datetime.datetime.now,   required=True)
	author  = StringField(max_length=128, default="beingzy", required=True)
	body    = StringField(required=True)
	tags    = ListField(StringField(), required=False)

class Resume(Document):
	first_name  = StringField(max_length=128, required=True)
	last_name   = StringField(max_length=128, required=True)
	middle_name = StringField(max_length=128, required=False)
	phone       = StringField(max_length=128, required=True)
	email       = EmailField(required=True)
	version     = FloatField(required=True)

class Moto(Document):
	created = DateTimeField(default=datetime.datetime.now,   required=True)
	body    = StringField(max_length=1000, required=True)
	tags    = ListField(StringField(), required=True) 