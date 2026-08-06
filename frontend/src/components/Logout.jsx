import { useState } from "react"

function Logout({setView}){

    function handleLogout(){
        setView('login')
    }

    return(
        <>
            <button onClick={handleLogout}>Log Out</button>
        </>
    )
}

export default Logout