from django.contrib import admin
from jobs.models import JobOpportunity
from jobs.models import Application


# Register your models here.
class JobOpportunityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','enterprise_id']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(JobOpportunity, JobOpportunityAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'application_date','student_cpf',
        'job_opportunity', 'id',
    ]
    list_filter = [
        'job_opportunity',
    ]
    list_editable = [
        'job_opportunity',
    ]
    # prepopulated_fields = {'slug': ('numero', 'rua', 'cep',)}
    date_hierarchy = 'application_date'

admin.site.register(Application, ApplicationAdmin)


