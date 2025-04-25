import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../api/axios';

export default function ProductDetailPage() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    api.get(`/products/${id}/`)
       .then(res => setProduct(res.data))
       .catch(err => console.error(err));
  }, [id]);

  if (!product) return <p className="loading">로딩 중…</p>;

  return (
    <div className="page-container detail-container">
      <h2 className="detail-title">{product.title}</h2>
      <p className="detail-price">{product.price.toLocaleString()}원</p>
      <p className="detail-desc">{product.description}</p>
      <p className="detail-meta">
        작성자: {product.seller_username} · 찜 {product.likes_count}회 · 신고 {product.reports_count}회
      </p>
    </div>
  );
}

