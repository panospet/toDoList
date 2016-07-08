import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myToDoList.settings")

import django
django.setup()

from django.contrib.auth.models import User
from toDoList.models import Task


def populate():
    user = add_user('test', 'test1', 'testuser', 'test@test.net', 'qwe123qwe')
    add_task(user, 'first task', 'first task description', 'C', False)
    add_task(user, 'second task', 'second task description', 'C', False)
    add_task(user, 'third task', 'third task description', 'O', True)

    user2 = add_user('panos', 'pet', 'panospet', 'panos@panos.net', 'qwe123qwe')
    add_task(user2, 'Random1 task', 'This is task Random1!!!', 'A', False)
    add_task(user2, 'Random2 task', 'This is task Random2!!!', 'B', True)
    add_task(user2, 'Random3 task', 'This is task Random3!!!', 'C', False)


def add_user(first_name, last_name, username, email, password):
    """
    Function that adds a user without superuser permissions.
    """
    user = User.objects.get_or_create(
        first_name=first_name, last_name=last_name,
        username=username, email=email)[0]
    user.set_password(password)
    user.save()
    return user


def add_task(user, title, description, priority, is_completed):
    """
    Function that adds a task in the database.
    """
    task = Task.objects.get_or_create(user=user, title=title,
	description=description,  priority=priority, is_completed=is_completed)[0]
    task.save()
    return task


def print_db():
    """
    Just to know, print what is inside our database.
    """
    for user in User.objects.all():
        for task in user.task_set.all():
            print("User: {} -- Task: {}".format(user, task))


if __name__ == '__main__':
    print("Starting to populate DB...\n")
    populate()
    print_db()