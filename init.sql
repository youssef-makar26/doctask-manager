CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title TEXT,
    priority TEXT,
    done BOOLEAN DEFAULT FALSE
);
