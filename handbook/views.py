from django.shortcuts import render, get_object_or_404
from .models import (
    StateVariety,
    Ingredient,
    Recipe,
    Nutrition,
    Fact,
    Gallery
)
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):

    recipe_count = Recipe.objects.count()
    ingredient_count = Ingredient.objects.count()
    variety_count = StateVariety.objects.count()
    fact_count = Fact.objects.count()

    recipes = Recipe.objects.all()[:3]

    context = {
        'recipe_count': recipe_count,
        'ingredient_count': ingredient_count,
        'variety_count': variety_count,
        'fact_count': fact_count,
        'recipes': recipes
    }

    return render(
        request,
        'handbook/home.html',
        context
    )


def history(request):
    return render(request, 'handbook/history.html')


def varieties(request):
    varieties = StateVariety.objects.all()

    return render(
        request,
        'handbook/varieties.html',
        {
            'varieties': varieties
        }
    )


def ingredients(request):
    ingredients = Ingredient.objects.all()

    return render(
        request,
        'handbook/ingredients.html',
        {
            'ingredients': ingredients
        }
    )

def recipes(request):

    recipe_list = Recipe.objects.all()

    paginator = Paginator(
        recipe_list,
        6
    )

    page_number = request.GET.get('page')

    recipes = paginator.get_page(
        page_number
    )

    return render(
        request,
        'handbook/recipes.html',
        {
            'recipes': recipes
        }
    )


def nutrition(request):
    nutrition = Nutrition.objects.all()

    return render(
        request,
        'handbook/nutrition.html',
        {
            'nutrition': nutrition
        }
    )
    
def recipe_detail(request, id):
    recipe = get_object_or_404(
        Recipe,
        id=id
    )

    return render(
        request,
        'handbook/recipe_detail.html',
        {
            'recipe': recipe
        }
    )


def tips(request):
    return render(request, 'handbook/tips.html')


def gallery(request):

    category = request.GET.get('category')

    images = Gallery.objects.all()

    if category:
        images = images.filter(
            category=category
        )

    context = {
        'images': images
    }

    return render(
        request,
        'handbook/gallery.html',
        context
    )

def history(request):
    return render(request, 'handbook/history.html')

def facts(request):

    facts = Fact.objects.filter(
        is_fun_fact=False
    )

    fun_facts = Fact.objects.filter(
        is_fun_fact=True
    )

    context = {
        'facts': facts,
        'fun_facts': fun_facts
    }

    return render(
        request,
        'handbook/facts.html',
        context
    )

def ingredient_detail(request, id):
    ingredient = get_object_or_404(
        Ingredient,
        id=id
    )

    return render(
        request,
        'handbook/ingredient_detail.html',
        {
            'ingredient': ingredient
        }
    )

def variety_detail(request, id):
    variety = get_object_or_404(
        StateVariety,
        id=id
    )

    return render(
        request,
        'handbook/variety_detail.html',
        {
            'variety': variety
        }
    )


def search(request):
    query = request.GET.get('q')

    recipes = Recipe.objects.filter(
        Q(title__icontains=query)
    )

    ingredients = Ingredient.objects.filter(
        Q(name__icontains=query)
    )

    context = {
        'query': query,
        'recipes': recipes,
        'ingredients': ingredients
    }

    return render(
        request,
        'handbook/search.html',
        context
    )
    
def contact(request):
    return render(
        request,
        'handbook/contact.html'
    )
    
def about(request):
    return render(request, 'handbook/about.html')


def ingredients(request):
    ingredients = Ingredient.objects.all()

    return render(
        request,
        'handbook/ingredients.html',
        {'ingredients': ingredients}
    )


def ingredient_detail(request, id):
    ingredient = get_object_or_404(
        Ingredient,
        id=id
    )

    return render(
        request,
        'handbook/ingredient_detail.html',
        {'ingredient': ingredient}
    )

def variety_detail(request, id):
    variety = get_object_or_404(
        StateVariety,
        id=id
    )

    return render(
        request,
        'handbook/variety_detail.html',
        {'variety': variety}
    )
    
def shopping_list(request):
    return render(
        request,
        'handbook/shopping_list.html'
    )