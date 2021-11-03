import React from 'react'


export default class HomeContainer extends React.Component{
    constructor(props){
        super(props)
        this.state={

        }
    }
    render(){
        return<div style={{"text-align":"center"}}>
            <img src={require('../img/WebBG.png')}></img>
        </div>
    }
}
