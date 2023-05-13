-- use public schema
SET search_path TO public;

-- Create task table
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100) NOT NULL,
  description TEXT,
  due_datetime DATE
);
