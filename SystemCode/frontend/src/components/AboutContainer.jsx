import React from 'react'
import IframeComp from './iframes'

export default class AboutContainer extends React.Component{
    constructor(props){
        super(props)
        this.state={

        }
    }
    render(){
        return<div>
            <h1>About</h1>
            <iframe
              title="Inline Frame Example"
               src='https://github.com/IRS-PM/Workshop-Project-Submission-Template'>
            </iframe>
        </div>
    }
}
