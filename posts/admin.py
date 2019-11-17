from django.contrib import admin
'''TO DO: regitrar post en el administrador ''' 


from posts.models import Post
from django.contrib.auth.models import User
# admin.site.register(Post)

@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','profile','title','photo')
    list_display_links=('id','user')
    list_editable=('title','photo')
    search_fields=('title','user') # Como ven tambien se puede buscar por campos que son de relacion normal y solo de herencia no mas
    list_filter=('created','modified')
    fieldsets=(
        (
            'Profile',{
                'fields':(('user','profile'),
                         )
            }
        ),
        (
            'Post',{
                'fields':(('title','photo'),
                         )
            }
        ),
        (
            'Metadata',{
               'fields':(('created','modified'),
                ),
            }
        )
    )
    readonly_fields =('created','modified',)