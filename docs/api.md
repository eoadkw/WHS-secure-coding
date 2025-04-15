# 📡 API 명세

## 회원가입
- POST /api/register
- body: { username, password, email }
- response: { message }

## 상품 등록
- POST /api/products
- body: { title, description, price }
- header: Authorization (JWT)
- response: { product_id }

## 채팅 전송
- POST /api/message
- body: { to_user_id, content }
- header: Authorization (JWT)
