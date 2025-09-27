import React, {useState}from 'react'

function Text() {
    const [text,setText] = useState("Hello")
  return (
    <div>
      <h1>{text}</h1>
      <button onClick={()=> setText("How are you")}>Click to change text</button>
    </div>
  )
}

export default Text
