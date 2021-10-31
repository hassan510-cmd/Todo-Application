import React, { Component } from 'react'
import '../TodoStyle/bootstrap.min.css'
import TodoForm from './TodoForm'
import TodoHeader from './TodoHeader'
import TodoItem from './TodoItem'

export default class TodoParent extends Component {
    render() {
        return (
            <div className='container'>
                
                <TodoForm/>
                
            </div>
        )
    }
}
