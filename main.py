import mysql.connector
from config import host,user,password
import random
db=mysql.connector.connect(
    user=user,
    password=password,
    host=host,
    db="exotic_fruits"
    )

names=["Karen","Vardan","Simon","Sargis","Mesrop","Narek","Artur","Araqel","Armen","Tigran","Davit","Harutyun","Hakob","Arman","Karlen","Lazar","Gurgen","Zarmik","Ararat","Zaven","Vardges","Vahag","Artak","Vahram"]
last_names=["Simonyan","Vardanyan","Kirakosyan","Shahmuradyan","Petrosyan","Pashikyan","Veranyan","Hayrapetyan","Asatryan","Mkrtchyan","Kostanyan","Karayan","Tankyan","Muradyan","Sahakyan","Sayadyan","Ghazaryan"]
cars=['BMW','Mercedes','Gaz','LADA','Opel']
condition=['New','Good','Bad']

car_model=['1997','1998','2000','2004','1989','2005','2012','2009','2011','2013','2003','1979','1999']
city=['yerevan','gyumri','vanadzor','sisian','kapan','stepanakert','gavar','tashir','hoktemberian','eghegnadzor']
comments=['5','4.5','4','3.5','3','2.5','2','1.5','1']

fruits=['apple','avocado','banana','cherry','kiwi','mango','orange','pineapple','stawberries','watermelon']
country=['india','tailand','china','spain','greece','hawaii','mozambique','brazil','mexico','italy']
status=['done','in process','not started']
salary=['400','460','520','380','500']

mycursor=db.cursor()
#mycursor.execute("CREATE DATABASE exotic_fruits")
#mycursor.execute("CREATE TABLE Customer (customer_id int PRIMARY KEY AUTO_INCREMENT,first_name VARCHAR(50),last_name VARCHAR(50),city ENUM('yerevan','gyumri','vanadzor','sisian','kapan','stepanakert','gavar','tashir','hoktemberian','eghegnadzor'),phone int UNSIGNED)")
#mycursor.execute("CREATE TABLE Fruit(fruit_id int PRIMARY KEY AUTO_INCREMENT,name ENUM('apple','avocado','banana','cherry','kiwi','mango','orange','pineapple','stawberries','watermelon'),improved_from ENUM('india','tailand','china','spain','greece','hawaii','mozambique','brazil'),picture VARCHAR(200))")
#mycursor.execute("CREATE TABLE bridge(order_id int PRIMARY KEY AUTO_INCREMENT ,cust_id int,FOREIGN KEY(cust_id) REFERENCES Customer(customer_id),fruit_id int,FOREIGN KEY(fruit_id) REFERENCES Fruit(fruit_id),status ENUM('done','in process','not started'))")
#mycursor.execute("CREATE TABLE cars(car_id int PRIMARY KEY AUTO_INCREMENT,car_brand ENUM('BMW','Mercedes','Gaz','LADA','Opel'),car_year int UNSIGNED,car_condition ENUM('New','Good','Bad') )")
#mycursor.execute("CREATE TABLE drivers(driver_id int PRIMARY KEY AUTO_INCREMENT,first_name VARCHAR(50),last_name VARCHAR(50),age int UNSIGNED,carid int,FOREIGN KEY(carid) REFERENCES cars(car_id),salary int UNSIGNED )")
#mycursor.execute("CREATE TABLE delivery_status (delivery_id int PRIMARY KEY AUTO_INCREMENT,orderid int,FOREIGN KEY(orderid) REFERENCES bridge(order_id),driverid int,FOREIGN KEY(driverid) REFERENCES drivers(driver_id),delivery_time int UNSIGNED)")
#mycursor.execute("CREATE TABLE customer_last_ratings (rating_id int PRIMARY KEY AUTO_INCREMENT,customerid int,FOREIGN KEY(customerid) REFERENCES Customer(customer_id),Fruit ENUM('apple','avocado','banana','cherry','kiwi','mango','orange','pineapple','stawberries','watermelon'),rating ENUM('5','4.5','4','3.5','3','2.5','2','1.5','1') )")


#for x in range(6):
#    c=random.sample(cars,1)
 #   cc=random.sample(car_model,1)
 #   cm=random.sample(condition,1)
  #  mycursor.execute("INSERT INTO cars (car_brand,car_year,car_condition) VALUES (%s,%s,%s)",(c[0],cc[0],cm[0]))
 #   db.commit()




#for x in range(10):
   # n=random.sample(names,1)
   # f=random.sample(last_names,1)
   # c=random.sample(city,1)
   # p = random.randint(100000000, 999999999)
   # mycursor.execute("INSERT INTO Customer (first_name,last_name,city,phone) VALUES (%s,%s,%s,%s)", (n[0], f[0], c[0],p))
   # db.commit()

#for x in range(10):
   # n =random.sample(names,1)
   # f= random.sample(last_names,1)
   # a= random.randint(18,60)
  #  s = random.sample(salary, 1)
  #  c= random.randint(1,5)
   # print(c,type(c))
   # mycursor.execute("INSERT INTO drivers (first_name,last_name,age,carid,salary) VALUES (%s,%s,%s,%s,%s)", (n[0],f[0],a,c,int(s[0])))
  #  db.commit()

#link='C:\\Users\\Narek\\Desktop\\Bigdata\\dataset1\\dtrain\\watermelon'
#mycursor.execute("INSERT INTO Fruit (fruit_name,imported_from,picture) VALUES (%s,%s,%s)", (fruits[9],country[9],link))
#db.commit()


#for x in range(15):
   # k=random.randint(1,10)
   # c=random.randint(1,10)
   # s =random.sample(status,1)
   # mycursor.execute("INSERT INTO bridge (cust_id,fruit_id,status) VALUES (%s,%s,%s)", (k,c,s[0]))
  #  db.commit()

#for x in range(20):
   # k=random.randint(1,10)
   # c=random.sample(fruits,1)
    #s=random.sample(comments,1)
   # print(s)
   # mycursor.execute("INSERT INTO customer_last_ratings (customerid,Fruit,rating) VALUES (%s,%s,%s)", (k,c[0],s[0]))
   # db.commit()



#mycursor.execute("ALTER TABLE Fruit CHANGE name fruit_name ENUM('apple','avocado','banana','cherry','kiwi','mango','orange','pineapple','stawberries','watermelon')")
#mycursor.execute("ALTER TABLE Fruit CHANGE improved_from imported_from ENUM('india','tailand','china','spain','greece','hawaii','mozambique','brazil','mexico','italy')")

#mycursor.execute("DROP TABLE customer_last_ratings ")
mycursor.execute("SHOW TABLES")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("SELECT * FROM bridge ")
#mycursor.execute("SELECT * FROM cars ")
#mycursor.execute("SELECT * FROM Customer ")
#mycursor.execute("SELECT * FROM Fruit ")
#mycursor.execute("SELECT * FROM delivery_status")
#mycursor.execute("SELECT * FROM drivers ")
#mycursor.execute("SELECT * FROM customer_last_ratings ")
for x in mycursor:
   print(x)

#print("Welcome to exotic fruits delivery store \n 1 - Customer list \n 2 - Fruit list \n 3 - orders \n 4 - cars \n 5 - drivers, \n 6 - delivery_status, \n 0 - exit ")





