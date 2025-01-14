import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Header from './Header';
import Enter from './Enter';
import Display from './Display';
import Footer from './Footer.js'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <Header />
      <Enter />
      <Display />
  <Footer />
  </React.StrictMode>
);
