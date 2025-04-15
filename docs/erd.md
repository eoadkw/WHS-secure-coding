# 📦 ERD 설계

## User
- id (PK)
- username
- password
- email
- is_admin
- created_at

## Product
- id (PK)
- seller_id (FK: User)
- title
- description
- price
- is_active
- created_at

## Message
- id (PK)
- sender_id (FK: User)
- receiver_id (FK: User)
- content
- timestamp

## Transaction
- id (PK)
- buyer_id (FK: User)
- seller_id (FK: User)
- product_id (FK: Product)
- amount
- status
- timestamp
