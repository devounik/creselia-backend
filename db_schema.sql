-- Drop existing tables if they exist
DROP TABLE IF EXISTS databases;
DROP TABLE IF EXISTS queries;
DROP TABLE IF EXISTS chats;
DROP TABLE IF EXISTS chat_sessions;
DROP TABLE IF EXISTS users;

-- 1️⃣ Users Table
CREATE TABLE users (
    uid VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    profile_pic TEXT
);

-- 2️⃣ Chat Sessions Table
CREATE TABLE chat_sessions (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(uid) ON DELETE CASCADE,
    session_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3️⃣ Chats Table
CREATE TABLE chats (
    id SERIAL PRIMARY KEY,
    session_id INT REFERENCES chat_sessions(id) ON DELETE CASCADE,
    user_id VARCHAR(255) REFERENCES users(uid) ON DELETE CASCADE,
    message TEXT NOT NULL,
    response TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4️⃣ Query Logs Table
CREATE TABLE queries (
    id SERIAL PRIMARY KEY,
    session_id INT REFERENCES chat_sessions(id) ON DELETE CASCADE,
    user_id VARCHAR(255) REFERENCES users(uid) ON DELETE CASCADE,
    natural_query TEXT NOT NULL,
    sql_query TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 5️⃣ Database Connections Table
CREATE TABLE databases (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users(uid) ON DELETE CASCADE,
    db_type VARCHAR(50) NOT NULL,
    host VARCHAR(255) NOT NULL,
    port VARCHAR(10) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password TEXT NOT NULL,
    db_name VARCHAR(255) NOT NULL
);
