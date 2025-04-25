import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout              from './components/Layout';
import HomePage            from './pages/HomePage';
import ProductListPage     from './pages/ProductListPage';
import ProductDetailPage   from './pages/ProductDetailPage';
import CreateProductPage   from './pages/CreateProductPage';
import WishlistPage        from './pages/WishlistPage';
import ReportPage          from './pages/ReportPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index               element={<HomePage />} />
          <Route path="products"     element={<ProductListPage />} />
          <Route path="products/:id" element={<ProductDetailPage />} />
          <Route path="create"       element={<CreateProductPage />} />
          <Route path="wishlist"     element={<WishlistPage />} />
          <Route path="report"       element={<ReportPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

