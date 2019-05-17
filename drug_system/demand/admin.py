from django.contrib import admin

# Register your models here.
from .models import Medicine, Demander, Detail, Demand, Demander_Demand, Medicine_type
admin.site.register(Medicine)
admin.site.register(Demander)
admin.site.register(Detail)
admin.site.register(Demand)
admin.site.register(Demander_Demand)
admin.site.register(Medicine_type)
