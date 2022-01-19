from django.contrib import admin
from .models import Question, Choice, Artist, Album, Song

# Register your models here.

class ChoiceInline(admin.StackedInline):
# class ChoiceInline(admin.TabularInline):
# TabularInline 扁平化显示
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
# # 排序，默认pub_date是在question_text后面的
#     fields = ['pub_date','question_text']

# 分段
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')

    # 对显示结果过滤
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
# admin.site.register(Choice)
# admin.site.register(Question)