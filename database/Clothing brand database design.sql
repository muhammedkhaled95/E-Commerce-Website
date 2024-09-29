CREATE TABLE "users" (
  "id" int PRIMARY KEY,
  "username" varchar UNIQUE,
  "email" varchar UNIQUE,
  "password" varchar,
  "full_name" varchar,
  "is_active" bool,
  "created_at" timestamp,
  "role" varchar
);

CREATE TABLE "carts" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "created_at" timestamp,
  "total_amount" float,
  "status" varchar
);

CREATE TABLE "cart_items" (
  "id" int PRIMARY KEY,
  "cart_id" int,
  "product_id" int,
  "quantity" int,
  "subtotal" float
);

CREATE TABLE "categories" (
  "id" int PRIMARY KEY,
  "name" varchar UNIQUE
);

CREATE TABLE "products" (
  "id" int PRIMARY KEY,
  "title" varchar,
  "description" varchar,
  "price" int,
  "discount_percentage" float,
  "rating" float,
  "stock" int,
  "brand" varchar,
  "thumbnail" varchar,
  "images" varchar,
  "is_published" bool,
  "created_at" timestamp,
  "category_id" int
);

CREATE TABLE "payments" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "cart_id" int,
  "amount" float,
  "status" varchar,
  "payment_method" varchar,
  "transaction_id" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "orders" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "cart_id" int,
  "total_amount" float,
  "status" varchar,
  "shipping_address" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

CREATE TABLE "addresses" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "type" varchar,
  "address_line1" varchar,
  "address_line2" varchar,
  "city" varchar,
  "state" varchar,
  "postal_code" varchar,
  "country" varchar,
  "created_at" timestamp,
  "updated_at" timestamp
);

ALTER TABLE "products" ADD FOREIGN KEY ("category_id") REFERENCES "categories" ("id");

ALTER TABLE "cart_items" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("id");

ALTER TABLE "cart_items" ADD FOREIGN KEY ("cart_id") REFERENCES "carts" ("id");

ALTER TABLE "carts" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "payments" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "payments" ADD FOREIGN KEY ("cart_id") REFERENCES "carts" ("id");

ALTER TABLE "orders" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");

ALTER TABLE "orders" ADD FOREIGN KEY ("cart_id") REFERENCES "carts" ("id");

ALTER TABLE "addresses" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id");
