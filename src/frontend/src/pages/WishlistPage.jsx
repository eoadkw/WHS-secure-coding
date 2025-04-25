import {useEffect,useState} from 'react';
import api from '../api/axios';
import {Link} from 'react-router-dom';

export default function WishlistPage(){
  const [products,setProducts]=useState([]);
  useEffect(()=>{
    api.get('/products/?liked=true')
      .then(res=>setProducts(res.data))
      .catch(err=>console.error(err));
  },[]);
  return (
    <div style={{padding:'1rem'}}>
      <h2>찜한 상품 목록</h2>
      <ul>
        {products.map(p=>(
          <li key={p.id}>
            <Link to={`/products/${p.id}`}>{p.title} – {p.price}원</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

