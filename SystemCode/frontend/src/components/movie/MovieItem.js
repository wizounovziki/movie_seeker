import React from 'react'
import style from '../../css/item.scss'

export default class MovieItem extends React.Component{
    constructor(props){
        super(props)

        this.state={

        }
    }

    componentWillMount(){

    }
    render(){
        return(<div className={style.box}>
            <img src={this.props.images.small.replace('.jpg','.webp')} className={style.img}></img>
            <h4>Title:{this.props.title}</h4>
            <h4>Year:{this.props.year}</h4>
            <h4>Type:{this.props.genres.join(',')}</h4>
        </div>)
    }
}
