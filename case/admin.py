from django.contrib import admin

from .models import Case, CaseParametr, CaseSection

admin.site.register(Case)
admin.site.register(CaseSection)
admin.site.register(CaseParametr)
