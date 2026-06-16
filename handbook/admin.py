from django.contrib import admin
from .models import (
    StateVariety,
    Ingredient,
    Recipe,
    Nutrition,
    Fact,
    Gallery
)

admin.site.register(StateVariety)
admin.site.register(Ingredient)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'state',
        'difficulty',
        'preparation_time',
        'cooking_time'
    )

    list_filter = (
        'difficulty',
        'state'
    )

    search_fields = (
        'title',
    )
    
    list_per_page = 10

admin.site.register(Nutrition)
admin.site.register(Fact)
admin.site.register(Gallery)