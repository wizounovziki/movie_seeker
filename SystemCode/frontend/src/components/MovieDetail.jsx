import React from 'react'
import {Link,Route,Switch} from 'react-router-dom'
import { Button,Spin, Alert ,Rate} from 'antd';
import { LeftOutlined } from '@ant-design/icons';
import Axios from 'axios'
export default class MovieDetail extends React.Component{
    constructor(props){
        super(props)
        
        this.state={
            size: 'small',
            isloading: 'true',
            info: new Object(),
            value: 0,
            valueChanged: false,
            login: false
           
        }
    }

    componentWillMount(){
        var tk = ''
        if (localStorage.getItem("token")) {
            //add token
            this.setState({login:true})
            tk = localStorage.getItem("token");
        }

        const fetchConfig = {
            headers: { 'content-type': `multipart/form-data` ,'token': tk }
        }
        
        // var link = 'http://e9e7-116-88-178-213.ngrok.io'
        var link = 'http://127.0.0.1:5001'
        fetch(link + '/movie_detail/'+
        this.props.match.params.id, fetchConfig)
        .then(response=>{
            return response.json()
        })
        .then(data=>{
            console.log(data)

            this.setState({
                info:data,
                isloading:false
            })
            if(this.state.login){
                this.setState({value:this.state.info.user_rate})
            }
        }).catch(err => {
            //console.error.bind(err);
            // redirect to login
            localStorage.clear();
            this.setState({
                login:false
            })
    })
    }

    goBack=()=>{
        this.props.history.go(-1)
    }

    handleChange=(value)=>{
        this.setState({ value:value, valueChanged:true });
    }

    handleSubmit=()=>{
        alert('Rating submitted')
        let formData = new FormData()
        formData.append('rating', this.state.value)
        formData.append('movie_id', this.state.info.id)
        var tk = ''
        if (localStorage.getItem("token")) tk = localStorage.getItem("token");
        const config = {
            headers: { 'content-type': `multipart/form-data` ,'token': tk }
        }
        var link = 'http://127.0.0.1:5001/rating'
        // var link = 'http://e9e7-116-88-178-213.ngrok.io/rating'
        Axios.post(link, formData, config)
        .then((response) =>{
            var data = response.data

            if (data['status']=='true') this.setState({ valueChanged:false });

        })
        // this.setState({ valueChanged:false });
    }

    renderInfo(){
        if(this.state.isloading){
            return<Spin tip="Loading...">
                <Alert
                message="Requesting"
                description="A few seconds..."
                type="info"
                />
           </Spin>
           



        }else{
            console.log(this.state.info)

            return<div style={{textAlign:"center"}}>
                
                <h1 style={{'font-size':30}}><b>{this.state.info.title}</b></h1> 
                <div style={{'margin-bottom':10}}> General Rate: <Rate allowHalf disabled defaultValue={this.state.info.rate} /></div>
                <a href={this.state.info.url}>
                <img src={this.state.info.img} style={{"height":600,"width":450}} onerror={this.src=''}></img>
                </a>
                <p style={{textIndent:'2em',lineHeight:"30px"}}>Click image to view in IMDB</p>
                <p style={{textIndent:'2em',lineHeight:"30px",'font-size':20}}>{this.state.info.genre}</p>
                { this.state.login?
                <div>
                Your Rate: <Rate allowHalf  onChange={this.handleChange} value={this.state.value}/> 
                { this.state.valueChanged?<Button onClick={this.handleSubmit}>Submit</Button> : null}              
                </div> : null
                }
            </div>
        }
    }

    render(){
        return<div>
             <Button type="primary" 
             shape="round" 
             icon={<LeftOutlined/>} 
             size={this.state.size}
             onClick={this.goBack}>
                 
                Back to list
             </Button>
             {this.renderInfo()}
        </div>

    }
    
}
