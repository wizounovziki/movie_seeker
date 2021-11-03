import React from 'react';
import MovieItem from './MovieItem.js'
class MovieList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {  }
    }
    componentDidMount(){
        console.log();
    }
    render() { 
    // return ( <div>MovieList---{this.props.match.params.type}</div> );
    return (<div>
        {this.state.movies.map((item,i)=>{
            return<MovieItem {...item} key={i}></MovieItem>
        })}
    </div>)
    }
}
 
export default MovieList;