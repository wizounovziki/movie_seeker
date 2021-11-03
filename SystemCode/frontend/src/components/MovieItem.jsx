import React from 'react'

import style from '../css/item.scss'
import { Rate } from 'antd';
export default class MovieItem extends React.Component{
    constructor(props){
        super(props)

        this.state={
            
        }
    }
    componentWillMount(){
           
    }
    goDetail=()=>{
        this.props.history.push('/movie/detail/'+this.props.id)
    }
    render(){
        return<div className={style.box} style={{"height":360, "width":230}} onClick={this.goDetail}>
            <img src={this.props.img} style={{"width":150,"height":210}} onerror={this.src=require('../img/loadingFailed.jpg')}></img>
            <div>
            Rate: <Rate allowHalf disabled defaultValue={this.props.rate} />
            </div>
            <h4 style={{width: 170}}><b>{this.props.title}</b></h4>
            <h4 style={{width: 170}}>Year: {this.props.year}</h4>
            <div style={{width: 170, 'word-wrap':'break-word','word-break':'break-all'}}>
            <h4>{this.props.genre}</h4>
            </div>
        </div>
    }
    
}
