from django.contrib import admin
# from .models import Person
from .models import MySkillModel
from .models import Person, Group, Membership
# from .form import TodoAdminForm



# @admin.register(Car)
# class CarAdmin(admin.ModelAdmin):
#     list_display = ('name', 'owner', 'slug', 'year', 'created_at', 'id')
#     prepopulated_fields = {'slug': ('name',)}
    
    

# @admin.register(Authore)
# class AuthoreAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'print_year', 'id')


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author_names', 'id')

#     def author_names(self, obj):
#         return ", ".join([author.first_name + ' ' + author.last_name for author in obj.authore.all()])

    
    
# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'age', 'is_above', 'bio', 'create_person', 'id')
    
    
#     def is_above(self, obj):
#         if obj.age > 18:
#             return True
#         return False
    
#     is_above.boolean = True

# @admin.register(Todo)
# class TodoAdmin(admin.ModelAdmin):
#     form = TodoAdminForm
#     list_display = ('title', 'body', 'created', 'id')
    
    
@admin.register(MySkillModel)
class MySkillModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'id')
    


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id')
    

# @admin.register(Group)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('name', 'members_str', 'id')
    
#     def members_str(self, obj):
#         return ', '.join([i.name for i in obj.members.all()])
    
    
# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ('peson', 'group', 'date_joined', 'id')