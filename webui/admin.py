from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import action

from . import models


@action(description="Печать РПД")
def print_subject(model_admin, request, queryset):
    print(model_admin)
    print(request)
    print(queryset)


class SubjectModelAdmin(ModelAdmin):
    actions = [print_subject]


admin.site.register(models.EducationPlan)
admin.site.register(models.Subject, SubjectModelAdmin)
