import React from 'react'
import { Rate, Spin, Alert, Pagination } from 'antd';
import MovieItem from './MovieItem.jsx'
import { data } from 'autoprefixer';
import { thisExpression } from '@babel/types';
export default class MovieList extends React.Component{
    constructor(props){
        super(props)
        this.state={
            movies:[],//Movie List
            nowPage: 1,//当前展示第几页的数据
            pageSize:14,// Num of movies in each page.
            total:0,// Num of movie in current cate
            isloading:true,
            movieType:props.match.params.type

        }
    }


    //当页码改变的时候，加载新一页的数据
    pageChanged=(page)=>{
        this.props.history.push('/movie/'+this.state.movieType+'/'+page)
    }


    loadMovieListByTypeAndPage=()=>{
        // fetchJsonp
        var tk = ''
        if (localStorage.getItem("token")) {
            console.log('exist')
            console.log(localStorage.getItem("token"))
            tk = localStorage.getItem("token");
        }

        const fetchConfig = {
            headers: { 'content-type': `multipart/form-data` ,'token': tk }
        }

        const start=this.state.pageSize*(this.state.nowPage-1)
        const url = `http://127.0.0.1:5001/${this.state.movieType}/${this.state.nowPage}/${this.state.pageSize}`
        // const url = `http://e9e7-116-88-178-213.ngrok.io/${this.state.movieType}/${this.state.nowPage}/${this.state.pageSize}`
        
        console.log('loading')
        console.log(fetchConfig)
        fetch(url,fetchConfig)
        .then(response=>{
            return response.json()
        })
        .then(data=>{        
            console.log(data)
            this.setState({
                isloading:false,//把loading效果隐藏
                movies:data.data,//为电影列表重新赋值
                total:data.total//把总条数 保存到state上
            })         
        })
    }
    componentWillMount(){
        this.loadMovieListByTypeAndPage()
    }

    componentWillReceiveProps(nextProps){
        this.setState({
            isloading:true,
            nowPage:parseInt(nextProps.match.params.page)||1,
            movieType:nextProps.match.params.type,
            
        },function(){
        
            this.loadMovieListByTypeAndPage()
        })
    }


    renderList(){
        if(this.state.isloading){      
            {/* antd spin UI */}
            return<Spin tip="Loading...">
               <Alert
               message="Requesting the list..."
               description="Surprise is coming..."
               type="info"
               />
           </Spin>
        }else{//
            return(<div>
                  <div style={{display:'flex',flexWrap:'wrap', 'margin-left':20}}>
                  {/* {this.state.movies.map((item,i)=>{
                    return<MovieItem {...item} key={i}></MovieItem>
                  })} */}
                  
                   {this.state.movies.map((item,i)=>{

                        return<div>
                              <MovieItem {...item} key={i} history={this.props.history}></MovieItem>
                              
                              </div>
                    })}
                   
                  </div>
                  <Pagination style={{'text-align':'center'}} defaultCurrent={this.state.nowPage} total={this.state.total}
                    pageSize={this.state.pageSize}  onChange={this.pageChanged} />
                  {/* <Pagination defaultCurrent={this.state.nowPage} 
                            total={this.state.total} 
                            pageSize={this.state.pageSize}
                            onChange={this.pageChanged}/> */}

                  </div>)
        }
    }
    render(){
        var t = ''
        if(this.props.match.params.type == 'full_list'){
            t = 'Full List'
        }
        else if (this.props.match.params.type == 'recommend'){
            t = 'Popular Trending'
        }
        else if (this.props.match.params.type == 'also_like'){
            t = 'You Might Also Like'
        }
        else if (this.props.match.params.type == 'rated'){
            t = 'Rated Movies'
        }
        
        return<div>
            <h1 style={{'font-size':30}}>{t} </h1>
            <div style={{'height':20}}></div>
            { this.renderList()}
            
        </div>
    }


}
