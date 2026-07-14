function Login(){

    return(
        <>
            <h2>Login Component</h2>
            <form>
                <label htmlFor="username">Username: </label>
                <input type="text" id="username" autoComplete="off"></input>
                <label htmlFor="password">Password: </label>
                <input type="password" id="password"></input>
                <button type="submit">Log In</button>
            </form>
        </>
    )
}

export default Login