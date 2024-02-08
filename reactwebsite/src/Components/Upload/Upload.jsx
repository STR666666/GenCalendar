import React, { useRef } from 'react'
import { useState } from 'react'
import './Upload.css'
import { Logo } from '../Logo/Logo'
import { UploadDone } from '../UploadDone/UploadDone'

export const Upload = () => {
    const orig = {background: '#F3F5F7'}
    const onhover = {background: '#d3e4f5'}

    const [color, setColor] = useState(orig)
    const [files, setFiles] = useState(null);
    const inputRef = useRef();

    const handleDragOver = (event) => {
        event.preventDefault();
        setColor(onhover)
    };
    const handleDrop = (event) => {
        event.preventDefault();
    };

    const handleDragLeave = (event) => {
        setColor(orig)
    }

    if (files)
        return (<UploadDone></UploadDone>)

    return (
        <div className="page">
        <Logo></Logo>
        <div className="allelementssignup">
            <div className="uploadbigtext">Upload your transcript</div>
            {!files && (
            <div className="uploadbox" style={color} onDragOver={handleDragOver} onDrop={handleDrop} onDragLeave={handleDragLeave}>
                <div className="frame11">
                    <div className="frame10">
                        <div className="innerbigtext">Drag and drop files here</div>
                        <div className="g20">
                            <div className = "line"></div>
                            <div className="smalltext">Or</div>
                            <div className = "line"></div>
                        </div>
                    </div>
                    <input type="file" onChange={(event) => setFiles(event.target.files)} hidden ref={inputRef}></input>
                    <div className="frame9">
                        <div className="UploadWebShop" id="UploadWebShop">
                            <button onClick={() => inputRef.current.click()}>Browse files</button>
                        </div>
                    </div>
                </div>
            </div>)}
        </div>
        </div>
        
    )
}
