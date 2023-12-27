from requests_html import HTMLSession
import json
import requests
import requests
from bs4 import BeautifulSoup
import PyPDF2
import spacy
import pandas as pd
from pyresparser import ResumeParser
class UsernameError(Exception):
    pass
class PlatformError(Exception):
    pass
class User:
    def __init__(self,username=None,platform=None):
        self.__username = username
        self.__platform = platform
    def codechef(self):
        url = "https://codechef.com/users/{}".format(self.__username)
        session = HTMLSession()
        d= dict()
        r = session.get(url,timeout=10)
       
        # print(r)
        if r.status_code!=200:
            d["username"]="invalid username please enter correct details"
            d["global_rank"]="xxxx"
            d["country_rank"]="xxxx"
            d["rating"]="xxxx"
            return d
        try:
            rating_header = r.html.find(".rating-header",first=True)
        except:
            # raise UsernameError('User not found')
            d["username"]="invalid username please enter correct details"
            d["global_rank"]="xxxx"
            d["country_rank"]="xxxx"
            d["rating"]="xxxx"
            return d

        try:
            rating = rating_header.find(".rating-number",first=True).text
            d["rating"]=rating
        except:
            d["username"]="invalid username please enter correct details"
            d["global_rank"]="xxxx"
            d["country_rank"]="xxxx"
            d["rating"]="xxxx"
            return d
            # raise UsernameError('User not found')
        max_rating = rating_header.find('small')[0].text[1:-1].split()[2]
        rating_star = len(r.html.find(".rating-star",first=True).find('span'))
        ranks = r.html.find('.rating-ranks',first=True).find('strong')
        global_rank = ranks[0].text
        country_rank = ranks[1].text
        d['username']=self.__username
        d["global_rank"]=global_rank
        d["country_rank"]=country_rank
        return d
       
      
                
    def codeforces(self):
        url = 'https://codeforces.com/api/user.info?handles={}'.format(self.__username)
        r = requests.get(url,timeout=10)
        d  = dict()   
        r_data = r.json()
        # print(r_data)
        if r_data['status'] != 'OK':
            d['username'] = "invalid username and please enter correct username"
            d['ranking'] = "xxxx"
            d['maxRating'] = "xxxx"
            return d
        else:
            d['username'] = self.__username
            if "rank" in r_data['result'][0]:
                d['ranking'] = r_data['result'][0]['rank']
            else:
                d["ranking"] = "No participation in contests"
            if "maxRating" in r_data['result'][0]:
                d['maxRating'] = r_data['result'][0]['maxRating']
            else:
                d["maxRating"] = "No participation in contests"
            return d
        return d

    def gfg(self):
        url = "https://auth.geeksforgeeks.org/user/{}/?utm_source=geeksforgeeks".format(self.__username)
        response = requests.get(url)
        d = dict()
        # print(response)
        if response.status_code!=200:
             d['username']="Please enter valid username and details"
             d['institute_rank']="xxxx"
             d['total_no_of_problems']="xxxx"
             d['coding_score']="xxxx"
             return d   
            
        if response.status_code == 200:
           soup = BeautifulSoup(response.text, 'html.parser')
        data = list()
        d['username']=self.__username 
        try:  
            d['institute_rank']=soup.select('.rankNum')[0].text
        except:
             d['username']="Please enter valid username and details"
             d['institute_rank']="xxxx"
             d['total_no_of_problems']="xxxx"
             d['coding_score']="xxxx"
             return d 
        d['total_no_of_problems']=soup.select('.score_card_value')[1].text
        d['coding_score']=soup.select('.score_card_value')[0].text
        # data.append(d)
        return d
           
           
        
        
        
    def leetcode(self):
        url="https://leetcode-stats-api.herokuapp.com/{}".format(self.__username)
        r = requests.get(url)
        d = dict()
        if r.status_code!=200:
             d['username']="Please enter valid username and details"
             d['totalSolved']="xxxx"
             d['ranking']="xxxx"
             d['acceptanceRate']="xxxx"
             return d
        r_data = r.json()
        d['username']=self.__username
        d['totalSolved']=r_data["totalSolved"]
        d['ranking']=r_data["ranking"]
        d['acceptanceRate']=r_data["acceptanceRate"]
        return d
    def github(self):
        url=" https://api.github.com/users/{}".format(self.__username)
        r=requests.get(url)
        if r.status_code !=200:
            li=["invalid username"]
            return li
        r_data = r.json()
        url1="https://api.github.com/users/{}/repos".format(self.__username)
        r1=requests.get(url1)
        if r1.status_code !=200:
            raise UsernameError('User not found')
        r1_data = r1.json()
        d=dict()
        
        dr=dict()
        d['username']=r_data["login"]
        d['public_repos']=r_data["public_repos"]
        l=len(r1_data)
        dali=[]
        for i in range(l):
            li=[]
            li.append(r1_data[i]["name"])
            li.append(r1_data[i]["html_url"])
            dali.append(li)
        return dali
        
        
       
        
    def get_info(self):
        if self.__platform=='codechef':
            return self.codechef()
        if self.__platform=='codeforces':
            return self.codeforces()
        if self.__platform =='leetcode':
            return self.leetcode()
        if self.__platform =='gfg':
            return self.gfg()
        if self.__platform =='github':
            return self.github()
        raise PlatformError('Platform not Found')
    


def skills(f_path):
    nlp = spacy.load("en_core_web_sm")
    a=PyPDF2.PdfReader(f_path)
    dat=a.pages[0].extract_text()
    doc = nlp(dat)
    extracted_main = []
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
    for token in doc:
     if token.text in known_skills:
         extracted_main.append(token.text)
    extracted_main=set(extracted_main)
    extracted_main=list(extracted_main)
    return extracted_main


        
        
    

user1="Aakash751"
user2="aakash2504"
user3="gopuaakash"
user4="gopuaakash751"
user5="lnarayana_46"

def code(user1,user2,user3,user4,user5):
   obj =  User(user1,"leetcode")
   obj1 = User(user2,"codechef")
   obj2 = User(user3,"codeforces")
   obj3 = User(user4,"gfg")
   obj4 = User(user5,"github")
   data1=dict()
   data1["obj"]=obj.get_info()
   data1["obj1"]=obj1.get_info()
   data1["obj2"]=obj2.get_info()
   data1["obj3"]=obj3.get_info()
   data1["obj4"]=obj4.get_info()
#    print(data1)
   return data1
# code(user1,user2,user3,user4,user5)
    
    
 