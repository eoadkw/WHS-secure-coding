export default function ProductCard({ product }) {
  return (
    <div className="card">
      <div className="thumbnail">📷</div>
      <h3>{product.title}</h3>
      <p>{product.price.toLocaleString()}원</p>
      <a href={`/products/${product.id}`} className="detail-btn">
        상세보기
      </a>
    </div>
  );
}

