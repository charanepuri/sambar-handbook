from django.db import models

class StateVariety(models.Model):
    state = models.CharField(max_length = 100)
    variety_name = models.CharField(max_length = 100)
    description = models.TextField()
    spice_level = models.CharField(max_length = 50)
    sweetness = models.CharField(max_length = 50)
    coconut_usage = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.variety_name
    
class Ingredient(models.Model):
    CATEGORY_CHOICES = [
        ('Lentil', 'Lentil'),
        ('Vegetable', 'Vegetable'),
        ('Spice', 'Spice'),
        ('Tempering', 'Tempering'),
        ('Garnish', 'Garnish'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='ingredients/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=100)

    state = models.ForeignKey(
        StateVariety,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        blank=True
    )

    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()

    instructions = models.TextField()

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )

    image = models.ImageField(
        upload_to='recipes/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
    
class Nutrition(models.Model):
    recipe = models.OneToOneField(
        Recipe,
        on_delete=models.CASCADE
    )

    calories = models.IntegerField()
    protein = models.FloatField()
    carbohydrates = models.FloatField()
    fiber = models.FloatField()

    def __str__(self):
        return self.recipe.title
    
class Fact(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    is_fun_fact = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('Ingredient', 'Ingredient'),
        ('Cooking', 'Cooking'),
        ('Dish', 'Dish'),
        ('Regional', 'Regional'),
        ('Vegetable', 'Vegetable'),
    ]

    title = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to='gallery/'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    def __str__(self):
        return self.title