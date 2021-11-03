import React, { useEffect, useState } from "react";

// function IframeComp() {
//   const [content, setContent] = useState('');

//   useEffect(() => {
//     fetch("https://www.example.com", {
//       headers: {"Authorization", "JWT eyJ0eXAiOiJK"}
//     })
//       .then(response => response.text())
//       .then(data => setContent(data))
//       .catch(err => err)
//   }, []);

//   return (
//       <iframe sandbox id="inlineFrameExample"
//               title="Inline Frame Example"
//               width="300"
//               height="200"
//               src={content}>
//       </iframe>
//   );
// }

// export default IframeComp;


export default class IframeComp extends React.Component{
    constructor(props){

        super(props)
        this.state={           
        }
    }

    render(){
        const [content, setContent] = useState('');
          useEffect(() => {
            fetch('https://github.com/IRS-PM/Workshop-Project-Submission-Template', {
            'headers': {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
            })
            .then(response => response.text())
            .then(data => setContent(data))
            .catch(err => err)
        }, []);
        return<div>
            <iframe sandbox id="inlineFrameExample"
              title="Inline Frame Example"
              width="300"
              height="200"
              src={content}>
          </iframe>
        </div>
    }
    
}