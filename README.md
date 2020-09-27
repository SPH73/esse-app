# PIXPI MEDIA

Our heart is in everything!

## Introduction

A platform for sharing memories, special occasions and events.

### Table of Contents

1. [UX](#ux)

   - [Goals](#goals)

     - [Project Goals](#project-goals)
     - [Target Audience](#target-audience)
     - [User Goals](#user-goals)
     - [Future Goals](#future-goals)

   - [User Stories](#user-stories)

     - [Visitor Stories](#visitor-stories)
     - [User Stories by Type](#user-stories-by-type)

   - [Design](#design)

     - [User Interface](#user-interface)
     - [Wireframes](#wireframes)
     - [Database Design](#database-design)
     - [Model Architecture](#model-architecture)

2. [Features](#features)

   - [Existing Features](#existing-features)
   - [Future Features](#future-features-to-implement)

3. [Technologies Used](#technologies-used)

   - [Languages](#languages)
   - [Frameworks/libraries](#frameworks/libraries)
   - [Database](#database)
   - [Development and Hosting Tools](#development/hosting)

4. [Testing](#testing)

5. [Deployment](#deployment)

   - [Local](#local-setup)
     - [Prerequisites](#prerequisites)
     - [Procedure](#procedure)
   - [Heroku](#deployment-on-heroku)
     - [Requirements](#requirements)

6. [Credits](#credits)

7. [Acknowledgements](#acknowledgements)

8. [Resources](#resources)

9. [Other Notes](#other-notes)
   - [Next Steps](#next-steps)
   - [Personal Takeways](#personal-takeawys)

## UX

### Project Goals

Create a project plan that outlines my project idea and the elements required to complete it.  
Learn additional material based on the above and develop a deeper understanding of the material already covered in the course.  
Understand the process of developing a Django app in a Docker container and then implement it.  
Develop an application that is easy to use and meets the needs of the target audience and one which is aesthetically pleasing and intuitive to all users/visitors.  
Purposefully implement a database design suitable for the application.  
Produce a project that fulfills the requirements of the Milestone project criteria.  
Produce a project that I am proud of.

### Target Audience

### User Goals

### Future Goals

### User Stories

#### Visitor Stories

#### User Stories by Type

## Features

### Existing Features

### Future Features to Implement

## Design

### UI

### Database Schema

### Model Architecture

## Technologies Used

### Languages

[Python 3.8](https://www.python.org/) A python image pulled from the Docker Hub was used inside a Docker container.

### Frameworks

[Django 3.1](https://www.djangoproject.com/) A high-level Python Web framework that encourages rapid development and clean, pragmatic design.  
[Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/)

### Libraries/Packages

[Psycopg2-binary](https://pypi.org/project/psycopg2-binary/) psycopg2 - Python-PostgreSQL Database Adapter (for development)  
[environs with django suppoort](https://pypi.org/project/environs/#usage-with-django) for separation and parsing of environment variables which installs [dj-database-url](https://pypi.org/project/dj-database-url/) as a dependency.  
[Django-Crispy-forms](https://pypi.org/project/django-crispy-forms/) prestyled bootstrap forms  
[Django-allauth](https://pypi.org/project/django-allauth/)

### Database

[Postgresql 12](https://www.postgresql.org/) Open source database used from conception to deployment as a container pulled from Docker Hub.

### Development/Hosting

[Visual Studio Code](https://code.visualstudio.com/) As with all my projects, VS Code is my preferred code editor.  
[autopep8 extension](https://marketplace.visualstudio.com/items?itemName=himanoa.Python-autopep8)  
[pipenv](https://pypi.org/project/pipenv/) Python recommended dependency manager.  
[Docker](www.docker.com) To containerize the app environment.  
[Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) to manage (view) the docker containers.  
[Git](https://git-scm.com/) For version control.  
[GitHub](https://github.com/) To store the repository and share the code remotely.  
[Heroku](https://www.heroku.com/) Cloud platform as a service to deploy the app.

## Testing

Coverage.py is being used to check the code being tested or more specifically to find missing tests or code/modules not included in addition to the django test module and TestCase and SimpleTestCase classes.

Thanks to Adam Johnson and this blog post [Getting a Django Application to 100% Coverage](https://adamj.eu/tech/2019/04/30/getting-a-django-application-to-100-percent-coverage/) I was able to resolve coverage reporting 98% to 100% by including the code in manage.py which is a workaround for a bug in the report. See screenshots here and refer to the credit code in manaage.py.

## Deployment

## Credits

Credit to [Zac Kwan](https://medium.com/@Zaccc123) and [this blog](https://medium.com/@Zaccc123/django-tests-with-nose-and-coverage-dff5d3633b4b) for the additional line of code in manage.py to generate a coverage html report.

## Acknowledgements

### Resources

[Django source code](https://github.com/django/django)  
[Django Docs](https://www.djangoproject.com/)  
[Django packages](https://djangopackages.org/)  
[Postgresql Docs](https://postgresapp.com/documentation/)

[Django REST framework](https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes)

[CustomUser](https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)  
[Django-allauth](https://readthedocs.org/projects/django-allauth/)  
[Allauth Social login - Google](https://django-allauth.readthedocs.io/en/latest/providers.html#google)

[Cloudinary Dashboard](https://cloudinary.com/console/)  
[Cloudinary Django SDK](https://cloudinary.com/documentation/django_image_and_video_upload)  
[Cloudinary Django Library](https://github.com/cloudinary/pycloudinary)  
[cloudinary-Heroku](https://devcenter.heroku.com/articles/cloudinary)

[Bootstrap Grid ref](https://getbootstrap.com/docs/4.5/layout/grid/)  
[Bootstrap Icons](https://icons.getbootstrap.com/)

[Django Tests](https://docs.djangoproject.com/en/3.1/topics/testing/)  
[Django SerializeMixin](https://docs.djangoproject.com/en/3.1/topics/testing/advanced/#testing-reusable-applications)  
[coverage.py docs](https://coverage.readthedocs.io/en/coverage-5.2.1/cmd.html)  
[Testing with Coverage](https://devguide.python.org/coverage/#using-coverage-py)  
[Adam Johnson Blog on coverage](https://adamj.eu/tech/2019/04/30/getting-a-django-application-to-100-percent-coverage/#:~:text=Code%20coverage%20is%20a%20simple,tool%20for%20measuring%20code%20coverage.)

[Learn Django Tutorials](https://learndjango.com/tutorials/)  
[UUID as Prinary ID](https://tech.serhatteker.com/post/2020-01/uuid-primary-key/#:~:text=In%20Django%20whenever%20we%20create,was%20added%20in%20Django%201.8%20.)

[ArrayField](https://docs.djangoproject.com/en/3.1/ref/contrib/postgres/fields/)

#### Next Steps
