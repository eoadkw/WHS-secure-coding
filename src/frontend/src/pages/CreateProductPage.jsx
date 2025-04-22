import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function CreateProductPage() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/api/products/', {
        title,
        description,
        price,
      }, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        }
      });
      navigate('/products');
    } catch (error) {
      console.error('상품 등록 실패:', error);
    }
  };

  return (
    <div style={{ padding: '1rem' }}>
      <h2>상품 등록</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>제목</label><br />
          <input value={title} onChange={(e) => setTitle(e.target.value)} />
        </div>
        <div>
          <label>설명</label><br />
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} />
        </div>
        <div>
          <label>가격</label><br />
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
        </div>
        <button type="submit">등록</button>
      </form>
    </div>
  );
}

export default CreateProductPage;

