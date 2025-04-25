import {useEffect,useState} from 'react';
import {useParams} from 'react-router-dom';
import api from '../api/axios';

export default function ProductDetailPage(){
  const {id}=useParams();
  const [product,setProduct]=useState(null);
  useEffect(()=>{
    api.get(`/products/${id}/`)
      .then(res=>setProduct(res.data))
      .catch(err=>console.error(err));
  },[id]);
  if(!product) return <p style={{padding:'1rem'}}>로딩 중…</p>;
  return (
    <div style={{padding:'1rem'}}>
      <h2>{product.title}</h2>
      <p>{product.description}</p>
      <p>가격: {product.price}원</p>
      <p>작성자: {product.seller_username}</p>
      <p>찜 {product.likes_count}회 · 신고 {product.reports_count}회</p>
    </div>
  );
}

