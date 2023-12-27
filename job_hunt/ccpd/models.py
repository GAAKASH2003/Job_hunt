from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz
from datetime import timedelta

# Create your models here.

indian_cities = [
    ('Kochi', 'Kochi'),
    ('Bhubaneswar', 'Bhubaneswar'),
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Chennai', 'Chennai'),
    ('Delhi', 'Delhi'),
    ('Kolkata', 'Kolkata'),
    ('Jaipur', 'Jaipur'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Hyderabad', 'Hyderabad'),
    ('Bangalore', 'Bangalore'),
    ('Noida', 'Noida'),
    ('Gurgaon', 'Gurgaon'),
    ('Nagpur', 'Nagpur'),
    ('Lucknow', 'Lucknow')
]
job_titles = [
    ('Analyst', 'Analyst'),
    ('Assistant Manager Supply Chain', 'Assistant Manager Supply Chain'),
    ('Associate Analyst', 'Associate Analyst'),
    ('Associate Software Engineer', 'Associate Software Engineer'),
    ('AUT - Assistant Under Training', 'AUT - Assistant Under Training'),
    ('Business Analyst', 'Business Analyst'),
    ('Business Development Manager', 'Business Development Manager'),
    ('Consultant', 'Consultant'),
    ('Developer Associate', 'Developer Associate'),
    ('Engineer Trainee', 'Engineer Trainee'),
    ('Field Engineer', 'Field Engineer'),
    ('Financial Analyst', 'Financial Analyst'),
    ('Graduate Engineer Trainee (Get)', 'Graduate Engineer Trainee (Get)'),
    ('Graduate Trainee', 'Graduate Trainee'),
    ('Internship Trainee', 'Internship Trainee'),
    ('Java Developer', 'Java Developer'),
    ('Management Trainee', 'Management Trainee'),
    ('Managing Director', 'Managing Director'),
    ('Post Graduate Engineer Trainee', 'Post Graduate Engineer Trainee'),
    ('Mechanical Engineer', 'Mechanical Engineer'),
    ('Software Developer', 'Software Developer'),
    ('System Engineer', 'System Engineer'),
    ('System Engineer Hardware', 'System Engineer Hardware'),
    ('Technical Lead', 'Technical Lead'),
    ('Project Engineer', 'Project Engineer'),
    ('R&D Engineer', 'R&D Engineer'),
    ('Sde1', 'Sde1'),
    ('Software Analyst', 'Software Analyst'),
    ('Trainee Decision Scientist', 'Trainee Decision Scientist')
]

role=[
    ('INTERN','INTERN'),
    ('FULLTIME','FULLTIME')
]
degrees=[
    ('Btech','Btech'),
    ('MCA','MCA'),
    ('Mtech','Mtech')
]
branches = [
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('EEE','EEE'),
    ('Mechanical','Mechanical'),
    ('Chemical','Chemical'),
    ('Civil', 'Civil'),
    ('Metallurgy','Metallurgy'),
    ('Biotechnology','Biotechnology'),
]





        

class addinfo(models.Model):
    res_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.FileField(upload_to='resumes/',default="",blank=True)
    phone=models.CharField(max_length=11)
    work_place = models.CharField(max_length=33,choices=indian_cities,default="")
    designation= models.CharField(max_length=33,choices=job_titles,default="")
    job_role=models.CharField(max_length=33,choices=role,default="")
    codechef_username=models.CharField(max_length=30,blank=True,null=True,default="")
    leetcode_username=models.CharField(max_length=30,blank=True,null=True,default="")
    gfg_username=models.CharField(max_length=30,blank=True,null=True,default="")
    codeforces_username=models.CharField(max_length=30,blank=True,null=True,default="")
    github_username=models.CharField(max_length=30,blank=True,null=True,default="")


    
class profile(models.Model):
    prof_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    info=models.OneToOneField(addinfo,on_delete=models.CASCADE)
    

    
class compann(models.Model):
    ann_id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=30)
    offer_type=models.CharField(max_length=30)
    eligible_branches=models.CharField(max_length=20)
    eligibility_criteria=models.CharField(max_length=20)
    Job_title=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    deadline=models.DateTimeField()
    jd=models.URLField(max_length=200, blank=True, null=True)
    def is_expired(self):
        current_time = timezone.now()+timedelta(hours=5, minutes=30)
        return current_time > self.deadline




class comapply(models.Model):
    apply_id=models.AutoField(primary_key=True)
    company=models.ForeignKey(compann,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    usern=models.CharField(max_length=30,default="")
    name=models.CharField(max_length=20)
    Degree=models.CharField(max_length=20,choices=degrees,default="")
    Branch=models.CharField(max_length=20,choices=branches,default="")
    cgpa=models.FloatField()
    email=models.EmailField()
    roll_no=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=10)
    file=models.FileField(upload_to='resumes/',default="",blank=True)
        
        

    
    
    
    
    
    
    
    
    
    
    
    
        
     
     
     
    
        
    
    