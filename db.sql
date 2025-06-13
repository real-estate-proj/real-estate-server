-- Migrations will appear here as you chat with AI

create table users (
  id bigint primary key generated always as identity,
  name text,
  email text unique,
  phone text,
  password_hash text,
  role text,
  avatar_url text,
  created_at timestamp
);

drop table if exists users cascade;

drop table if exists property_types cascade;

drop table if exists locations cascade;

drop table if exists properties cascade;

drop table if exists images cascade;

drop table if exists favorites cascade;

drop table if exists chats cascade;

drop table if exists messages cascade;

drop table if exists admins cascade;

drop table if exists reports cascade;

drop table if exists tags cascade;

drop table if exists property_tags cascade;

drop table if exists blogs cascade;

drop table if exists comments cascade;

drop table if exists blog_reports cascade;

drop table if exists comment_reports cascade;

drop table if exists votes cascade;

create table users (
  id bigint primary key generated always as identity,
  name text,
  email text unique,
  phone text,
  password_hash text,
  role text check (role in ('admin', 'landlord', 'tenant')),
  avatar_url text,
  created_at timestamp
);

create table property_types (
  id bigint primary key generated always as identity,
  name text
);

create table locations (
  id bigint primary key generated always as identity,
  province text,
  district text,
  ward text,
  street text
);

create table properties (
  id bigint primary key generated always as identity,
  user_id bigint,
  type_id bigint,
  location_id bigint,
  title text,
  description text,
  price numeric,
  area numeric,
  bedrooms int,
  bathrooms int,
  status text check (status in ('available', 'sold', 'rented')),
  featured boolean,
  published_at timestamp,
  is_verified boolean,
  foreign key (user_id) references users (id),
  foreign key (type_id) references property_types (id),
  foreign key (location_id) references locations (id)
);

create table images (
  id bigint primary key generated always as identity,
  property_id bigint,
  url text,
  foreign key (property_id) references properties (id)
);

create table favorites (
  user_id bigint,
  property_id bigint,
  primary key (user_id, property_id),
  foreign key (user_id) references users (id),
  foreign key (property_id) references properties (id)
);

create table chats (
  id bigint primary key generated always as identity,
  user1_id bigint,
  user2_id bigint,
  created_at timestamp,
  foreign key (user1_id) references users (id),
  foreign key (user2_id) references users (id)
);

create table messages (
  id bigint primary key generated always as identity,
  chat_id bigint,
  sender_id bigint,
  content text,
  sent_at timestamp,
  foreign key (chat_id) references chats (id),
  foreign key (sender_id) references users (id)
);

create table admins (
  id bigint primary key generated always as identity,
  user_id bigint,
  is_super boolean,
  foreign key (user_id) references users (id)
);

create table reports (
  id bigint primary key generated always as identity,
  property_id bigint,
  reporter_id bigint,
  reason text,
  created_at timestamp,
  foreign key (property_id) references properties (id),
  foreign key (reporter_id) references users (id)
);

create table tags (
  id bigint primary key generated always as identity,
  name text
);

create table property_tags (
  property_id bigint,
  tag_id bigint,
  primary key (property_id, tag_id),
  foreign key (property_id) references properties (id),
  foreign key (tag_id) references tags (id)
);

create table blogs (
  id bigint primary key generated always as identity,
  user_id bigint,
  title text,
  content text,
  created_at timestamp,
  foreign key (user_id) references users (id)
);

create table comments (
  id bigint primary key generated always as identity,
  blog_id bigint,
  user_id bigint,
  content text,
  created_at timestamp,
  foreign key (blog_id) references blogs (id),
  foreign key (user_id) references users (id)
);

create table blog_reports (
  id bigint primary key generated always as identity,
  blog_id bigint,
  reporter_id bigint,
  reason text,
  created_at timestamp,
  foreign key (blog_id) references blogs (id),
  foreign key (reporter_id) references users (id)
);

create table comment_reports (
  id bigint primary key generated always as identity,
  comment_id bigint,
  reporter_id bigint,
  reason text,
  created_at timestamp,
  foreign key (comment_id) references comments (id),
  foreign key (reporter_id) references users (id)
);

create table votes (
  id bigint primary key generated always as identity,
  user_id bigint,
  blog_id bigint,
  vote_type text check (vote_type in ('upvote', 'downvote')),
  created_at timestamp,
  foreign key (user_id) references users (id),
  foreign key (blog_id) references blogs (id)
);

comment on column users.role is 'admin, landlord, tenant';

comment on column properties.status is 'available, sold, rented';