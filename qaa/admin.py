from django.contrib import admin
from qaa.models import Question, Answer, Category

class QuestionAdmin(admin.ModelAdmin):
    fields=['title', 'asked_by', 'category', 'desc', 'pub_date']

class AnswerAdmin(admin.ModelAdmin):
    fields=['answer', 'question', 'submitted_by', 'pub_date', 'is_best']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['title']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category, CategoryAdmin)
