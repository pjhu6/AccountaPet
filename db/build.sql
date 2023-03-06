CREATE TABLE IF NOT EXISTS users (
	user_id text PRIMARY KEY,
	points integer DEFAULT 0
);

CREATE TABLE IF NOT EXISTS pets (
    pet_name text DEFAULT NULL,
    species text DEFAULT NULL,
    hunger integer DEFAULT 5,
    happiness integer DEFAULT 0,
    birthday DATE,
    user_id text,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS user_consumables (
    c_id text,
    user_id text,
    FOREIGN KEY (c_id) REFERENCES all_consumables(c_id) ON DELETE CASCADE
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS all_consumables (
    c_id text PRIMARY KEY,
    c_name text DEFAULT NULL,
    cost integer DEFAULT 0,
    hunger_value integer DEFAULT 0,
    happiness_value integer DEFAULT 0
);

INSERT INTO all_consumables (c_id, c_name, cost, hunger_value, happiness_value) VALUES ('DOG_FOOD', 'Dog food', 10, 1, 1);
