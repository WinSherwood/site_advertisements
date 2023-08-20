from django.contrib import admin

from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'descriptions', 'price', 'trades', 'created_date', 'updated_at', 'user', 'created_foto']
    list_filter = ['date_now', 'descriptions', 'trades']
    fieldsets = (
        ("Первый блок", {
            "fields": ("title", "descriptions", "image", "user")}),
        ("Второй блок", {
            "classes": ("collapse",),
            "fields": ("price", "trades")}),
    )
    actions = ["make_true", "make_false", "created_date", 'updated_at']

    @admin.action(description="Обновить торг на True")
    def make_true(self, request, queryset):
        queryset.update(trades=True)

    @admin.action(description="Обновить торг на False")
    def make_false(self, request, queryset):
        queryset.update(trades=False)


admin.site.register(Advertisement, AdvertisementAdmin)
