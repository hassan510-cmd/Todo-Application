import React, { Component } from 'react'
import '../TodoStyle/bootstrap.min.css'
export default class TodoItem extends Component {


    render() {
        var style = this.props.state ?{textDecoration: 'line-through'} :{textDecoration: 'none'}
        return (

            <div className='mb-3'>
                <div className=" shadow p-1  bg-body rounded-3 border border-primary">
                    <div className="card-body">
                        
                        <h3 style={style} className="card-title">{this.props.title}</h3>
                        <p style={style} className="card-text">{this.props.desc}</p>
                         <span className='text-muted'>id {this.props.pk} state : {this.props.state}</span>  
                        <div className='task_action'>
                            <button className='btn btn-success ' onClick={()=>this.props.as_done(this.props.pk)}>{this.props.state?'undo':'Done'}</button>
                            <button className='btn btn-danger task_delete'  onClick={()=>this.props.del_task(this.props.pk)}>Delete</button>
                        </div>
                    </div>
                </div>
            </div>

        )
    }
}
