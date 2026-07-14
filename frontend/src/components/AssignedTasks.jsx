function AssignedTasks(){

    const userID = '001'

    const tasks = [
            {
                ID: 1,
                Description: 'Create the frontend template',
                Deadline: '7/20/2026',
                CompletionStatus: 'Incomplete',
                OwnerID: '003',
                AssignedBy: '001'
            },
            {
                ID: 2,
                Description: 'Create the backend',
                Deadline: '8/2/2026',
                CompletionStatus: 'Incomplete',
                OwnerID: '003',
                AssignedBy: '001'
            },
            {
                ID: 3,
                Description: 'Start the project',
                Deadline: '7/15/2026',
                CompletionStatus: 'Complete',
                OwnerID: '003',
                AssignedBy: '002'
            }    
    ]

    const assignedTasks = tasks.filter(t => t.AssignedBy == userID)

    return(
        <>
            <h2>Assigned Tasks Component</h2>
            <h4>Hello {userID}. Here are the tasks you've assinged.</h4>
            {assignedTasks.map((task, index)=>(
                <div key={task.ID}>
                    <span>Task Description: {task.Description}</span>
                    <br/>
                    <span>Task Status: {task.CompletionStatus}</span>
                    <br/>
                    <span>Task Deadline: {task.Deadline}</span>
                    <br/>
                    <span>Task Owner: {task.OwnerID}</span>
                    <br/>
                    <button>Edit Task</button>
                    <br/><br/>
                </div>
            ))}
        </>
    )
}

export default AssignedTasks