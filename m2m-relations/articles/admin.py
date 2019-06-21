from django.contrib import admin

from .models import Article, Scope, Data

from django.core.exceptions import ValidationError

from django.forms import BaseInlineFormSet


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):

        counter = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    counter += 1

        if counter != 1:
            raise ValidationError('Главный тэг может быть только один')

        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Data
    formset = RelationshipInlineFormset


@admin.register(Scope)
class ObjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
