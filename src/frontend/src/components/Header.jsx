import { NavLink } from 'react-router-dom';

export default function Header() {
  return (
    <header>
      <h1>📦 중고 거래 플랫폼</h1>
      <nav>
        <NavLink to="/" end>홈</NavLink>
        <NavLink to="/products">상품 목록</NavLink>
        <NavLink to="/wishlist">찜한 상품</NavLink>
        <NavLink to="/reports">신고 목록</NavLink>
      </nav>
    </header>
  );
}

