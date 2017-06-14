from django.contrib import admin
from .models import StudiesTypeOffered, StudiesOffertList, StudiesOffert

# Register your models here.

@admin.register(StudiesTypeOffered)
class StudiesTypeOfferedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(StudiesOffertList)
class StudiesOffertListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(StudiesOffert)
class StudiesOffertAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_list',)

    def get_queryset(self, request):
        return super(StudiesOffertAdmin, self).get_queryset(request).prefetch_related('knowledge_topics')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.knowledge_topics.all())
