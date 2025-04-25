import { useEffect, useState } from 'react';
import api from '../api/axios';
import ProductCard from '../components/ProductCard';

export default function WishlistPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get('/products/?liked=true')
       .then(res => setProducts(res.data))
       .catch(err => console.error(err));
  }, []);

  return (
    <div className="page-container">
      <h2>찜한 상품 목록</h2>
      {products.length === 0
        ? <p className="empty-text">찜한 상품이 없습니다.</p>
        : <div className="grid">
            {products.map(p => <ProductCard key={p.id} product={p} />)}
          </div>
      }
    </div>
  );
}

