-- CREATE TABLE "user"(
--     "id_user" INTEGER NOT NULL,
--     "username" VARCHAR(255) NOT NULL,
--     "userfamily" VARCHAR(255) NOT NULL,
--     "age" INTEGER NOT NULL
-- );
-- ALTER TABLE
--     "user" ADD PRIMARY KEY("id_user");
-- CREATE TABLE "BanckAccount"(
--     "id_bank" INTEGER NOT NULL,
--     "bankname" INTEGER NOT NULL,
--     "balance" INTEGER NOT NULL,
--     "id_user" INTEGER NOT NULL
-- );
-- ALTER TABLE
--     "BanckAccount" ADD PRIMARY KEY("id_bank");
-- CREATE TABLE "trip"(
--     "id_trip" INTEGER NOT NULL,
--     "origin" VARCHAR(255) NOT NULL,
--     "destintion" VARCHAR(255) NOT NULL,
--     "id_user" INTEGER NOT NULL,
--     "id_card" INTEGER NOT NULL
-- );
-- ALTER TABLE
--     "trip" ADD PRIMARY KEY("id_trip");
-- CREATE TABLE "unnamed_table_4"(
--     "id_card" INTEGER NOT NULL,
--     "balance" INTEGER NOT NULL,
--     "type_card" VARCHAR(255) NOT NULL,
--     "date_card" DATE NULL,
--     "id_user" INTEGER NOT NULL
-- );
-- ALTER TABLE
--     "unnamed_table_4" ADD PRIMARY KEY("id_card");
-- ALTER TABLE
--     "BanckAccount" ADD CONSTRAINT "banckaccount_id_user_foreign" FOREIGN KEY("id_user") REFERENCES "user"("id_user");
-- ALTER TABLE
--     "trip" ADD CONSTRAINT "trip_id_user_foreign" FOREIGN KEY("id_user") REFERENCES "user"("id_user");
-- ALTER TABLE
--     "unnamed_table_4" ADD CONSTRAINT "unnamed_table_4_id_user_foreign" FOREIGN KEY("id_user") REFERENCES "user"("id_user");
-- ALTER TABLE
--     "trip" ADD CONSTRAINT "trip_id_card_foreign" FOREIGN KEY("id_card") REFERENCES "unnamed_table_4"("id_card");



-- insert into users (id_user,username,userfamily,age)
-- values(1000,'reza','amin',22),
-- (1001,'mohammad','rezaei',18),
-- (1002,'ehasn','daryadel',15),
-- (1003,'amir','hassani',20);



-- insert into cards (id_card,balance,type_card,date_card,id_user)
-- values(2000,23000,'singlecard',NULL,1000),
-- (2001,25000,'creditcard',NULL,1001),
-- (2002,7000,'termcard',NULL,1002),
-- (2003,23000,'termcard',NULL,1000)


-- insert into trip(id_trip,origin,destintion,id_user,id_card)
-- values(5000,'isfahan','tehran',1000,2000),
-- (5001,'tehran','isfahan',1000,2003),
-- (5002,'mashad','qom',1001,2001),
-- (5003,'shiraz','sannandaj',1002,2002);





-- Question 1

-- select DISTINCT trip.id_user, users.username
-- from trip
-- join users
-- on trip.id_user = users.id_user
-- order by id_user asc;





-- Question 2

-- select trip.id_user,users.username,users.userfamily
-- from trip
-- join cards
-- on trip.id_card = cards.id_card
-- join users
-- on trip.id_user = users.id_user
-- where cards.type_card = 'singlecard';





-- Question 3

-- select count( DISTINCT cards.type_card) as counter_card,trip.id_user,users.userfamily,users.username
-- from trip
-- join cards
-- on trip.id_card = cards.id_card
-- join users
-- on trip.id_user = users.id_user
-- group by trip.id_user,users.userfamily,users.username
-- having count(trip.id_card) > 1








-- Question 4

-- select users.username,users.userfamily,origin,destintion,cards.balance
-- from trip
-- join users
-- on trip.id_user = users.id_user
-- join cards
-- on trip.id_card = cards.id_card







-- Question 5

--  select DISTINCT id_trip
-- from trip
-- join cards
-- on trip.id_card = cards.id_card
-- join users
-- on trip.id_user = cards.id_user
-- where (users.age * 1000 < cards.balance);












