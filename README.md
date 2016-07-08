# toDoList

## Simple to-do list static page application using Django, AngularJS and Django Rest Framework

### Installation

First of all, clone the repo. Then, navigate inside 'toDoList' folder
	cd toDoList

Assuming that you have python-pip and virtualenvwrapper installed on your system, just type
the command:
	mkvirtualenv myToDoList

and then, to installed the required packages, type:
	pip install -r requirements.txt

...and fortunately in will install django and rest framework for you.

To migrate the database, type:
	./manage.py makemigrations
	./manage.py migrate

Then, to run the application with the custom mini-server django provides, type:
	./manage.py runserver

And then hit 'localhost:8000' to your browser. You now see the login screen.

If you finished and want to exit the virtual environment, type:
	deactivate

Enjoy!