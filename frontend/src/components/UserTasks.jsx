import { useState, useEffect } from "react"

import Logout from "./Logout"

function UserTasks({setView, userID}){

    const [dailyTasks, setDailyTasks] = useState([])
    const [assignedTasks, setAssignedTasks] = useState([])

    useEffect(()=>{
        fetch(`http://127.0.0.1:5000/usertasks/${userID}`)
        .then(response => response.json())
        .then(data => {
            setDailyTasks(data.filter(task => "daily_task_description" in task))
            setAssignedTasks(data.filter(task => "assigned_task_description" in task))
        })
    }, [])

    return(
        <>
            <Logout setView={setView}/>
            <h2>User Tasks Component</h2>
            <div>
                <h3>Daily Tasks</h3>
                {dailyTasks.map((task, index)=>(
                    <div key={index}>
                        <span>Task Description: {task.daily_task_description}</span>
                        <br/>
                        <span>Task Deadline:</span>
                        <br/>
                        <span>Completion Status: </span>{task.completion_staus ? <span>Complete!</span> : <span>Incomplete</span>}
                        <br/>
                        <button>Change Completion Status</button>
                        <br/><br/>
                    </div>
                ))}
                <h3>Assigned Tasks</h3>
                {assignedTasks.map((task, index)=>(
                    <div key={index}>
                        <span>Task Description: {task.assigned_task_description}</span>
                        <br/>
                        <span>Task Deadline:</span>
                        <br/>
                        <span>Completion Status: </span>{task.completion_staus ? <span>Complete!</span> : <span>Incomplete</span>}
                        <br/>
                        <button>Change Completion Status</button>
                        <br/><br/>
                    </div>
                ))}
            </div>
        </>
    )
}

export default UserTasks