BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 32e1bb9aed91

INSERT INTO alembic_version (version_num) VALUES ('32e1bb9aed91') RETURNING alembic_version.version_num;

-- Running upgrade 32e1bb9aed91 -> 6c7a64b479db

CREATE TABLE users (
    id SERIAL NOT NULL, 
    name VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    phone VARCHAR(20), 
    password_hash TEXT, 
    role VARCHAR(20), 
    avatar_url TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (email)
);

CREATE INDEX ix_users_id ON users (id);

UPDATE alembic_version SET version_num='6c7a64b479db' WHERE alembic_version.version_num = '32e1bb9aed91';

-- Running upgrade 6c7a64b479db -> 05cbf8fd7821

ALTER TABLE users ADD COLUMN is_admin TEXT;

UPDATE alembic_version SET version_num='05cbf8fd7821' WHERE alembic_version.version_num = '6c7a64b479db';

-- Running upgrade 05cbf8fd7821 -> 1d070c1fed06

CREATE TABLE locations (
    id BIGSERIAL NOT NULL, 
    province TEXT, 
    district TEXT, 
    ward TEXT, 
    street TEXT, 
    PRIMARY KEY (id)
);

CREATE TABLE property_types (
    id BIGSERIAL NOT NULL, 
    name TEXT, 
    PRIMARY KEY (id)
);

CREATE TABLE tags (
    id BIGSERIAL NOT NULL, 
    name TEXT, 
    PRIMARY KEY (id)
);

CREATE TABLE admins (
    id BIGSERIAL NOT NULL, 
    user_id BIGINT, 
    is_super BOOLEAN, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE blogs (
    id BIGSERIAL NOT NULL, 
    user_id BIGINT, 
    title TEXT, 
    content TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE chats (
    id BIGSERIAL NOT NULL, 
    user1_id BIGINT, 
    user2_id BIGINT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user1_id) REFERENCES users (id), 
    FOREIGN KEY(user2_id) REFERENCES users (id)
);

CREATE TABLE properties (
    id BIGSERIAL NOT NULL, 
    user_id BIGINT, 
    type_id BIGINT, 
    location_id BIGINT, 
    title TEXT, 
    description TEXT, 
    price NUMERIC, 
    area NUMERIC, 
    bedrooms INTEGER, 
    bathrooms INTEGER, 
    status TEXT, 
    featured BOOLEAN, 
    published_at TIMESTAMP WITHOUT TIME ZONE, 
    is_verified BOOLEAN, 
    PRIMARY KEY (id), 
    CONSTRAINT check_property_status CHECK (status IN ('available', 'sold', 'rented')), 
    FOREIGN KEY(location_id) REFERENCES locations (id), 
    FOREIGN KEY(type_id) REFERENCES property_types (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE blog_reports (
    id BIGSERIAL NOT NULL, 
    blog_id BIGINT, 
    reporter_id BIGINT, 
    reason TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(blog_id) REFERENCES blogs (id), 
    FOREIGN KEY(reporter_id) REFERENCES users (id)
);

CREATE TABLE comments (
    id BIGSERIAL NOT NULL, 
    blog_id BIGINT, 
    user_id BIGINT, 
    content TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(blog_id) REFERENCES blogs (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE favorites (
    user_id BIGINT NOT NULL, 
    property_id BIGINT NOT NULL, 
    PRIMARY KEY (user_id, property_id), 
    FOREIGN KEY(property_id) REFERENCES properties (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE images (
    id BIGSERIAL NOT NULL, 
    property_id BIGINT, 
    url TEXT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(property_id) REFERENCES properties (id)
);

CREATE TABLE messages (
    id BIGSERIAL NOT NULL, 
    chat_id BIGINT, 
    sender_id BIGINT, 
    content TEXT, 
    sent_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(chat_id) REFERENCES chats (id), 
    FOREIGN KEY(sender_id) REFERENCES users (id)
);

CREATE TABLE property_tags (
    property_id BIGINT NOT NULL, 
    tag_id BIGINT NOT NULL, 
    PRIMARY KEY (property_id, tag_id), 
    FOREIGN KEY(property_id) REFERENCES properties (id), 
    FOREIGN KEY(tag_id) REFERENCES tags (id)
);

CREATE TABLE reports (
    id BIGSERIAL NOT NULL, 
    property_id BIGINT, 
    reporter_id BIGINT, 
    reason TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(property_id) REFERENCES properties (id), 
    FOREIGN KEY(reporter_id) REFERENCES users (id)
);

CREATE TABLE votes (
    id BIGSERIAL NOT NULL, 
    user_id BIGINT, 
    blog_id BIGINT, 
    vote_type TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    CONSTRAINT check_vote_type CHECK (vote_type IN ('upvote', 'downvote')), 
    FOREIGN KEY(blog_id) REFERENCES blogs (id), 
    FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE comment_reports (
    id BIGSERIAL NOT NULL, 
    comment_id BIGINT, 
    reporter_id BIGINT, 
    reason TEXT, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(comment_id) REFERENCES comments (id), 
    FOREIGN KEY(reporter_id) REFERENCES users (id)
);

ALTER TABLE users ALTER COLUMN id TYPE BIGINT;

ALTER TABLE users ALTER COLUMN name TYPE TEXT;

ALTER TABLE users ALTER COLUMN name DROP NOT NULL;

ALTER TABLE users ALTER COLUMN email TYPE TEXT;

ALTER TABLE users ALTER COLUMN email DROP NOT NULL;

ALTER TABLE users ALTER COLUMN phone TYPE TEXT;

ALTER TABLE users ALTER COLUMN role TYPE TEXT;

ALTER TABLE users ALTER COLUMN role SET NOT NULL;

DROP INDEX ix_users_id;

ALTER TABLE users DROP COLUMN is_admin;

UPDATE alembic_version SET version_num='1d070c1fed06' WHERE alembic_version.version_num = '05cbf8fd7821';

-- Running upgrade 1d070c1fed06 -> b89341322321

UPDATE alembic_version SET version_num='b89341322321' WHERE alembic_version.version_num = '1d070c1fed06';

-- Running upgrade b89341322321 -> ffcd5fb5c225

ALTER TABLE comments DROP COLUMN created_at;

UPDATE alembic_version SET version_num='ffcd5fb5c225' WHERE alembic_version.version_num = 'b89341322321';

-- Running upgrade ffcd5fb5c225 -> 195fdc6ee92c

ALTER TABLE comments ADD COLUMN created_at TIMESTAMP WITHOUT TIME ZONE;

UPDATE alembic_version SET version_num='195fdc6ee92c' WHERE alembic_version.version_num = 'ffcd5fb5c225';

-- Running upgrade 195fdc6ee92c -> 19fe0a96fb4c

UPDATE alembic_version SET version_num='19fe0a96fb4c' WHERE alembic_version.version_num = '195fdc6ee92c';

-- Running upgrade 19fe0a96fb4c -> a3e314346527

ALTER TABLE users ADD COLUMN is_verified BOOLEAN;

UPDATE alembic_version SET version_num='a3e314346527' WHERE alembic_version.version_num = '19fe0a96fb4c';

-- Running upgrade a3e314346527 -> 85b84f1c6103

CREATE TABLE email_verifications (
    id SERIAL NOT NULL, 
    user_id BIGINT NOT NULL, 
    code VARCHAR(6) NOT NULL, 
    expires_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    is_used BOOLEAN NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(user_id) REFERENCES users (id), 
    UNIQUE (user_id)
);

UPDATE alembic_version SET version_num='85b84f1c6103' WHERE alembic_version.version_num = 'a3e314346527';

COMMIT;

