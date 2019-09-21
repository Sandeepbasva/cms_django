from django.conf.urls import url
from .views import students_list, student_details


urlpatterns = [
    url(r'studentList/?$', students_list, name='students_list'),
    url(r'studentDetail/(?P<sid>[a-zA-Z0-9]+)/?$', student_details, name='student_details')
]
