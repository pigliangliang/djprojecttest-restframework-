from django.contrib import admin

# Register your models here.


from bbs import models

class BBS_admin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'author', 'signature', 'view_count', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'author__user__username')


    def signature(self, obj):
        return obj.author.signature


    #signature.short_description = 'hah'

admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
