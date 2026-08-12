import { useState } from "react"

function Onboard({userID, setView}){

    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [confirmPassword, setConfirmPassword] = useState("")

    function ViewDashboard(){
        setView('dashboard')
    }

    function CreateUser(e){
        e.preventDefault()
        fetch(`http://127.0.0.1:5000/createuser/${userID}`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"username": username, "password": password, "confirm_password": confirmPassword})
        })
        .then(response=>response.json())
        .then(data=>{
            if ('error' in data){
                console.log(data['error'])
            }
            else{
                console.log('User was successfully created!')
                setUsername('')
                setPassword('')
                setConfirmPassword('')
            }
        })
    }

    return(
        <>
            <h3>Onboarding Component</h3>
            <button onClick={ViewDashboard}>To Dashboard</button>
            <form onSubmit={CreateUser}>
                <label htmlFor="username">Username</label>
                <input type="text" id="username" value={username} onChange={(e)=>setUsername(e.target.value)}></input>
                <label htmlFor="password">Password</label>
                <input type="password" id="password" value={password} onChange={(e)=>setPassword(e.target.value)}></input>
                <label htmlFor="confirm_password">Confirm Password</label>
                <input type="password" id="confirm_password" value={confirmPassword} onChange={(e)=>setConfirmPassword(e.target.value)}></input>
                <button type="submit">Create User</button>
            </form>
        </>
    )
}

export default Onboard