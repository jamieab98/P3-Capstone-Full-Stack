function AssignTask({setView}){

    function toDashboard(){
        setView('dashboard')
    }

    return(
        <>
            <h3>Assign Task Component</h3>
            <button onClick={toDashboard}>To Dashboard</button>
        </>
    )
}

export default AssignTask