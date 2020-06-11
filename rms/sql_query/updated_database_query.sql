CREATE SCHEMA `rms`;

-- =========================================================================

-- Admin Table
CREATE TABLE rmsFinalProject.admin(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    admin_name varchar(100) NOT NULL,
    password varchar(100) NOT NULL,
    roles varchar(100) not null,
    logged_in ENUM("yes", "no") DEFAULT "no" NOT NULL
);

-- Insert Query
INSERT INTO rmsFinalProject.admin(`admin_name`,`password`, roles) 
values("admin","admin", "Dashboard, Employees, Tables, Reservations, Category, Menu, Orders, Bill, Settings, Logout");

-- insert into admin(`admin_name`,`password`, roles) 
-- values("admin","admin", "Dashboard, Employees, Tables, Reservations, Category, Menu, Orders, Bill, Settings, Logout");



-- Update Query
-- UPDATE rmsFinalProject.admin SET logged_in = "yes" WHERE admin_name = "admin"

-- =========================================================================

-- Employee Table
CREATE TABLE `rmsFinalProject`.`employee`(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    employee_name varchar(100) NOT NULL,
    job_title varchar(100) NOT NULL,
    salary int NOT NULL,
    joining_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Insert Query
INSERT INTO `rmsFinalProject`.`employee` (`employee_name`, `job_title`,`salary`, `joining_date`) 
values ('zaka', 'waiter', 5000, '2020-04-1');

-- =========================================================================

-- Category Table / List the menu items

	-- Starters
	-- Non-Veg Items
	-- Veg Items
	-- Seafood Items
	-- Soft Drinks
	-- Beer/Liquors
	-- Dessert
	
CREATE TABLE `rmsFinalProject`.`category`(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    category_name varchar(100) NOT NULL
);

-- Insert Query
INSERT INTO `rmsFinalProject`.`category` (`category_name`) 
values 
 ('Starters'),
 ('Non-Veg Items'),
 ('Veg Items'),
 ('Seafood Items'),
 ('Soft Drinks'),
 ('Beer/Liquors'),
 ('Dessert');

-- =========================================================================

-- Menu/Food items to show/list to place an order
CREATE TABLE `rmsFinalProject`.`menu`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    food_name varchar(100) NOT NULL Primary key,
    price int NOT NULL,
    category_id int NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

-- Insert Query
INSERT INTO `rmsFinalProject`.`menu` (`food_name`, `price` ,`category_id`) 
values
 ('Chicken Nuggets', 10.00, 1),
 ('Pancakes', 10.00, 3),
 ('French Toast', 10.00, 3),
 ('Chicken Caeser Salad', 10.00, 2),
 ('Coke', 10.00, 5),
 ('Ice-Cream', 10.00, 7),
 ('Apple Crumble', 10.00, 7),
 ('Prawn Salad', 10.00, 4),
 ('Salmon Sandwich', 10.00, 4),
 ('Chicken Burger', 10.00, 2),
 ('Pulled Pork Sandwich', 10.00, 2),
 ('Fanta', 17.50, 5);

 
-- =========================================================================

-- Customer's Booking table
CREATE TABLE `rmsFinalProject`.`customerBooking`(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    customer_name varchar(100) NOT NULL,
    phone_number varchar(15) NOT NULL,
    booking_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
--     start_time timestamp NOT NULL default current_timestamp,
);

-- Select Query
select customer_name, phone_number, date(booking_date) as date, 
time_format(time(booking_date), '%H:%i') as time from customerBooking;

-- Insert Query
insert into `customerBooking` (`customer_name`, `phone_number`,  `booking_date`) 
values ('ali', '312000131', concat('2020-06-10', ' ', '13:30'));

-- =========================================================================

-- Tables table
CREATE TABLE `rmsFinalProject`.`tables`(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    table_number varchar(100) NOT NULL,
    covers int NOT NULL
);

-- Insert Query
INSERT INTO `rmsFinalProject`.`tables` (`table_number`,`covers`) 
values ('table1', 2);

-- =========================================================================

-- Order table
CREATE TABLE `rmsFinalProject`.`orders`(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    table_id int NOT NULL,
    food_list varchar(1000) not null,
    total_price varchar(100) not null,
    paid ENUM("yes", "no") DEFAULT "no" NOT NULL,
    FOREIGN KEY (table_id) REFERENCES `tables`(id)
);

-- CREATE TABLE `rmFinalProjects`.`orders`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     table_id int NOT NULL,
--     menu_id int NOT NULL,
--     quantity int NOT NULL,
--     FOREIGN KEY (table_id) REFERENCES `tables`(id),
--     FOREIGN KEY (menu_id) REFERENCES menu(id)
-- );

insert into orders (table_id, food_list, total_price)
values (2, "Burger, Pizza", "50")

-- Insert Query
-- INSERT INTO `rmsFinalProject`.`orders` (`quantity`, `order_id`,`product_id`) 
-- values (1,1,1);
-- INSERT INTO `rmsFinalProject`.`orders` (`quantity`, `order_id`,`product_id`) 
-- values (1,2,1);

-- =========================================================================

-- Restaurant Information table
CREATE TABLE `rest_info`(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    restaurant_name varchar(100) NOT NULL,
    address varchar(300) NOT NULL,
    contact varchar(300) NOT NULL
);

-- Insert Query
INSERT INTO `rmsFinalProject`.`rest_info`(`restaurant_name`, `address`, `contact`)
values("Food Fest", "Dublin", "0123456789");

-- =========================================================================

-- =========================================================================

-- Take care later
	-- JobTitle table  			- Create new
	-- user_privilege table		- Create new
	
	-- Product table
	-- Membership table
	
	-- Add Job Titles option

-- =========================================================================

-- =========================================================================
-- CREATE SCHEMA `rms` ;
-- CREATE TABLE `rms`.`employee`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL,
--     job_title varchar(100) NOT NULL,
--     salary int NOT NULL,
--     bonus int NOT NULL,
--     joining_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
-- );
-- INSERT INTO `rms`.`employee` (`name`, `job_title`,`salary` ,`bonus` ,`joining_date`) 
-- values ('zaka','waiter',5000,0,'2020-04-1');
-- INSERT INTO `rms`.`employee` (`name`, `job_title`,`salary` ,`bonus` ,`joining_date`) 
-- values ('talha','waiter',5000,0,'2020-01-1');
-- INSERT INTO `rms`.`employee` (`name`, `job_title`,`salary` ,`bonus` ,`joining_date`) 
-- values ('bilal','cook',10000,5,'2020-02-1');
-- 
-- 
-- 
-- CREATE TABLE `rms`.`category`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL
-- );
-- INSERT INTO `rms`.`category` (`name`) 
-- values ('bbq');
-- INSERT INTO `rms`.`category` (`name`) 
-- values ('continental');
-- INSERT INTO `rms`.`category` (`name`) 
-- values ('fast food');
-- 
-- 
-- 
-- CREATE TABLE `rms`.`product`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL,
--     quantity int NOT NULL,
--     price int NOT NULL,
--     selling_price int NOT NULL,
--     category_id int NOT NULL,
--     FOREIGN KEY (category_id) REFERENCES product(id)
-- );
-- INSERT INTO `rms`.`product` (`name`, `quantity`,`price` ,`selling_price` ,`category_id`) 
-- values ('tikka',100,100,200,1);
-- 
-- 
-- 
-- CREATE TABLE `rms`.`membership`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL,
--     off int NOT NULL
-- );
-- INSERT INTO `rms`.`membership` (`name`, `off`) 
-- values ('premium',20);
-- INSERT INTO `rms`.`membership` (`name`, `off`) 
-- values ('gold',10);
-- INSERT INTO `rms`.`membership` (`name`, `off`) 
-- values ('silver',5);
-- 
-- 
-- 
-- CREATE TABLE `rms`.`customer`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL,
--     phone_number varchar(15) NOT NULL,
--     membership_id int NOT NULL,
--     issue_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (membership_id) REFERENCES membership(id)
-- );
-- INSERT INTO `rms`.`customer` (`name`, `phone_number`,`membership_id` ,`issue_date`) 
-- values ('ali','312000131',1,'2020-02-1');
-- INSERT INTO `rms`.`customer` (`name`, `phone_number`,`membership_id` ,`issue_date`) 
-- values ('razi','333332313',1,'2020-01-24');
-- 
-- 
-- 
-- CREATE TABLE `rms`.`table`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     table_name varchar(100) NOT NULL,
--     no_of_seats int NOT NULL
-- );
-- INSERT INTO `rms`.`table` (`no_of_seats`,`table_name`) 
-- values (5,"table1");
-- INSERT INTO `rms`.`table` (`no_of_seats`,`table_name`) 
-- values (4,"table2");
-- INSERT INTO `rms`.`table` (`no_of_seats`,`table_name`) 
-- values (3,"table3");
-- 
-- 
-- 
-- 
-- CREATE TABLE `rms`.`reservation`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     table_id int NOT NULL,
--     customer_name varchar(100) NOT NULL,    
--     customer_phone_number varchar(100) NOT NULL,
--     start_time timestamp NOT NULL default current_timestamp,
--     end_time timestamp NOT NULL default current_timestamp,
--     FOREIGN KEY (table_id) REFERENCES `table`(id)
-- );
-- INSERT INTO `rms`.`reservation` (`table_id`,`customer_name`, `customer_phone_number`,`start_time` ,`end_time`) 
-- values (1,"tiwana",'333332313','2020-02-1 16:00:00','2020-02-1 18:00:00');
-- INSERT INTO `rms`.`reservation` (`table_id`,`customer_name`, `customer_phone_number`,`start_time` ,`end_time`) 
-- values (2,"malik",'334544313','2020-02-1 17:00:00','2020-02-1 19:00:00');
-- 
-- 
-- 
-- 
-- CREATE TABLE `rms`.`order`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     order_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     membership_id int,
--     FOREIGN KEY (membership_id) REFERENCES membership(id)
-- );
-- INSERT INTO `rms`.`order` (`order_date`, `membership_id`) 
-- values ('2020-02-1 19:00:00',1);
-- INSERT INTO `rms`.`order` (`order_date`, `membership_id`) 
-- values ('2020-02-1 18:00:00',null);
-- 
-- 
-- CREATE TABLE `rms`.`product_order`(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     quantity int NOT NULL,
--     order_id int NOT NULL,
--     product_id int NOT NULL,
--     FOREIGN KEY (order_id) REFERENCES `order`(id),
--     FOREIGN KEY (product_id) REFERENCES product(id)
-- );
-- INSERT INTO `rms`.`product_order` (`quantity`, `order_id`,`product_id`) 
-- values (1,1,1);
-- INSERT INTO `rms`.`product_order` (`quantity`, `order_id`,`product_id`) 
-- values (1,2,1);
-- 
-- CREATE TABLE rms.admin(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL,
--     password varchar(100) NOT NULL
-- );
-- 
-- CREATE TABLE rms.rest_info(
--     id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
--     name varchar(100) NOT NULL,
--     address varchar(300) NOT NULL,
--     contact varchar(300) NOT NULL
-- );
-- 
-- INSERT INTO rms.admin(`name`,`password`) values("zaka","zaka");
-- 
-- INSERT INTO
--   `rms`.`rest_info`(`name`, `address`, `contact`)
-- values(
--     "Fast Fest",
--     "XYZ Location",
--     "03433489123"
--   );
  
  
-- =========================================================================
