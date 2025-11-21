CREATE table IF NOT EXISTS hardware_type (
    id serial primary key,
    name varchar(255) not null unique,
    description text
);

ALTER TABLE hardware
  ADD COLUMN hardware_type_id INT;