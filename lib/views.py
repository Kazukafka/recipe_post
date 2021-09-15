from django.views.generic import ListView, CreateView  # ---この行を修正---

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe

# ---ここから追加---


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ["title", "content", "description"]
# ---ここまで追加---
