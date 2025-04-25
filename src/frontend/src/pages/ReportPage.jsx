import {useEffect,useState} from 'react';
import api from '../api/axios';
import {Link} from 'react-router-dom';

export default function ReportPage(){
  const [reports,setReports]=useState([]);
  useEffect(()=>{
    api.get('/products/reports/')
      .then(res=>setReports(res.data))
      .catch(err=>console.error(err));
  },[]);
  return (
    <div style={{padding:'1rem'}}>
      <h2>신고한 상품 목록</h2>
      <ul>
        {reports.map(r=>(
          <li key={r.id}>
            <Link to={`/products/${r.product}`}>{r.product} – {r.reason}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

