# toDoList

## Simple to-do list static page application using Django, AngularJS and Django Rest Framework

### Installation

First of all, clone the repo. Then, navigate inside 'toDoList' folder

```
cd toDoList
```

Assuming that you have `python-pip` and `virtualenvwrapper` installed on your system.
If not: for virtualenv see [here](https://virtualenv.pypa.io/en/latest/) and [here](https://pypi.python.org/pypi/virtualenvwrapper/).
For pip see [here](https://pip.pypa.io/en/stable/installing/).

Type the command:

```
mkvirtualenv myToDoList
```

and then, to installed the required packages, type:

```
pip install -r requirements.txt
```

...and fortunately in will install django and rest framework for you.

To migrate the database, type:

```
./manage.py makemigrations
./manage.py migrate
```

### Fill the database with some stuff

If you want to create your own superuser, type:

```
./manage.py createsupersuser
```

and enter your credentials.

To add some random data just to see how the application works, just execute the
following script:

```
python populate_database.py
```

This script fills your database with two users, with usernames 'test' and 'panospet'.
Each user has some tasks on his name. You can login with their cretentials (see next
step) and see their tasks.

### Run application

To run the application with the custom mini-server django provides, type:

```
./manage.py runserver
```

And then hit `localhost:8000` to your browser. You now see the login screen.
You can log in with the credentials of the superuser you created above, or, with
the credentials of the two test users. (test users have password `qwe123qwe`)

You can log out and log in with some different users, to see that each of them has
his own tasks. You can also create, update, delete tasks or mark them as completed.

Enjoy!

### Stop the application

If you want to stop the server simply type `Ctrl - C` in the terminal you started the
server before.

To exit the virtual environment, type:

```
deactivate
```

