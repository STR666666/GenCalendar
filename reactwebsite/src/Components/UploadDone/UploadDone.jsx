import React from 'react'
import { useState } from 'react'
import './UploadDone.css'
import { Logo } from '../Logo/Logo'
import checkicon from '../Assets/check_icon.png'
import { Upload } from '../Upload/Upload'

export const UploadDone = () => {
    
    return (
        <div className="page">
        <Logo></Logo>
        <div className="allelementssignup">
            <div className="updbigtext">Transcript uploaded!</div>
            <img src={checkicon} width="275px"></img>
            <div className="updbtn" id="updbtn">
                <button>Done</button>
            </div>
        </div>
        </div>
        
    )
}
