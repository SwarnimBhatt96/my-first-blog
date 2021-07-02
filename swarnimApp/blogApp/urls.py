from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.postList, name = 'post_list'),
    
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='blogApp/templates/registration/login.html'), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    path('post/<int:pk>/', views.postDetails, name = 'post_detail'),
    path('post/new', views.postNew, name = 'post_new' ),
    path('post/<int:pk>/edit/', views.postEdit, name='post_edit'),
    path('drafts/', views.postDraftList, name = 'post_draft_list'),
    path('post_publish/<int:pk>', views.postPublish, name = 'post_publish'),
    path('post/<int:pk>/remove/', views.postDelete, name = 'post_delete'),
    path('post/<int:pk>/comment/', views.addComment, name = 'add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.approveComment, name = 'comment_approve'),
    path('comment/<int:pk>/remove', views.removeComment, name = 'comment_remove'),
    
    
    
    
]