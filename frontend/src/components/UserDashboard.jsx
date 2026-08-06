import { useState } from "react"
import Logout from "./Logout"

function UserDashboard({setView}){

    return(
        <>
            <Logout setView={setView}/>
            <h2>User Dashboard Component</h2>
            <h3>Welcome !</h3>
            <h5>Employee ID: </h5>
            <span>You have  tasks to complete</span>
        </>
    )
}

export default UserDashboard