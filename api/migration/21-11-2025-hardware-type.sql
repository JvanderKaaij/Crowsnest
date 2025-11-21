CREATE table IF NOT EXISTS hardware_type (
    id serial primary key,
    name varchar(255) not null unique,
    description text,
    user_type_id INT,
    active INT
);

ALTER TABLE hardware
  ADD COLUMN hardware_type_id INT;