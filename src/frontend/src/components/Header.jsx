import { Link } from 'react-router-dom';
export default function Header(){
  return (
    <header style={{padding:'1rem',background:'#333',color:'#fff'}}>
      <h1>📦 중고 거래 플랫폼</h1>
      <nav>
        <Link to="/">홈</Link> |{' '}
        <Link to="/products">상품 목록</Link> |{' '}
        <Link to="/wishlist">찜한 상품</Link> |{' '}
        <Link to="/report">신고 목록</Link>
      </nav>
    </header>
  );
}

