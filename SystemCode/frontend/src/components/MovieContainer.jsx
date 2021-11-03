import React from 'react'
import { Layout, Menu} from 'antd';
import {HashRouter,Route,Link, Switch} from 'react-router-dom'
import MovieList from './MovieList.jsx';
import MovieDetail from './MovieDetail.jsx';
const { Content, Sider } = Layout;


export default class MovieContainer extends React.Component{
    constructor(props){
        super(props)
        this.state={
          login:false
        }
    }

    componentWillMount(){
      var tk = ''
      if (localStorage.getItem("token")) {
          //add token
          this.setState({login:true})
          console.log("yes")
          tk = localStorage.getItem("token");
      }

    }

    render(){
        console.log("rded")
        return <Layout className="site-layout-background" style={{height:"100%",backgroundColor:"#fff" }}>
        <Sider className="site-layout-background" width={200} style={{backgroundColor:"#fff"}}>
          <Menu
            mode="inline"
            // defaultSelectedKeys={[window.location.hash.split('/')[2]]}

            defaultSelectedKeys={['1']}
            style={{ height: '100%' }}
          >
           
              <Menu.Item key="1"><Link to="/movie/full_list/1">Full List</Link></Menu.Item>
              <Menu.Item key="2"><Link to="/movie/recommend/1">Popular Trendings</Link></Menu.Item>
              { this.state.login?<Menu.Item key="3"><Link to="/movie/also_like/1">You might also like</Link></Menu.Item>: null}
              { this.state.login?<Menu.Item key="4"><Link to="/movie/rated/1">Your rated list</Link></Menu.Item>: null}
              
          </Menu>
        </Sider>
        <Content style={{ padding:"10px"}}>
        <Switch>
          <Route exact path="/movie/detail/:id" component={MovieDetail}></Route>
          <Route exact path="/movie/:type/:page" component={MovieList}></Route>
          
              
        </Switch>
        {/* <Route path="/movie/:type/:page" component={MovieList}></Route> */}
        </Content>
      </Layout>

    }
}

