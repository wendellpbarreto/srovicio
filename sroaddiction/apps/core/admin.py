#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from .models import *

admin.site.unregister(Group)
# admin.site.unregister(Site)

# admin.site.register(Account)

class AccountInline(admin.StackedInline):
	model = Account
	extra = 1
	max_num = 20
	can_delete = True
	classes = ('grp-collapse grp-open',)
	inline_classes = ('grp-collapse grp-open',)
	fields = (
		('agency', 'account', 'operation',),
		('type',),
		('owner',),
	)

	verbose_name = _('Account')
	verbose_name_plural = _('Accounts')

class BankAdmin(admin.ModelAdmin):
	model = Bank
	inlines = (AccountInline,)
	fields = (
		('name', 'image',),
		('observation',),
	)

	verbose_name = _('Bank')
	verbose_name_plural = _('Banks')

admin.site.register(Bank, BankAdmin)

admin.site.register(Nationality)

class ImageInline(admin.TabularInline):
	model = Image
	extra = 1
	max_num = 10
	can_delete = True

	verbose_name = _('Image')
	verbose_name_plural = _('Images')

class VideoInline(admin.TabularInline):
	model = Video
	extra = 1
	max_num = 10
	can_delete = True

	verbose_name = _('Video')
	verbose_name_plural = _('Videos')

class NewsInline(admin.TabularInline):
	model = News
	extra = 1
	max_num = 10
	can_delete = True

	verbose_name = _('News')
	verbose_name_plural = _('News')

class ServerAdmin(admin.ModelAdmin):
	inlines = (
		ImageInline,
		VideoInline,
		NewsInline,
	)
	fieldsets = (
		(
			None, {
				'fields' : ('name', 'description',)
			}
		),
		(	
			None, {
				'fields' : (
					('originality', 'nationality',),
				)
			}
		),
		(
			_('Informations'), {
			    'classes': ('grp-collapse grp-open',),
				'fields' : (
					('cap', 'degree',),
					('mastery', 'exp_rate',),
					('exp_party_rate', 'gold_drop_rate',),
					('item_drop_rate', 'alchemy_rate',),
				)
			}
		),
		(
			_('Links'), {
			    'classes': ('grp-collapse grp-open',),
				'fields' : ('website_link', 'website_register_link',)
			}
		)
	)
	list_display = ('name', 'cap', 'originality', 'nationality',)
	list_filter = ('originality', 'nationality__name')
	search_fields = ('name', 'cap', 'originality', 'nationality__name',)
	ordering = ('name', 'cap', 'originality', 'nationality',)

	verbose_name = _('Server')
	verbose_name_plural = _('Servers')

admin.site.register(Server, ServerAdmin)

class TypeAdmin(admin.ModelAdmin):
	model = Type

	verbose_name = _('Type of price table')
	verbose_name_plural = _('Types of price tables')

admin.site.register(Type, TypeAdmin)

class PriceInline(admin.TabularInline):
	model = Price
	extra = 1
	max_num = 99
	can_delete = True

	verbose_name = _('Price')
	verbose_name_plural = _('Prices')
	
class PriceTableAdmin(admin.ModelAdmin):
	inlines = (PriceInline,)
	fields = (('type', 'server',),)
	list_display = ('server', 'type')
	list_filter = ('server__name', 'type__name')
	search_filter = ('server__name', 'type__name')
	ordering = ('server',)

admin.site.register(PriceTable, PriceTableAdmin)
