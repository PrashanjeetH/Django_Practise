# Django Practise
I posted all my Django practise code while going through the course from [edx](https://edx.org) and later exploring world of django on own. 

![](https://img.shields.io/badge/build-passed-green)  ![](https://img.shields.io/github/stars/PrashanjeetH/Django_Practise?style=flat)  ![](https://img.shields.io/badge/lisence-GNU-blue)
## Course Name :
[CS50's Web Development with Python and JavaScript | edx](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript)
## Instructor
[Brian Yu](https://www.edx.org/bio/brian-yu) and [David. J. Malan](https://www.edx.org/bio/david-j-malan)
     
## To Run any of the practise module run the below commands in the given sequence:
```python
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
Open your browser and goto 127.0.0.1:8000 where 8000 is the default port number django uses.

<details>
<summary>Repo Walkthrough</summary>
 
 - practise00 : Hello world in Django i.e rendering returning HTML response from views.
 - practise01 : Rendering returning HTML file from templates and using models/DB in Django.
 - practise02 : Renderin multiple HTML templtes and Linking them to each other.
 - practise03 : Intro to Django version of jinja2 i.e Django Template Language (DTL) and Loading Static files like css and js.
 - practise04 : Form in Django (Typical way).
 - practise05 : Form in Django (Django Forms Way).
 - practise06 : Handeling media files in Django.
 - practise07 : Introduction to Class Based View in Django.
 - practise08 : User Registration and individual content management.
 - practise09 : Social authentication integrated in project (google authentication) [Referred Blog](https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5)
 - practise10 : Sending mail using SMTP server ( HOST : gmail )
 - practise11 : Using Sessions for better experience.
</details>

*HAPPY CODING :)

__P.S. : Some modules may need some extra config. see settings.py file for reference.__
