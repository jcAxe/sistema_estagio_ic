from django.contrib import admin
from user_actions.models import Student
from user_actions.models import Enterprise



# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','major_id',
                    'id_doc_number', 'registered']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Student, StudentAdmin)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','registered']

    prepopulated_fields = {'slug': ('name',)}
    # prepopulated_fields = {'slug': ('numero', 'rua', 'cep',)}

    date_hierarchy = 'register_date'

admin.site.register(Enterprise, EnterpriseAdmin)


