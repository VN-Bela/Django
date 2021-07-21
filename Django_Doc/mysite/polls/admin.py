from django.contrib import admin
from .models import Question,Choice

# Register your models here.

#class QuestionAdmin(admin.ModelAdmin):
 #   fieldsets=[
  ###]
   
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    
    ]
    list_filter = ['pub_date']
    list_display=('question_text','pub_date','was_published_recently')
    inlines=[ChoiceInline]
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
