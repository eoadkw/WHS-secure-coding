import { Link } from 'react-router-dom';

function Header() {
  return (
    <header style={{ padding: '1rem', backgroundColor: '#f4f4f4' }}>
      <h1>🛍️ 중고 거래 플랫폼</h1>
      <nav style={{ marginTop: '0.5rem' }}>
        <Link to="/" style={{ marginRight: '1rem' }}>홈</Link>
        <Link to="/products" style={{ marginRight: '1rem' }}>상품 목록</Link>
        <Link to="/report">신고하기</Link>
      </nav>
    </header>
  );
}

export default Header;

