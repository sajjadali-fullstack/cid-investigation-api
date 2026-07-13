from django.contrib import admin
from testapp.models import Officer, Criminal, Case, Evidence, Witness

# Register your models / SQL Table here.

class OfficerAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'joining_date')
    search_fields = ('name', 'rank', 'joining_date')


class CriminalAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'age', 'gender', 'criminal_history', 'wanted')
    search_fields = ('name', 'alias', 'age', 'gender', 'criminal_history', 'wanted')


class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'case_number', 'description', 'location', 'date_registered', 'status')
    search_fields = ('title', 'case_number', 'description', 'location', 'date_registered', 'status')


class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('case', 'evidence_type', 'description', 'collected_by', 'collected_on')
    search_fields = ('case', 'evidence_type', 'description', 'collected_by', 'collected_on')


class WitnessAdmin(admin.ModelAdmin):
    list_display = ('case', 'name', 'phone', 'statement')
    search_fields = ('case', 'name', 'phone', 'statement')

admin.site.register(Officer, OfficerAdmin)
admin.site.register(Criminal, CriminalAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Evidence, EvidenceAdmin)
admin.site.register(Witness, WitnessAdmin)