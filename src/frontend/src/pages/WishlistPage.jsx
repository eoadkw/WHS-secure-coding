import { useEffect, useState } from "react";
import axios from "axios";

function WishlistPage() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/products/?liked=true", { withCredentials: true })
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.error("찜한 상품 목록 가져오기 실패:", error);
      });
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h2>찜한 상품 목록</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            <strong>{product.title}</strong> - {product.price}원
          </li>
        ))}
      </ul>
    </div>
  );
}

export default WishlistPage;

