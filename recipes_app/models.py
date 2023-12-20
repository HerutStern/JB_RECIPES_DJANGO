from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from recipes_app.validators import validate_level


# recipe
class Recipe(models.Model):
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    level = models.CharField(max_length=10, db_column='level' ,validators=[validate_level], null=True, blank=True)
    ingredients = models.CharField(max_length=500, db_column='ingredients', null=False, blank=False)
    instructions = models.CharField(max_length=500, db_column='instructions', null=False, blank=False)
    delete = models.BooleanField(db_column='delete', null=False, blank=False, default=False)

    class Meta:
        db_table = 'recipe'

class Rating(models.Model):
    recipe = models.ForeignKey('Recipe', db_column='recipe', on_delete=models.RESTRICT,
                               null=False, blank=False, related_name='rating')
    rating_number = models.SmallIntegerField(db_column='rating_number', null=False, blank=False,
                                             validators=[MinValueValidator, MaxValueValidator])
    rating_date = models.DateField(db_column='rating_date', null=False, blank=False, auto_now_add=True)

    class Meta:
        db_table = 'rating'

class Profile(models.Model):
    user = models.OneToOneField(User, db_column='user', on_delete=models.RESTRICT, related_name='profile',)
    profession = models.CharField(max_length=50, db_column='profession', null=True, blank=True)
    address = models.CharField(max_length=256, db_column='address', null=True, blank=True)

    class Meta:
        db_table = 'profile'


