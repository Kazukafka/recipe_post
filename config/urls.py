from django.contrib import admin
from django.urls import path

from lib.views import IndexTemplateView  # --- この行を追加 ---
from recipe.views import RecipeListView


urlpatterns = [
    path('admin/', admin.site.urls),
    # --- ここから修正 ---
    path('recipe/', RecipeListView.as_view(), name="recipe-index"),
    path('', IndexTemplateView.as_view(), name="index"),
    # --- ここまで修正 ---
]
