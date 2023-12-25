from django.contrib import admin
from django.urls import path, include # 👈 1. add this 

# 👇 2. Add those two line


urlpatterns = [
 
    path('admin/', admin.site.urls),

    # 👇 3. add this line too
    path('', include('menu_app.urls'))

# 👇 4. Add below line too
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)