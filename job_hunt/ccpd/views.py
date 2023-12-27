from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from ccpd.forms import *
from django.contrib.auth.models import User
from pyresparser import ResumeParser
import en_core_web_sm
import json
import requests
import requests
from bs4 import BeautifulSoup
from ccpd.codeprofiles import code,skills
from django.contrib.auth import authenticate, login
# from ccpd.whatsapp import whatt



class Signup(CreateView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class Login(CreateView):
    form_class = UserCreateForm
    template_name = 'login.html'
    success_url = reverse_lazy('info')
    
# def register(request):
#     msg = None
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             msg = 'user created'
#             return redirect('login_view')
#         else:
#             msg = 'form is not valid'
#     else:
#         form = SignUpForm()
#     return render(request,'signup.html', {'form': form, 'msg': msg})


# def login_view(request):
#     form = LoginForm(request.POST or None)
#     msg = None
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_admin:
#                 login(request, user)
#                 return redirect('info')
#             elif user is not None and user.is_customer:
#                 login(request, user)
#                 return redirect('info')
#             elif user is not None and user.is_employee:
#                 login(request, user)
#                 return redirect('index')
#             else:
#                 msg= 'invalid credentials'
#         else:
#             msg = 'error validating form'
#     return render(request, 'login.html', {'form': form, 'msg': msg})




def info(request):
    if request.method=='POST':
        form=addinfoform(request.POST,request.FILES)
        # print(form)
        
        if form.is_valid():
            info=form.save(commit=False)
            print(info)
            info.user=request.user
            info.save()
            return redirect('index')
    else:
        form=addinfoform()
    context={
        'form':form 
        }    
    return render(request,'info.html',context)    
        
        
def index(request):
    info=addinfo.objects.get(user=request.user)
    context={
        'info':info
    }
    return render(request,'index.html',context)

def oncamp(request):
    # url = "https://www.xpiria.in/placement"
    # response = requests.get(url)
    pass
    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    # return render()
def anns(request):
    announs=compann.objects.all()
    announs = [i for i in announs if not i.is_expired()]
    # print(announs)        
    if (request.method =='POST'):
        form = compannform(request.POST, request.FILES)
        print(form)
    
        if form.is_valid():
            info = form.save(commit=False)
            info.save()
            # message=f'''
            # {info.company_name}
            # Offer_type: {info.offer_type}
            # Eligible_branches: {info.eligible_branches}
            # Eligibility_criteria: {info.eligibility_criteria}
            # Job title: {info.Job_title}
            # Salary: {info.salary}
            # Deadline: {info.deadline}
            # Job_description:{info.jd}
            # '''
            # whatt('+916300471702',message)
            return redirect('anns')
    else:
        form = compannform()
    
    context = {
        'form': form,
        "anns":announs
    }
    return render(request, "ann.html", context)

            
def apply(request,pk):
    form=applyform(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            info=form.save(commit=False)
            info.user=request.user
            pinfo=addinfo.objects.get(user=request.user)
            info.usern=pinfo.res_id
            comp=compann.objects.get(pk=pk)
            info.company=comp
            info.save()
            return redirect('index')
        else:
          form=applyform()
    context={
        'form':form 
        }    
    return render(request,'apply.html',context)
    
    

def profs(request,pk):
    info=addinfo.objects.get(pk=pk)
    file=info.file
    file=str(file)
    file="media/"+file
    eskills=skills(file)
    pinfo=dict()
    pinfo["first_name"]=info.user.first_name
    pinfo["email"]=info.user.first_name
    
    user1=info.leetcode_username
    user2=info.codechef_username
    user3=info.codeforces_username
    user4=info.gfg_username
    user5=info.github_username
    # print(user1)
    # print(user2)
    # print(user3)
    # print(user4)
    # print(user5)
    data=code(user1,user2,user3,user4,user5)
    # print(data)
    context={
        "data":data,
        "pinfo":pinfo,
        "info":info,
        "skills":eskills
    }
    return render(request,"profiles.html",context)
    
def stul(request,pk):
    comp=compann.objects.get(ann_id=pk)
    data=comapply.objects.filter(company=comp)
    print(data)    
    context={
        "data":data
    }
    return render(request,"stulist.html",context)
    
    
    
def offc(request):
    info=addinfo.objects.get(user=request.user)
    file=info.file
    file=str(file)
    file="media/"+file
    data = ResumeParser(file).get_extracted_data()
    known_skills = [
    "Python",
    "Java",
    "JavaScript",
    "C++",
    "C#",
    "Ruby",
    "PHP",
    "Swift",
    "Kotlin",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "NodeJS",
    "ExpressJS",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Redis",
    "Django",
    "Flask",
    "Ruby on Rails",
    "Spring Boot",
    ".NET Core",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Scikit-Learn",
    "Natural Language Processing",
    "NLP",
    "Computer Vision",
    "Reinforcement Learning",
    "Deep Learning",
    "Machine Learning Algorithms",
    "Data Engineering",
    "Big Data Analytics",
    "Data Warehousing",
    "ETL (Extract, Transform, Load)",
    "AWS",
    "Azure",
    "Google Cloud",
    "Kubernetes",
    "Docker",
    "Jenkins",
    "Ansible",
    "Terraform",
    "React",
    "Vue.js",
    "Redux",
    "VueX",
    "HTML5",
    "CSS3",
    "Responsive Web Design",
    "Kotlin",
    "Java",
    "iOS",
    "Swift"
    "Selenium",
    "JUnit",
    "TestNG",
    "Linux",
    "Unix",
    "Windows",
    "Tableau",
    "Power BI",
    "Matplotlib",
    "Seaborn",
    "Data Analytics",
    "Business Intelligence",
    "Communication",
    "Problem Solving",
    "Teamwork",
    "Leadership",
    "Adaptability",
    "AutoCAD",
    "SolidWorks",
    "CATIA",
    "MATLAB",
    "ANSYS",
    "Thermodynamics",
    "Fluid Mechanics",
    "Mechanical Design",
    "Finite Element Analysis",
    "CAD",
    "CAM",
    "Heat Transfer",
    "Manufacturing Processes",
    "Machine Design",
    "Structural Analysis",
    "Control Systems",
    "Robotics",
    "Materials Science",
    "Mechatronics",
    "HVAC",
    "CNC Machining",
    "Welding",
    "Machining",
    "Product Design",
    "MERN"
]
    import PyPDF2
    import spacy
    import pandas as pd

    nlp = spacy.load("en_core_web_sm")
    a=PyPDF2.PdfReader(file)
    dat=a.pages[0].extract_text()
    doc = nlp(dat)
    extracted_main = []
    
    for token in doc:
     if token.text in known_skills:
         extracted_main.append(token.text)
    extracted_main=set(extracted_main)
    extracted_main=list(extracted_main)    
    # print(data['skills'])
    # print(data)
    role=info.designation
    city=info.work_place
    deg=info.job_role
    country="India"
    print(role,city,deg)
    import requests

    url = "https://jsearch.p.rapidapi.com/search"

    querystring = {"query":"{} in {}, {}".format(role,city,country),"page":"1","num_pages":"10","employment_types":"{}".format(deg)}
    # get your own api key from rapid api
    # API_KEY=""
    
    headers = {
        "X-RapidAPI-Key":"a312d09bf1msh733c7a2bdd51d33p1e0d88jsn7dd4057091d7",
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    job_data=response.json()['data']
    print(response)
    # print(job_data)
    skillmat={}
    for i in range(0,len(response.json()['data'])):
        skillmat[i]=response.json()['data'][i]['job_description']
        
    import spacy
    import pandas as pd

    nlp = spacy.load("en_core_web_sm")

    for i in range(0,len(skillmat)):   
        doc = nlp(skillmat[i])
        extracted_skills=[]

        for token in doc:
         if token.text in known_skills:
            extracted_skills.append(token.text)
        skillmat[i]=extracted_skills
        import pandas as pd
        job_desc=[]
        for i in range(0,len(skillmat)):
            job_desc.append(skillmat[i])
        job_desc 
        index=[]
        for i in range(0,len(skillmat)):
            index.append(i)
        dictionar={
            'index':index,
            'job_desc':job_desc
        }
        df=pd.DataFrame.from_dict(dictionar)
       
        new_row={
            'index':[len(df)],
            'job_desc':[extracted_main]
        }
        new_row=pd.DataFrame.from_dict(new_row)
        df=pd.concat([df,new_row], ignore_index=True)
        df['job_desc'] = [' '.join(desc) for desc in df['job_desc']]
        from sklearn.feature_extraction.text import CountVectorizer
        cv=CountVectorizer(max_features=100,stop_words='english')
        import pandas as pd 
        vec=cv.fit_transform(df['job_desc'])
        from sklearn.metrics.pairwise import cosine_similarity
        similarity=cosine_similarity(vec)
        def recommend():
            distances=similarity[len(df)-1]
            job_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])
            print(job_list)
            a=job_list
            final_list=[]
            for i in job_list:
                final_list.append(df.iloc[i[0]]['index'])
            last=[] 
            final_list=final_list[1:len(final_list)]   
            for i in final_list:
                last.append(job_data[i])
                     
            return last    
        final_list=recommend() 
        distances=similarity[len(df)-1]
        job_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])
        job_list=job_list[1:len(job_list)]
        # print(type(job_list[2][1]))
        per=[]
        for i in range(0,len(job_list)):
             per.append(float(job_list[i][1]))
        
        # per = [np.fabs(per[1]) for i in per]  
        for i in range(0,len(per)):
               if(per[i]== 0.0):
                   per[i]="No particular skills required"
            
           
        print(per)        
        # print(context)
        # print(final_list)
        print("hello")
        final_list = zip(final_list, per)
        context={
            'last':final_list
            
            
        }   
    return render(request,'offc.html',context)


