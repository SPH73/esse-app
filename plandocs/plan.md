# Project Planning

## Boilerplate

1. Install django and psycopg2-binary
2. Create Dockerfile
3. Create docker-compose.yml to automate commands and persist database data using volumes
4. Create accounts app
5. Add to installed apps in settings (register)
6. Specify Database
7. Create CustomUser model
8. Initialise database
9. Create CustomUserForms
10. Register CustomUser and CustomUserAdmin
11. Create Superuser
12. Install environs package with django support
13. Move sensitive variables to docker-compose and include in .gitignore
14. Save to remote repo
15. Write unit tests for user and superuser creation
16. Install coverage and run (add to .gitignore)
17. Create Pages App for static pages
18. Create templates directory add path to settings TEMPLATES....'DIRS'
19. create \_base template
20. create index template
21. add authentication

## build up site with features

1. create memberships app
2. Create UserMemberships
3. Create Subscriptions
4. Create Share app
5. Create Profile
6. develop api
7. plan next stage of implementing cloudinary

## generic process

create app  
register in installed apps  
add url maps  
create app urls.py  
run migrations  
create models  
run migrations again and for every addition or change  
register models on admin  
configure list views  
create app views  
test all new added funtionality with unit tests using coverage.py
