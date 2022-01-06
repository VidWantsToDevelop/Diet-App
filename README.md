# Diet-App

**Description of the project**:
As you can see, my project has been called "DietApp" and there are no specific reasons for creating exactly this type of project, the reason is just that I always really wanted to create some kind of dynamic application, which will interact with the user and help him in some cases.
a)This app allows users to monitor their statistics of the calories they have consumed and burnt (with the sports activity).To this end, if the user wants the application to collect his/her statistics, he/she will be asked to fill the "Update" form each day, after completing, at least, one form the user will be able to look at his/her statistics of this day (there are also some additional features - charts and graphs, they contain data from the database, which display user's DAILY fats/carbohydrates/proteins ratio and the most important chart - WEEKLY CONSUMPTION, this function will not be activated until the moment of the user has been filling the daily form for the period of a week. After each Sunday user will get a graphical display of his/her calories intake and spending, this information will be displayed on the period of the whole month and deleted at the start of the next month).
b)The second function of this application - is the ability of users to choose one of the given types of diets and receive some advice upon these diets on their profile page (information in the advice section has been written only as of the example, I am not a nutritionist to give such advice :) ). At the moment, the "Plans" page consists of 6 randomly found diet plans from the internet, each of the given plan can be viewed by clicking on the Title of the diet and the user will be provided with some basic introduction for this diet and important pros/cons of the chosen diet. After selecting any plan user will start receiving advice on his/her "My Profile" page.


**Distinctiveness and Complexity**:
First of all, I would like to say that, in this project, I have used some of the new features. Here are some of them: 
a)Chart.js: Quite interesting JavaScript library which allowed me to implement any kinds of charts and graphs into my project.
b)Responsive design: That was a really interesting experience of setting up a CSS file for different kinds of screens, that made my project more flexible and reliable.
c)And my favorite one - Bootstrap: This framework made my life much easier, with the help of bootstrap I have established a lot of elements, for example: footer, navbar (which can even collapse, if you use it on mobile phones)
d)Also, I would like to mention - the usage of animations. Animations made my project look much smoother and easy on the eye.
e)This project contains a lot of JavaScript functions, that helped my project to look more dynamic (especially the usage of promises, which made it easier to work with the requests from the Fetch API). With the help of separated functions, it was much easier to save some space and use animation with any element I would like to.
f)For the proper work of bootstrap functions I have connected the jQuery library to this project.


**Project construction**:
My web application ( Capstone ) is a Django-based one, it consists of one model called DietApp. The only instruments I have been using in this project are: Django's features for the work with databases and other back-end stuff; JavaScript (including some additional JavaScript libraries like Chart.js); HTML as the front-end of the pages, CSS for a styling and mobile responsiveness purposes.


**How to run this project**:
I believe there are no pre-required files or libraries that must be downloaded. So, you just need to have python and Django framework been installed. I'm not really sure, but maybe the only thing you have to do before running the server is to make migrations from the database. You have to open the directory of the web application in your prompt, then write down these commands:

a)python manage.py makemigrations dietApp
b)python manage.py migrate
after these preparations, I believe you will be able to start this project by writing down
c)python manage.py runserver
!If you would like to get access to the superuser profile here are the login and password: login - admin; password - 322
