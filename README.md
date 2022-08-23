# MxAcademy

MxAcademy is an online distance learning platform using Django and MySql. Frontend HTML pages are integrated with Django Templates. 

## Environment Requirements:

- Django 2.2
- Python 3.7
- MySql 5.7
- other dependency see `requirements.txt`



## Client-Side Features:

- Basic:
  - Registration, User Center, Global Search
- Course
  - Course Management
  - Instructor Managment 
  - Organization Management
  - Video Contents 
  - Course Recommandation System
- User Operations
  - Comments
  - Subscription

#### Demo Pic:

course list page

<img src="https://raw.githubusercontent.com/hesihui/MxAcademy/main/demo_pic/course-page1.jpg"/>

course details page

<img src="https://raw.githubusercontent.com/hesihui/MxAcademy/main/demo_pic/course-page2.png"/>

course contents page

<img src="https://github.com/hesihui/MxAcademy/blob/main/demo_pic/course-page3.png"/>

organization page

<img src="https://raw.githubusercontent.com/hesihui/MxAcademy/main/demo_pic/org-page1.png"/>



## Admin-Side Features (customized with Django Admin):

- Course Management
- Authentication and Authority Management 
- Course Organization Management

Admin system 

<img src="https://raw.githubusercontent.com/hesihui/MxAcademy/main/demo_pic/management1.png"/>

<img src="https://raw.githubusercontent.com/hesihui/MxAcademy/main/demo_pic/management2.png"/>

## Configuration

setting.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "<db name>",
        'USER': "root",
        'PASSWORD': "<password>",
        'HOST': "127.0.0.1"
    }
}
```



##### Resource

Xadmin Documentation: https://github.com/sshwsfc/xadmin

VideoJs: https://videojs.com/
