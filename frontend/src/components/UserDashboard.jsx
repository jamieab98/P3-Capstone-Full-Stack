import { useState } from "react"

function UserDashboard(){

    const tasks = [
            {
                ID: 1,
                Description: 'Create the frontend template',
                Deadline: '7/20/2026',
                CompletionStatus: 'Incomplete',
                AssignedBy: '001'
            },
            {
                ID: 2,
                Description: 'Create the backend',
                Deadline: '8/2/2026',
                CompletionStatus: 'Incomplete',
                AssignedBy: '001'
            },
            {
                ID: 3,
                Description: 'Start the project',
                Deadline: '7/15/2026',
                CompletionStatus: 'Complete',
                AssignedBy: '001'
            }
        
    ]
    
    const userData = {
        Username: 'jamieab98',
        EmployeeID: '002',
        ManagerID: '001'
    }

    const incTasks = tasks.filter(t => t.CompletionStatus == 'Incomplete')    

    return(
        <>
            <h2>User Dashboard Component</h2>
            <h3>Welcome {userData.Username}!</h3>
            <h5>Employee ID: {userData.EmployeeID}</h5>
            <span>You have {incTasks.length} tasks to complete</span>
        </>
    )
}

export default UserDashboard