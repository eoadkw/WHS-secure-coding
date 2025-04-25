import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/axios';

export default function CreateProductPage() {
  const [form, setForm] = useState({ title:'', description:'', price:'' });
  const nav = useNavigate();

  const handleSubmit = e => {
    e.preventDefault();
    api.post('/products/', form)
       .then(() => nav('/products'))
       .catch(err => console.error(err));
  };

  return (
    <div className="page-container form-container">
      <h2 className="form-title">상품 등록</h2>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label>제목</label>
          <input
            type="text"
            value={form.title}
            onChange={e => setForm({...form, title: e.target.value})}
            required
          />
        </div>
        <div className="form-group">
          <label>설명</label>
          <textarea
            value={form.description}
            onChange={e => setForm({...form, description: e.target.value})}
            required
          />
        </div>
        <div className="form-group">
          <label>가격</label>
          <input
            type="number"
            value={form.price}
            onChange={e => setForm({...form, price: e.target.value})}
            required
          />
        </div>
        <button type="submit" className="btn">등록</button>
      </form>
    </div>
  );
}

