from django.contrib import admin

from polls.models import Choice, Question

# class QuestionAdmin(admin.ModelAdmin):
#     fields = [ 'pub_date','question_text']

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    fieldsets = [ 
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}) 
       ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)