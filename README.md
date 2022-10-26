https://user-images.githubusercontent.com/34107104/198111318-37e14a51-fa16-45bd-8fe1-c75e5056f59c.mp4
# web-portfolio-pro
#This is a web application that allow's authenticated users to add their locations
# <h3> Technologies </h3>
- Python Django 
- Bootstrap 
- postgreSQL 
- postgis 
- django-leaflet 

# <h3> Features </h3>
- User Registration Page 
- Login Page 
- User Profile Page 
- User Edit Profile Page 
- Home page with map with marked locations of users 
- logg activities for tracking user authentication

# <h3> Setup </h3>
1. Create a python enviroment locally 
2. Activate the enviroment 
3. Clone the project 
4. Install packages from requirments.txt file 
   - pip install -r requirments.txt 
5. Create your database usering postgreSQL 
6. Add the below 
  - Database Name 
  - Database password 
  - Database user 
7. Creating the below Extension for the database 
   - CREATE EXTENSION postgis; 
   - CREATE EXTENSION postgis_topology; 
8. Run migrations 
   - pthon manage.py makemigrations 
9. Migrate 
   - python manage.py migrate 
10. Run Server 
    - python manage.py runserver 


# <h3> How to Use the project </h3>
1. Create a User using the Register link in the navbar 
2. Login with the authenticated users 
3. Go to your profile page by clicking the profile link in the dropdown in the navbar 
4. Update your account by clicking the update button on your profile page 

# Note 
## for windows users if you are having problems with installing Grdal 
[Watch this youtube video ](https://www.youtube.com/watch?v=u7KRKYd5aBQ "Google's Homepage")
   
![WXWorkCapture_1666709378190](https://user-images.githubusercontent.com/34107104/197806837-503e50e8-f8ae-4319-a178-66c4dc8d8f20.png)
![WXWorkCapture_16667092009477](https://user-images.githubusercontent.com/34107104/197806859-39e7db27-02e4-4413-8cb4-daecdffdd4e4.png)
