
from records.views import addUser
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', addUser)
#localhost/api/user ----list()
#localhost/api/user/5 ----retrive
