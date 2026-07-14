function UserTasks(){

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

    return(
        <>
            <h2>User Tasks Component</h2>
            <div>
                {tasks.map((task, index)=>(
                    <div key={index}>
                        <span>Task Description: {task.Description}</span>
                        <br/>
                        <span>Task Deadline: {task.Deadline}</span>
                        <br/>
                        <span>Completion Status: {task.CompletionStatus}</span>
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