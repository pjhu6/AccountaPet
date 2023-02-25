CREATE TABLE IF NOT EXISTS users (
	user_id text PRIMARY KEY,
	points integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS pets (
    pet_id text PRIMARY KEY,
    pet_name text DEFAULT NULL,
    species text DEFAULT NULL,
    hunger integer DEFAULT 5,
    happiness integer DEFAULT 0,
    birthday DATE,
    user_id text,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS consumables (
    c_name text DEFAULT NULL,
    cost integer DEFAULT 0,
    hunger_value integer DEFAULT 0,
    happiness_value integer DEFAULT 0,
    user_id text,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
