from django.contrib import admin
from blog.models import Post
# Register your models here.


@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title', )}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
    # 모델 오브젝트.all()결과로 queryset타입ㅔ의 리턴값