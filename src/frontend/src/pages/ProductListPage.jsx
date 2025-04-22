import { useEffect, useState } from 'react';
import api from '../api/axios';

function ProductListPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    api.get('products/')
      .then(response => setProducts(response.data))
      .catch(error => console.error('상품 목록 불러오기 실패:', error));
  }, []);

  return (
    <div style={{ padding: '1rem' }}>
      <h2>상품 목록</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <strong>{product.title}</strong> - {product.price}원
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductListPage;

