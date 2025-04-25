import { useState, useEffect } from 'react';
import api from '../api/axios';

export default function ReportPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get('/api/products/?reported=true', { withCredentials: true })
       .then(res => setProducts(res.data))
       .catch(console.error);
  }, []);

  return (
    <div>
      <h2>신고한 상품 목록</h2>
      <ul>
        {products.map(p => (
          <li key={p.id}>{p.title} – {p.price}원</li>
        ))}
      </ul>
    </div>
  );
}

