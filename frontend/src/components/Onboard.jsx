function Onboard({userID, setView}){

    function ViewDashboard(){
        setView('dashboard')
    }

    return(
        <>
            <h3>Onboarding Component</h3>
            <button onClick={ViewDashboard}>To Dashboard</button>
        </>
    )
}

export default Onboard