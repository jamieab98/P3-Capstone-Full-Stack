import { useState, useEffect } from "react"
import Logout from "./Logout"

function UserDashboard({setView, userID}){

    const [userData, setUserData] = useState({})
    const [incompleteTasks, setIncompleteTasks] = useState(0)

    useEffect(()=>{
        fetch(`http://127.0.0.1:5000/userdata/${userID}`)
        .then(response => response.json())
        .then(data => {
            setUserData(data)
            const incompleteAssigned = data.assigned_tasks.filter(task => task.completion_status == false).length
            setIncompleteTasks(incompleteAssigned)
        })
    }, [])

    function ViewTasks(){
        setView('usertasks')
    }

    function ViewAssignTask(){
        setView('assigntask')
    }

    return(
        <>
            <Logout setView={setView}/>
            <h2>User Dashboard Component</h2>
            <h3>Welcome {userData.username}!</h3>
            <button onClick={ViewAssignTask}>Assign Task</button><br/>
            <h5>Employee ID: {userData.id}</h5>
            <span>You have {incompleteTasks} tasks to complete</span>
            <button onClick={ViewTasks}>View Tasks</button>
        </>
    )
}

export default UserDashboard