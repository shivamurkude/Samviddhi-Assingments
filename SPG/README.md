## Commands tp create Database

CREATE DATABASE teacher;
CREATE USER teacher WITH PASSWORD 'root';
ALTER ROLE teacher SET client_encoding TO 'utf8';
ALTER ROLE teacher SET default_transaction_isolation TO 'read committed';
ALTER ROLE teacher SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE teacher TO teacher;