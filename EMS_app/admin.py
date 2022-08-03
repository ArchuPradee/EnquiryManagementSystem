from django.contrib import admin
from EMS_app import models


admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Student)
admin.site.register(models.Enquiry)

