import React from "react"
import { Routes, Route, Link, NavLink } from "react-router-dom"
import Home from "./home"
import About from "./about"

export default function App() {
  return (
    <div>
      <h1>My App</h1>
      <NavLink className={({isActive}) => isActive && "text-red"}/>
      <nav>
        <Link to="/">Home</Link> |{" "}
        <Link to="/about">About</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </div>
  )
}
