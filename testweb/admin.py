from django.contrib import admin
from testweb.models import Student
from testweb.models import Test
from testweb.models import Signup
from testweb.models import Signup1
from testweb.models import Result
from testweb.models import Reset
from testweb.models import Physics
from testweb.models import PhysicsResult
from testweb.models import Chemistry
from testweb.models import ChemistryResult
from testweb.models import Math
from testweb.models import MathResult
from testweb.models import TeacherSignup
from testweb.models import Teacher
# Register your models here.


class Display(admin.ModelAdmin):
    list_display = ('srollno','sname')
    search_fields=('sname',)
    
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Signup,Display)
admin.site.register(Signup1,Display)
admin.site.register(Result)
admin.site.register(Reset)
admin.site.register(Chemistry)
admin.site.register(ChemistryResult)
admin.site.register(Physics)
admin.site.register(PhysicsResult)
admin.site.register(Math)
admin.site.register(MathResult)
admin.site.register(TeacherSignup)
admin.site.register(Teacher)