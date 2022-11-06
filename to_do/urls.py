from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .views import HomePage, BoardCreateAPIView, \
    BoardUpdateDestroyAPIView, BoardListAPIView, TodoCreateAPIView, \
    TodoListAPIView


schema_view = get_schema_view(
    openapi.Info(
        title="To-Do API",
        default_version='v1',
        description="""
        Descriptions of the exact clarity and understanding 
        of the project to implement and simplify the use of this site!
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="vadimsalapugin@gmail.com"),
        license=openapi.License(name="For Free!"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

swagger_urls = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns = [
    # Main page
    path('', HomePage.as_view(), name='home-page'),

    # APIViews for boards
    path('list-boards/', BoardListAPIView.as_view(), name='list-boards'),
    path('create-board/', BoardCreateAPIView.as_view(), name='create-board'),
    path('upd-del-board/<int:pk>/', BoardUpdateDestroyAPIView.as_view(), name='upd-del-board'),

    # APIView for tasks
    path('todo-create/', TodoCreateAPIView.as_view(), name='todo-create'),
    path('todo-list/<int:pk>', TodoListAPIView.as_view(), name='todo-list')
]

urlpatterns += swagger_urls
