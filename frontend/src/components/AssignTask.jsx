import { useState } from "react"

function AssignTask({setView, userID}){

    const [ownerID, setOwnerID] = useState(0)
    const [description, setDescription] = useState("")

    function toDashboard(){
        setView('dashboard')
    }

    function handleAssignTask(e){
        e.preventDefault()
        fetch(`http://127.0.0.1:5000/assigntask/${userID}`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"ownerID": ownerID, "description": description})
        })
        .then(response => response.json())
        .then(data => {
            if ('error' in data){
                console.log('There was an error')
            }
            else{
                console.log('Task successfully added')
                setOwnerID(0)
                setDescription("")
            }
        })
    }

    return(
        <>
            <h3>Assign Task Component</h3>
            <button onClick={toDashboard}>To Dashboard</button>
            <form onSubmit={handleAssignTask}>
                <label htmlFor="owner_id">Employee number: </label>
                <input type="number" id="owner_id" value={ownerID} onChange={(e)=>setOwnerID(e.target.value)}></input>
                <label htmlFor="description">Description: </label>
                <input type="text" id="description" value={description} onChange={(e)=>setDescription(e.target.value)}></input>
                <button type="submit">Submit</button>
            </form>
        </>
    )
}

export default AssignTask