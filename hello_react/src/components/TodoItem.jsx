import React, { Component } from 'react'
import '../TodoStyle/bootstrap.min.css'
import axios from 'axios'
export default class TodoItem extends Component {

    constructor(props) {
        super(props)
    
        this.state = {
            task_state:0,
            btn_state:'',
            text_style:"",
            task_style:{'display': 'block'},
            
        }
        this.url="http://127.0.0.1:8000"
    }
    
    ToggleTaskState = (pk) => {
        axios.patch(`${this.url}/tasks/list/${pk}/`).then(response=>{
            let new_state=response.data.message.state ? 0 :1
            this.setState({
                text_style:new_state ?{textDecoration: 'none'} :{textDecoration: 'line-through'},
                task_state:new_state,
                btn_state:new_state ?"Done" :"Undo"
            })
        })
        
    }

    DeleteTask=(pk)=>{
        axios.delete(`${this.url}/tasks/list/${pk}/`)
        this.setState({
            task_style:{'display': 'none'}
        })
    }


    componentWillMount=()=>{
        this.setState({
            text_style:this.props.state ?{textDecoration: 'line-through'} :{textDecoration: 'none'},
            btn_state:this.props.state ?"Undo" :"Done",
        })
      
        
    }
    
 
    render() {
        return (

            <div className='mb-3' style={this.state.task_style}>
                <div className=" shadow p-1  bg-body rounded-3 border border-primary">
                    <div className="card-body">
                        
                        <h3 style={this.state.text_style} className="card-title">{this.props.title}</h3>
                        <p style={this.state.text_style} className="card-text">{this.props.desc}</p>
                         <span className='text-muted'>id {this.props.pk} state : {this.state.task_state}</span>  
                        <div className='task_action'>
                            <button className='btn btn-success ' onClick={()=>this.ToggleTaskState(this.props.pk)}>{this.state.btn_state}</button>
                            <button className='btn btn-danger task_delete'  onClick={()=>this.DeleteTask(this.props.pk)}>Delete</button>
                        </div>
                    </div>
                </div>
            </div>

        )
    }
}
