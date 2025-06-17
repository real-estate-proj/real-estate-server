-- Insert sample data into users
insert into
  users (
    name,
    email,
    phone,
    password_hash,
    role,
    avatar_url,
    created_at
  )
values
  (
    'Alice Johnson',
    'alice@example.com',
    '123-456-7890',
    'hashed_password_1',
    'landlord',
    'http://example.com/avatar1.jpg',
    now()
  ),
  (
    'Bob Smith',
    'bob@example.com',
    '234-567-8901',
    'hashed_password_2',
    'tenant',
    'http://example.com/avatar2.jpg',
    now()
  ),
  (
    'Charlie Brown',
    'charlie@example.com',
    '345-678-9012',
    'hashed_password_3',
    'admin',
    'http://example.com/avatar3.jpg',
    now()
  ),
  (
    'David Wilson',
    'david@example.com',
    '456-789-0123',
    'hashed_password_4',
    'landlord',
    'http://example.com/avatar4.jpg',
    now()
  ),
  (
    'Eva Green',
    'eva@example.com',
    '567-890-1234',
    'hashed_password_5',
    'tenant',
    'http://example.com/avatar5.jpg',
    now()
  );

-- Insert sample data into property_types
insert into
  property_types (name)
values
  ('Apartment'),
  ('House'),
  ('Condo');

-- Insert sample data into locations
insert into
  locations (province, district, ward, street)
values
  (
    'Province A',
    'District 1',
    'Ward 1',
    'Street 123'
  ),
  (
    'Province B',
    'District 2',
    'Ward 2',
    'Street 456'
  ),
  (
    'Province C',
    'District 3',
    'Ward 3',
    'Street 789'
  );

-- Insert sample data into properties
insert into
  properties (
    user_id,
    type_id,
    location_id,
    title,
    description,
    price,
    area,
    bedrooms,
    bathrooms,
    status,
    featured,
    published_at,
    is_verified
  )
values
  (
    1,
    1,
    1,
    'Luxury Apartment',
    'A beautiful luxury apartment with modern amenities.',
    500000,
    1200,
    3,
    2,
    'available',
    true,
    now(),
    true
  ),
  (
    2,
    2,
    2,
    'Cozy House',
    'A cozy house perfect for a small family.',
    300000,
    800,
    2,
    1,
    'available',
    false,
    now(),
    false
  ),
  (
    1,
    3,
    3,
    'Modern Condo',
    'A modern condo in the city center.',
    400000,
    1000,
    2,
    2,
    'sold',
    true,
    now(),
    true
  );

-- Insert sample data into images
insert into
  images (property_id, url)
values
  (1, 'http://example.com/image1.jpg'),
  (2, 'http://example.com/image2.jpg'),
  (3, 'http://example.com/image3.jpg');

-- Insert sample data into favorites
insert into
  favorites (user_id, property_id)
values
  (2, 1),
  (2, 3),
  (5, 2);

-- Insert sample data into chats
insert into
  chats (user1_id, user2_id, created_at)
values
  (1, 2, now()),
  (3, 4, now()),
  (2, 5, now());

-- Insert sample data into messages
insert into
  messages (chat_id, sender_id, content, sent_at)
values
  (
    1,
    1,
    'Hello, I am interested in your property.',
    now()
  ),
  (
    1,
    2,
    'Great! Let me know if you have any questions.',
    now()
  ),
  (2, 3, 'Hi, can we discuss the details?', now());

-- Insert sample data into admins
insert into
  admins (user_id, is_super)
values
  (3, true);

-- Insert sample data into reports
insert into
  reports (property_id, reporter_id, reason, created_at)
values
  (2, 5, 'Illegal listing', now()),
  (3, 2, 'Misleading information', now());

-- Insert sample data into tags
insert into
  tags (name)
values
  ('Luxury'),
  ('Pet-friendly'),
  ('Near public transport');

-- Insert sample data into property_tags
insert into
  property_tags (property_id, tag_id)
values
  (1, 1),
  (2, 2),
  (3, 3);

-- Insert sample data into blogs
insert into
  blogs (user_id, title, content, created_at)
values
  (
    1,
    'The Future of Real Estate',
    'Exploring the trends in real estate.',
    now()
  ),
  (
    2,
    'How to Buy a House',
    'A guide to buying your first home.',
    now()
  );

-- Insert sample data into comments
insert into
  comments (blog_id, user_id, content, created_at)
values
  (1, 2, 'Great insights!', now()),
  (2, 1, 'Very helpful, thanks!', now());

-- Insert sample data into blog_reports
insert into
  blog_reports (blog_id, reporter_id, reason, created_at)
values
  (1, 3, 'Inappropriate content', now());

-- Insert sample data into comment_reports
insert into
  comment_reports (comment_id, reporter_id, reason, created_at)
values
  (1, 4, 'Spam', now());

-- Insert sample data into votes
insert into
  votes (user_id, blog_id, vote_type, created_at)
values
  (1, 1, 'upvote', now()),
  (2, 2, 'downvote', now());