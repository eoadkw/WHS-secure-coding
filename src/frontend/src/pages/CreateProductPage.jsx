import {useState} from 'react';
import api from '../api/axios';
import {useNavigate} from 'react-router-dom';

export default function CreateProductPage(){
  const [form,setForm]=useState({title:'',description:'',price:''});
  const nav=useNavigate();
  const onSubmit=e=>{
    e.preventDefault();
    api.post('/products/',form)
      .then(()=>nav('/products'))
      .catch(err=>console.error(err));
  };
  return (
    <div style={{padding:'1rem'}}>
      <h2>상품 등록</h2>
      <form onSubmit={onSubmit}>
        <label>제목<br/>
          <input value={form.title}
                 onChange={e=>setForm({...form,title:e.target.value})}/>
        </label><br/>
        <label>설명<br/>
          <textarea value={form.description}
                    onChange={e=>setForm({...form,description:e.target.value})}/>
        </label><br/>
        <label>가격<br/>
          <input type="number" value={form.price}
                 onChange={e=>setForm({...form,price:e.target.value})}/>
        </label><br/>
        <button type="submit">등록</button>
      </form>
    </div>
  );
}

