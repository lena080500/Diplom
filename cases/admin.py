from django.contrib import admin

# Register your models here.
from cases.models import Case, CaseSection, CaseParametr

admin.site.register(Case)
admin.site.register(CaseSection)
admin.site.register(CaseParametr)
