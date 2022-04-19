from django.contrib import admin

# Register your models here.
from case.models import Case, CaseParametr, CaseSection

admin.site.register(Case)
admin.site.register(CaseSection)
admin.site.register(CaseParametr)
