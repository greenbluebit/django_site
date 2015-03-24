INSTRUCTIONS

Make a free account on Heroku

Open command line 

do 'heroku login'

do  'heroku git:clone -a freshertomatoes' to take the project from my running git repo on heroku or 'git clone https://github.com/GreenBlueBit/django_site.git' to get it from here.

do 'heroku create' 

do 'git push heroku master' 

do 'git run python manage.py migrate' 

If static files don't show, do 'heroku run python manage.py collectstatic' 

If you want, check logs via 'heroku logs --tail' Heroku – How to access the administration page of the application  


Go to 'http://freshertomatoes.herokuapp.com/fresh_tomatoes/' to see the content in use. 

Open 'http://freshertomatoes.herokuapp.com/admin/login/?next=/admin/' to get to the administration login page. 

Username: 'test' , Password: 'test' 

Here you can add/remove/edit/read any of the movies or shows 


For more information check my mini report pdf in this repo called reportReadme.pdf

