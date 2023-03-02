# UOCIS322 - Project 5 #

## Name: Nathaniel Mason

## Contact Info: nmason@uoregon.edu

## Project Description:
The goal of this project is to create a web application based on RUSA's online calculator. The web app also contains two buttons that allow the user to submit and fetch brevet data from a MongoDB database. 
* The application is a worksheet on the web that allows the user to choose a distance and start date, and then after entering the distance value of a brevet controle, the opening and closing time of the controle will be displayed
* The algorithm is based on the algorithm from the RUSA website, which can be found at: https://rusa.org/pages/acp-brevet-control-times-calculator
* There are two buttons: Submit and Display, which allow the user to submit data to the database and to fetch the most recent data that was submitted

### To start the application, the user should use the following docker commands:
* "docker build -t myimage ." to build your image (you can also use "docker images" to list existing images and check that the creation was successful)
* "docker run -d -p 5001:5000 myimage" to create a running container and set the port that you will access on your browser (you can also use "docker ps" to view existing containers and check that your container is created and running)
#### Now that the docker container is created and running, you can access the application by going to your browser and entering localhost:5001 (5001 is the port you will use from the browser that was defined using the -p tag in the docker run command)

#### Once you are viewing the application on your browser, you can choose a brevet distance, start date, and enter some distances for difffernt controles that are on the brevet. Each time one of these controles is entered, an open time and close time will be displayed. You can enter a distance in miles or km, the algorithm will automatically convert back and forth between the two.