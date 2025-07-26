import React from 'react';
import Sidebar from './Sidebar';
import Header from './Header';

const Layout = ({ children }) => {
  return (
    <div className="min-h-screen bg-background">
      <Sidebar />
      <Header />
      <main className="ml-16 pt-16 p-6">
        {children}
      </main>
    </div>
  );
};

export default Layout;

