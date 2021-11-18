import React, { Component } from 'react'
import '../TodoStyle/bootstrap.min.css'
import '../TodoStyle/tasks.css'
import TodoItem from './TodoItem'
import axios from 'axios'
export default class TodoForm extends Component {

    constructor(props) {
        super(props)

        this.state = {
            task_title: '',
            task_description: '',
            data: []
        }
        this.url="http://127.0.0.1:8000"
    }



    HandelTaskForm = (event) => {
        this.setState({
            [event.target.name]:event.target.value
        })
    }


    componentDidMount(){
        axios.get(`${this.url}/tasks/hello-view/`).then(response=>{
            this.setState({
                data:response.data.Tasks
            })
        }).catch(error=>{
            console.log(error)
        })
    }



    AddTask=(e)=>{
        e.preventDefault()
        e.target.task_description.value=''
        e.target.task_title.value=''
        var send_data = {
            name: this.state.task_title,
            description: this.state.task_description,
        }
        axios.post(`${this.url}/tasks/hello-view/`,send_data).then(res=>{
            this.setState(prevState=>({
                data:[...prevState.data,res.data.message]
            }))
            console.log(res.data)
        })
    }

    UpdateDataAfterDelete=(pk)=>{
        const {data:current_data}=this.state
        console.log(current_data)
        for (var item of current_data){
            if (item.id == pk){
                console.log(item)
                current_data.splice(current_data.indexOf(item),1)
                console.log(current_data)
                this.setState({
                    data:[...current_data]
                })
            }
        }
    }


    render() {

        return (
            <div >

                <form onSubmit={this.AddTask}>
                    <div className="mb-3">
                        <label  className="form-label">Task Titles</label>
                        <input name='task_title' onChange={this.HandelTaskForm} type="text" className="form-control" id="task_title" placeholder="Task Title" />
                    </div>
                    <div className="mb-3">
                        <label  className="form-label">Task Breif</label>
                        <textarea name='task_description' onChange={this.HandelTaskForm} className="form-control" id="task_desc" rows="3" placeholder='Task Breif'></textarea>
                    </div>
                    
                    <button type='submit' className='btn btn-primary mb-3' onClick={this.add_task}>Add Task</button>
                </form>
                <div className="tasks">
                    {this.state.data.map((rec, index) =>
                        <TodoItem
                            key={index} // required
                            title={rec.name}
                            desc={rec.description}
                            pk={rec.id}
                            state={rec.state}
                            UpdateDataAfterDelete={this.UpdateDataAfterDelete}
                        
                        />
                    )}
                </div>

            </div>
        )
    }
}
