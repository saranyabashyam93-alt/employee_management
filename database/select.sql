--SELECT datname FROM pg_database;


SELECT name FROM sqlite_master
WHERE type='table' AND name='employees';