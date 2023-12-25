from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class RecipeList(ListView):
    # model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetail(DetailView):
    # model = Recipe
    template_name = 'recipe_detail.html'
    context_object_name = 'recipe'
    
class RecipeCreate(CreateView):
    # model = Recipe
    template_name = 'recipe_form.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('recipe_list')

class RecipeUpdate(UpdateView):
    # model = Recipe
    template_name = 'recipe_update.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('recipe_list')

class RecipeDelete(DeleteView):
    # model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
