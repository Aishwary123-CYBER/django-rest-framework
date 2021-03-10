from informationapi.viewset import TeacherViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teacher',TeacherViewsets)

#something like localhost : p/api/ will be triggered from our urls.py file

#list = we have to make request like (localhost:p/api/teacher) to post request 

#retrive = for single record (localhost:p/api/teacher/id)

#The information will be stored in postre database table which we have created in models!

