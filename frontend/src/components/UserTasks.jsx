import { useState, useEffect } from "react"
import DeleteConfirmation from "./DeleteConfirmation"

import Logout from "./Logout"

function UserTasks({setView, userID}){

    const [assignedTasks, setAssignedTasks] = useState([])
    const [deleting, setDeleting] = useState(false)
    const [deletingTask, setDeletingTask] = useState(0)

    useEffect(()=>{
        fetch(`http://127.0.0.1:5000/usertasks/${userID}`)
        .then(response => response.json())
        .then(data => {
            setAssignedTasks(data.filter(task => "assigned_task_description" in task))
        })
    }, [])

    function markComplete(id, type){
        fetch(`http://127.0.0.1:5000/changecompletion/${id}`, {
            method: "PATCH",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"type": type})
        })
        .then(response => response.json())
        .then(data => {
            return fetch(`http://127.0.0.1:5000/usertasks/${userID}`)
        })
        .then(response => response.json())
        .then(data => {
            setAssignedTasks(data.filter(task => "assigned_task_description" in task))
        })
    }

    function toDashboard(){
        setView('dashboard')
    }

    function DeleteTask(id){
        setDeleting(true)
        setDeletingTask(id)
    }

    return(
        <>
            <Logout setView={setView}/>
            <button onClick={()=>toDashboard()}>Back to Dashboard</button>
            <h2>User Tasks Component</h2>
            <div>
                <h3>Assigned Tasks</h3>
                {assignedTasks.map((task, index)=>(
                    <div key={index}>
                        <span>Task Description: {task.assigned_task_description}</span>
                        <br/>
                        <span>Task Deadline:</span>
                        <br/>
                        <span>Completion Status: </span>{task.completion_status ? <span>Complete!</span> : <span>Incomplete</span>}
                        <br/>
                        <button onClick={()=>markComplete(task.id, "assigned")}>Change Completion Status</button>
                        <br/>
                        <button onClick={()=>DeleteTask(task.id)}>Delete Task</button>
                        <br/><br/>
                    </div>
                ))}
            </div>
            {deleting == true && <DeleteConfirmation userID={userID} deletingTask={deletingTask} setDeleting={setDeleting}/>}
        </>
    )
}

export default UserTasks