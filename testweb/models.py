from django.db import models



# Create your models here.
class Student(models.Model):
    srollno = models.CharField(max_length=10,primary_key=True)
    sname = models.CharField(max_length=50)
    sattempt = models.IntegerField(default=0)
    spoints = models.FloatField(default=0)
    def __str__(self):
        return self.sname
    
    
    

    
    
class Test(models.Model):
    qno=models.IntegerField(primary_key=True)
    qname = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now=True)
    qclass = models.CharField(max_length=1)
    a = models.CharField(max_length=100, default='SOME STRING')
    b = models.CharField(max_length=100, default='SOME STRING')
    c = models.CharField(max_length=100, default='SOME STRING')
    d = models.CharField(max_length=100, default='SOME STRING')
    def __str__(self):
        return self.qclass
    
    


class Chemistry(models.Model):
    qno=models.IntegerField(primary_key=True)
    qname = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now=True)
    qclass = models.CharField(max_length=1)
    a = models.CharField(max_length=100, default='SOME STRING')
    b = models.CharField(max_length=100, default='SOME STRING')
    c = models.CharField(max_length=100, default='SOME STRING')
    d = models.CharField(max_length=100, default='SOME STRING')
    def __str__(self):
        return self.qclass
    
    


class Physics(models.Model):
    qno=models.IntegerField(primary_key=True)
    qname = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now=True)
    qclass = models.CharField(max_length=1)
    a = models.CharField(max_length=100, default='SOME STRING')
    b = models.CharField(max_length=100, default='SOME STRING')
    c = models.CharField(max_length=100, default='SOME STRING')
    d = models.CharField(max_length=100, default='SOME STRING')
    def __str__(self):
        return self.qclass
    
    
    
    
    
class Math(models.Model):
    qno=models.IntegerField(primary_key=True)
    qname = models.CharField(max_length=500)
    add_date = models.DateTimeField(auto_now=True)
    qclass = models.CharField(max_length=1)
    a = models.CharField(max_length=100, default='SOME STRING')
    b = models.CharField(max_length=100, default='SOME STRING')
    c = models.CharField(max_length=100, default='SOME STRING')
    d = models.CharField(max_length=100, default='SOME STRING')
    def __str__(self):
        return self.qclass
    



class Result(models.Model):
    resultid = models.BigAutoField(primary_key=True,auto_created=True)
    username = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt = models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField()
    points = models.FloatField()
    
    
    


class PhysicsResult(models.Model):
    resultid = models.BigAutoField(primary_key=True,auto_created=True)
    username = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt = models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField()
    points = models.FloatField()
    
    
    

class ChemistryResult(models.Model):
    resultid = models.BigAutoField(primary_key=True,auto_created=True)
    username = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt = models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField()
    points = models.FloatField()   
    
    
    
    
class MathResult(models.Model):
    resultid = models.BigAutoField(primary_key=True,auto_created=True)
    username = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    attempt = models.IntegerField()
    right = models.IntegerField()
    wrong = models.IntegerField()
    points = models.FloatField()
     

    
class Signup(models.Model):
    sname = models.CharField(max_length=50)
    srollno = models.CharField(max_length=25,primary_key=True)
    spass = models.CharField(max_length=150)
    def __str__(self):
        return self.spass
   
    

class Signup1(models.Model):
    sname = models.CharField(max_length=50)
    srollno = models.CharField(max_length=25,primary_key=True)
    spass = models.CharField(max_length=150)
    def __str__(self):
        return self.srollno




class TeacherSignup(models.Model):
    empid = models.CharField(max_length=10,primary_key=True)
    ename = models.CharField(max_length=50)
    epass = models.CharField(max_length=150)
    esubject = models.CharField(max_length=50)
    def __str__(self):
        return self.empid
    
    
    
    
class Teacher(models.Model):
    empid = models.CharField(max_length=10,primary_key=True)
    ename = models.CharField(max_length=50)
    esubject = models.CharField(max_length=50)
    def __str__(self):
        return self.ename
    



class Reset(models.Model):
    sid = models.BigAutoField(primary_key=True,auto_created=True)
    srollno = models.CharField(max_length=25)
    stoken = models.CharField(max_length=100)
    spass = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    def __str__(self):
        return self.stoken