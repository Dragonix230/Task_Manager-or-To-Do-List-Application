# Task_Manager-or-To-Do-List-Application
Project Report: To-D0 List OR Task Manager Application

1. Introduction
The Django Task Manager is a web-based application that allows users to manage their tasks effectively. Users can create, update, delete, and view tasks, with added features for user authentication (login and registration). The system is designed to be simple, responsive, and user-friendly, with a clean UI using baby pink and black colors.

The application was built using Django as the backend framework and SQLite for persistent storage. It includes Docker for containerization, making it easy to deploy the application to the cloud.

2. Objective
The primary goal of the Task Manager application is to provide a platform where users can manage their tasks efficiently. The key features include:
- **Task Management**: Create, update, delete, and view tasks.
- **User Authentication**: Users can register and log in to manage their tasks.
- **Persistent Storage**: Tasks are stored in a database (SQLite) for future access.
- **Simple and Intuitive UI**: The frontend is designed with minimal complexity and uses a consistent baby pink and black color scheme.
- **Dockerization**: Containerization of the application for easy cloud deployment.

---

3. Technologies Used

### 3.1 **Backend**
- **Python**: The programming language used to build the backend logic.
- **Django**: The web framework used for building the application’s backend, handling requests, routing, and ORM (Object Relational Mapping) with SQLite.
- **SQLite**: A lightweight relational database used for storing user data and tasks.

### 3.2 **Frontend**
- **HTML/CSS**: Used for structuring and styling the web pages. The CSS is embedded in the HTML to keep the project structure simple, following the chosen color scheme.
- **JavaScript**: Used minimally to add interactivity to the frontend where necessary (e.g., handling form submissions).

### 3.3 **Containerization**
- **Docker**: Used for containerizing the application, enabling easy deployment and running of the application in different environments (e.g., cloud services like AWS, GCP, etc.).

---

 4. Features and Functionalities

### 4.1 **User Authentication**
- **Login/Signup**: Users can create an account and log in to manage their tasks. Django's built-in authentication system handles password hashing and session management.
- **Logout**: Users can log out securely, ensuring no unauthorized access to their data.

### 4.2 **Task Management**
- **Create Tasks**: Users can create tasks by providing details such as the task name, description, and due date.
- **View Tasks**: Users can view a list of all their tasks. Tasks can be filtered based on their completion status (e.g., completed or pending).
- **Update Tasks**: Users can update task details, including marking tasks as completed or changing their due dates.
- **Delete Tasks**: Users can delete tasks they no longer need.

### 4.3 **Persistent Storage**
All tasks and user data are stored in an SQLite database, allowing users to access their tasks even after logging out and logging back in. Each user's tasks are stored separately, ensuring privacy and data security.

### 4.4 **Frontend Design**
The frontend is designed to be visually appealing and simple. The color scheme is a soft baby pink and black, with clear and easy-to-read fonts. The design is responsive, allowing users to access the task manager from different devices.

---

5. System Architecture

### 5.1 **Django Framework**
Django follows the **Model-View-Controller (MVC)** architectural pattern (though it’s called MTV in Django). Here’s how each component works:

- **Model**: Represents the database schema. The `Task` model defines the structure of the tasks stored in the database.
- **View**: The view contains the business logic. It handles user requests, interacts with the database, and returns the appropriate response (HTML pages).
- **Template**: Templates are used to render HTML. Django’s templating engine is used to dynamically render pages based on user data.

### 5.2 **Database Structure**
The database structure is simple, with a `User` model (provided by Django’s authentication system) and a `Task` model to store the task data. The `Task` model contains fields like:
- `name`: The name of the task.
- `description`: A detailed description of the task.
- `due_date`: The deadline for the task.
- `status`: Indicates whether the task is completed or pending.

---

 6. Implementation

### 6.1 **Project Structure**
```
taskmanager/
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_form.html
│   │       ├── signup.html
│   │       └── login.html
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── Dockerfile
├── requirements.txt
└── manage.py
```

### 6.2 **Key Code Snippets**

#### **Task Model (models.py)**
```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)  # False = Pending, True = Completed

    def __str__(self):
        return self.name
```

#### **Views for Task Management (views.py)**
```python
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    # Logic for task creation
    pass

@login_required
def task_update(request, task_id):
    # Logic for task update
    pass

@login_required
def task_delete(request, task_id):
    # Logic for task deletion
    pass
```

#### **Dockerfile**
```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

7. Testing

The project was tested both manually and automatically:
- **Unit Testing**: Django’s built-in test framework was used to test individual components (models, views, etc.).
- **Manual Testing**: The application was manually tested on a local machine to ensure all features (task management, user authentication, etc.) worked as expected.

---

 8. Dockerization and Deployment

The application was containerized using Docker to facilitate easy deployment across different environments. The steps involved:
- Writing a **Dockerfile** to define the container’s environment.
- Building and running the Docker image locally.
- The Docker image can be deployed to any cloud platform like AWS or Google Cloud for public access.

---

9. Future Enhancements

Some potential enhancements for this project include:
- **Task Prioritization**: Adding a priority level to tasks to help users better organize them.
- **Task Search**: Implementing a search functionality to quickly find tasks.
- **Notification System**: Sending notifications to users for upcoming deadlines.
- **Multi-User Collaboration**: Allowing multiple users to collaborate on tasks.

---


10. Conclusion

The Django Task Manager application successfully provides an easy-to-use interface for managing tasks. With Dockerization, the application is ready for deployment in any cloud environment, ensuring scalability and reliability.

