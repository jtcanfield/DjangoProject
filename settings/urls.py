"""firstdjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import greeting_view
from core.views import bmi
from core.views import bmi_measurement
from core.views import goodbye_view

# ^ beginning of string
# $ end of string
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bmimeasurement', bmi_measurement),
    url(r'^bmi', bmi),
    url(r'^goodbye', goodbye_view),
    url(r'^$', greeting_view),
]
