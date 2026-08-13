import { useState } from "react"

function DeleteConfirmation(){

    const [password, setPassword] = useState()

    function ConfirmDelete(e){
        e.preventDefault()
        console.log('Confirming task deletion')
        console.log(password)
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