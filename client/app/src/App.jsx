import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import {BrowserRouter,Routes, Route} from 'react-router-dom';
import Home from './components/Home';
import Oncekiler from './components/Heyo.jsx'
import Login from './components/Login.jsx';
import './App.css'
import Register from './components/Register.jsx';

function App() {
  return <div className='App'>
    
    <Routes>
      <Route path="" element={<Home/>}/>
      <Route path="/eski" element={<Oncekiler />}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/register" element={<Register/>}/>
    </Routes>
    
    

  </div>
}

export default App
