# todo_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_app.urls')),
    path('', lambda request: HttpResponse("Welcome to the Todo App")),  # Optional welcome view
]
