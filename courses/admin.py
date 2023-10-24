# from django.contrib import admin
# from .models import Article, Courses, Onepart
# from .form import NotNoneArticleForm


# @admin.register(Courses)
# class CoursesAdmin(admin.ModelAdmin):
#     list_display = ('title', 'lenght')
    
    

# @admin.register(Onepart)
# class OnepartAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description')
    
    

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     form = NotNoneArticleForm
#     list_display = ('title', 'body')
    
#     def clean(self):
#         title = self.cleaned_data.get('title')
#         if title == 'None':
#             raise 


# admin.site.register(Comment)