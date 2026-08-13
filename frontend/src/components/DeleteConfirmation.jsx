import { useState } from "react"

function DeleteConfirmation({userID, deletingTask}){

    const [password, setPassword] = useState("")

    function ConfirmDelete(e){
        e.preventDefault()
        console.log(deletingTask)
        fetch(`http://127.0.0.1:5000/deletetask/${deletingTask}`,{
            method: 'DELETE',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'manager_password': password, 'user_id': userID})
        })  
        .then(response=>response.json())
        .then(data=>console.log(data))
    }

    return(
        <>
            <h3>Delete Confirmation Component</h3>
            <h4>Confirm Deletion with Manager Password</h4>
            <form onSubmit={ConfirmDelete}>
                <label htmlFor="password">Password: </label>
                <input type="password" id="password" value={password} onChange={(e)=>setPassword(e.target.value)}></input>
                <button type="submit">Confirm</button>
            </form>
        </>
    )
}

export default DeleteConfirmation