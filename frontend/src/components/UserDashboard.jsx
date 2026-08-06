import { useState, useEffect } from "react"
import Logout from "./Logout"

function UserDashboard({setView, userID}){

    const [userData, setUserData] = useState({})

    useEffect(()=>{
        fetch(`http://127.0.0.1:5000/userdata/${userID}`)
        .then(response => response.json())
        .then(data => {
            setUserData(data)
        })
    }, [])

    return(
        <>
            <Logout setView={setView}/>
            <h2>User Dashboard Component</h2>
            <h3>Welcome {userData.username}!</h3>
            <h5>Employee ID: {userData.id}</h5>
            <span>You have  tasks to complete</span>
        </>
    )
}

export default UserDashboard