# Collision and bike parking details
## Introduction
This project to get details of accident details in NY and try to coorelate impact of bike parking location on this accident, you can get front end of this prject [here](https://github.com/vihang16/collision-info-frontend)

## Technology
 - Python-3.9
 - Django-3.1.5
 - pandas-1.2.3
 - mysqlclient-2.0.3
 - django-cors-headers-3.7.0
 - sodapy-2.1.0
 - requests-2.25.1
 - Mysql-8.0
 - Docker-20.10.5

## Brief overview
There total 3 modules in this part
1. Get accident details from open source api
2. Get bike parking details from AWS location
3. store the data and render it on UI

This project divided into 2 apps
 - collision_data
 - bike_parking_info

Currently this module loads on demand based on the api calls


## Apps
  1.collision_data:<br/>This app respnsible for getting accident data for different cities and store into mysql table and retrieve it on api calls<br/>
    **Models (db tables)**<br/>
    *City*:: This contains list of city to fetch collsion data ( currently NY )<br/>
    *CollisionDetails*: it iterate over list of cities and gets data accident occured in that city and performs upsert query<br/>
  2. bike_parking_info:<br/>This app responsible for storing and retriving bike start and end location details<br/>
    **Models (db tables)** <br/>
    *BikeParkingInfo* : this Model is responsible for storing bike start/end info ( location name, coordinates etc)
     

## Rest API endpoints
 API call | Use
 | :--| :-- |
 getAllData | Iters all the city store in city table and fetch accident details of that city
 getBorough/<str:borough> | Fetches data only for that borough from socarata/soda api
 getBoroughFromDb/<str:borough>/<int:city_id> | Fetches data only for given borugh and given city from database (useful when we have multiple cities)
 getCollisionDetailsFromDb | Get all accident details where cyclist was injured or killed
 getBikeParkingInfo | Get last one year bike parking location details from server and store it into mysql db
 getBikeParkingDetailsFromDb | Get all bike parking location from mysql db
 
 ## How to use the project
 1. Install Docker
 2. Use git clone  https://github.com/vihang16/collision-details-backend.git
 3. Open docker-compose.yaml file and edit frontend service location context to your Dockerfile of [frontend code](https://github.com/vihang16/collision-info-frontend) or you can remove that service to run front end independently 
 4. Open powershell (windows) go to the path of docker-compose file
 5. run docker-componse build
 6. run **docker-compose run web python manage.py migrate**, this will create all tables we need for this application
 7. run **docker-compose up db**  this will initialize and run mysql container
 8. connect to db using mysql work bench/CLI with port 3302, host: localhost, protocol- TCP ( as it is running from docker) password- 12345678 user-root
 9. check if user  **creditshelf_user** has all privilages using this query **select * from mysql.user;**, if not you can give all the privilages by below query  <br/> **GRANT ALL PRIVILEGES ON *.* TO 'creditshelf_user'@'%';**
 10. now run command **ALTER USER 'creditshelf_user'@'%' IDENTIFIED WITH sql_native_password BY '12345678';** to change authentication method for creditshelf_user ( as after mysql 8.0 version default auth engine change to  **caching_sha2_password** 
 11. create one db entry for table **City** for New York ( as we are fetching data only for it ) with below query <br/> **INSERT INTO `motor_vehicle_collision`.`collision_data_city`
(
`city_name`,
`city_url`,
`city_link_for_soda`,
`shortener_name_soda_link`)
VALUES
(
'New York',
'https://data.cityofnewyork.us/resource/h9gi-nx95.json',
'data.cityofnewyork.us',
'h9gi-nx95');**
 12. now you can stop running db with pressing CTRL+C
 13. run **docker-compose up**
 14. if you are seeing error like this ![image](https://user-images.githubusercontent.com/17112329/111816783-41655800-8903-11eb-8d4e-46c2f0888886.png) <br/> shutdown docker-compose as docker may have run it in race-condition
 15. run separetely all the services with below command <br/> docker-compose up db once it is done <br/> docker-compose up web and in last <br/> docker-compose up frontend
 16. once all containers are running we need to load data in our db, we can do that by running below curl/Postman commands <br/> http://127.0.0.1:5000/getAllData (note: port of web django app is 5000) <br/> http://127.0.0.1:5000/getBikeParkingInfo
 17. once data is loaded go to browser and open localhost:4000  you should see something like this after sometime <br/> ![image](https://user-images.githubusercontent.com/17112329/111817752-6908f000-8904-11eb-999a-29c374961785.png)


## Future course of action
1. Ceate crown job for **getAllData** api to update data on daily/weekly basis
2. Create crown job **getBikeParkingInfo** on monthly basis
3. Expose api like **getBorough/<str:borough>**, **getBoroughFromDb/<str:borough>/<int:city_id>** from UI to get more granular data to User.
 
 
  



