from django.contrib import admin
from .models import Sprint, Task

# Register the models so they appear in Django admin
admin.site.register(Sprint)
admin.site.register(Task)