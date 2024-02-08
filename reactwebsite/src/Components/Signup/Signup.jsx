import React from 'react'
import './Signup.css'
import { Logo } from '../Logo/Logo'

export const Signup = () => {
  return (
    <div className="page">
      <Logo></Logo>
      <div className="allelementssignup">
        <div className="bigtext">Create your account</div>
        <div className="signupcontainer">
            <div className="text">Name</div>
            <div className="Webshop" id="Webshop">
                <input type="email" placeholder='John Doe' />
            </div>
            <div className="text">Email</div>
            <div className="Webshop" id="Webshop">
                <input type="email" placeholder='student@ucsb.edu' />
            </div>
            <div className="text">Password</div>
            <div className="Webshop" id="Webshop">
                <input type="password" placeholder='Password' />
            </div>
            <div className="Webshop" id="Webshop">
                <button className="button">Let's go!</button>
            </div>
        </div>
      </div>
    </div>
    
  )
}
