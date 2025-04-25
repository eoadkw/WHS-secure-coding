// src/components/Layout.jsx
import React from 'react';
import { Outlet } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';

export default function Layout() {
  return (
    <div className="app-container">
      <Header />
      {/* CSS에서 main.content 에 스타일을 걸었으므로 className="content" 꼭 넣어주세요 */}
      <main className="content">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
}

