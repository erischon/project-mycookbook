from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import RecipeDetailView, RecipeEditView, RecipeDeleteView, RecipeDetailEditModeView, IngredientEditView, IngredientAddView, InstructionEditView, InstructionAddView, TagEditView, TagAddView
from . import views


urlpatterns = [
    path('cookbook-create/', views.create_cookbook, name='cookbook_create'),
    path('recipe-create/', views.create_recipe, name='recipe_create'),
    path('<slug:pk>/detail', login_required(RecipeDetailView.as_view()), name='recipe-detail'),
    # path('<slug:pk>/social-detail/<slug:access_code>', RecipeDetailView.as_view(), name='social-detail'),
    path('<slug:pk>/detail/edit', login_required(RecipeDetailEditModeView.as_view()), name='recipe-edit-mode'),
    path('<slug:pk>/recipe-edit', login_required(RecipeEditView.as_view()), name='recipe-edit'),
    path('<slug:pk>/recipe-delete', login_required(RecipeDeleteView.as_view()), name='recipe-delete'),
    path('<int:pk>/ingredient-edit', login_required(IngredientEditView.as_view()), name='ingredient-edit'),
    path('<int:pk>/ingredient-add', login_required(IngredientAddView.as_view()), name='ingredient-add'),
    path('<int:pk>/instruction-edit', login_required(InstructionEditView.as_view()), name='instruction-edit'),
    path('<int:pk>/instruction-add', login_required(InstructionAddView.as_view()), name='instruction-add'),
    path('<int:pk>/tag-edit', login_required(TagEditView.as_view()), name='tag-edit'),
    path('<int:pk>/tag-add', login_required(TagAddView.as_view()), name='tag-add'),
]
