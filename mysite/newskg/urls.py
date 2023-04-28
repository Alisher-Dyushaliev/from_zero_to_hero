from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page
# from rest_framework.routers import SimpleRouter
#
# router = SimpleRouter ()
# router.register('api/app', LangListView)

urlpatterns = [
    path ('', MainLang.as_view (), name='main'),
    # path ('', cache_page(60)(MainLang.as_view ()), name='main'),
    path ('pur/<int:purpose_id>/', PurposeLang.as_view (), name='purpose'),
    path ('framework/<int:pk>/', InfoLang.as_view (), name='framework'),
    path ('tag/<str:slug>/', TagLang.as_view (), name='tag'),
    path ('lang/add-lang/', AddLang.as_view (), name='add_lang'),
    path ('search/', Search.as_view (), name='search'),
    path ('mail/', email, name='captcha'),
    path ('registration/', registration, name='registration'),
    path ('login/', user_login, name='login'),
    path ('logout/', user_logout, name='logout'),
    path ('mptt/', get_mptt, name='mptt'),
    path ('tree/<int:pk>/', get_tree, name='tree'),
    # path ('', index, name='main'),
    # path ('pur/<int:purpose_id>/', get_purpose, name='purpose'),
    # path ('framework/<int:framework_id>/', framework, name='framework'),
    # path ('lang/add-lang/', lang_add, name='add_lang'),
]

# urlpatterns += router.urls