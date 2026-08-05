import { useState } from "react"

function Login(){
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    function attemptLogin(e){
        e.preventDefault()
        fetch("http://127.0.0.1:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response=>response.json())
        .then(data=>console.log(data))
    }

    return(
        <>
            <h2>Login Component</h2>
            <form onSubmit={attemptLogin}>
                <label htmlFor="username">Username: </label>
                <input type="text" id="username" autoComplete="off" value={username} onChange={(e)=>setUsername(e.target.value)}></input>
                <label htmlFor="password">Password: </label>
                <input type="password" id="password" value={password} onChange={(e)=>setPassword(e.target.value)}></input>
                <button type="submit">Log In</button>
            </form>
        </>
    )
}

export default Login