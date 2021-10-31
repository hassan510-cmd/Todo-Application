import React, { Component } from 'react'
import '../TodoStyle/bootstrap.min.css'
import '../TodoStyle/tasks.css'
import TodoItem from './TodoItem'
import axios from 'axios'
export default class TodoForm extends Component {

    constructor(props) {
        super(props)

        this.state = {
            task_state: 0,
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

    // HandelTaskDescription = (event) => {
    //     this.setState({
    //         task_description: event.target.value
    //     })
    // }


//    async componentDidMount(){
//     var result= await axios.get("http://127.0.0.1:5000/tasks")
//     this.setState({
//         data:result.data.tasks
//     })
//     }


    componentDidMount(){
        axios.get(`${this.url}/tasks/hello-view/`).then(response=>{
            this.setState({
                data:response.data.Tasks
            })
        }).catch(error=>{
            console.log(error)
        })
    }
    // get_data = async () => {

    //     var url = "http://127.0.0.1:5000/tasks"
    //     var data = await fetch(url, {
    //         method: "GET"
    //     })
    //     var resobj = await data.json()
    //     var all_data = resobj.tasks
    //     this.setState({
    //         data: all_data
    //     })

    // }

    done_task = async (pk) => {

        var url = `http://127.0.0.1:5000/done-task/${pk}`
        var data = await fetch(url, {
            method: "GET"
        })
        var resobj = await data.json()
        var all_data = resobj.tasks

        this.setState({
            data: all_data
        })

    }
    // add_task = async () => {
    //     var url = `http://127.0.0.1:5000/add-task`
    //     var send_data = {
    //         name: this.state.task_title,
    //         description: this.state.task_description,
    //         state: 0
    //     }
    //     var data = await fetch(url, {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify(send_data)
    //     }
    //     )
    //     var result = await data.json()
    //     this.setState({
    //         data: [...this.state.data, result]
    //     })

    // }


    AddTask=(e)=>{
        e.preventDefault()
        e.target.task_description.value=''
        e.target.task_title.value=''
        var send_data = {
            name: this.state.task_title,
            description: this.state.task_description,
            state: 0
        }
        axios.post(`${this.url}/tasks/hello-view/`,send_data).then(res=>{
            this.setState(prevState=>({
                data:[...prevState.data,res.data.message]
            }))
            console.log(res.data)
        })
    }


    del_task_by_id = async (pk) => {

        var url = `http://127.0.0.1:5000/del-task/${pk}`
        var data_after = await fetch(url, {
            method: "DELETE"
        })
        var resobj = await data_after.json()
        var all_data = resobj.tasks

        this.setState({
            data: all_data
        })

    }

    as_done = () => {

        if (this.state.task_state) {
            this.setState({
                task_state: 0
            })
        }
        else {
            this.setState({
                task_state: 1
            })

        }
    }

    render() {

        return (
            <div >

                <form onSubmit={this.AddTask}>
                    <div className="mb-3">
                        <label  className="form-label">Task Title</label>
                        <input name='task_title' onChange={this.HandelTaskForm} type="text" className="form-control" id="task_title" placeholder="Task Title" />
                    </div>
                    <div className="mb-3">
                        <label  className="form-label">Task Breif</label>
                        <textarea name='task_description' onChange={this.HandelTaskForm} className="form-control" id="task_desc" rows="3" placeholder='Task Breif'></textarea>
                    </div>
                    {/* <button className='btn btn-primary mb-3' onClick={this.get_data}>fetch all</button> */}
                    {/* <button type='submit' className='btn btn-primary mb-3' onClick={this.add_task}>Add Task</button> */}
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
                            as_done={this.done_task}
                            del_task={this.del_task_by_id}
                        />
                    )}
                </div>

            </div>
        )
    }
}
