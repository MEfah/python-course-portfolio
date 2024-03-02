"""
Функции панели управления для приложения "Блог".
"""

from django.contrib import admin

from blog.models import Blog
from blog.models import ContactInfo


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "publication_date",
        "created_at",
        "updated_at",
    )

    search_fields = ("title", "content")

    list_filter = (
        "created_at",
        "updated_at",
    )


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = (
        "info_type",
        "description",
        "value",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "value",
        "description",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
