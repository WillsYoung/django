from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'student', views.StudentEdit)

urlpatterns = [
    url(r'^index/', login_required(views.index)),
    url(r'stu_page', login_required(views.stu_page)),
    url(r'get/', views.get),
    url(r'^add_stu/', login_required(views.add_stu), name='add'),
    url(r'add_stu_info/(?P<stu_id>\d+)/', login_required(views.add_stu_info), name='addinfo')
]


urlpatterns += router.urls