import Login from "./components/Login"
import UserDashboard from "./components/UserDashboard"
import UserTasks from "./components/UserTasks"
import AssignedTasks from "./components/AssignedTasks"
import AssignTask from "./components/AssignTask"

import { useState } from "react"

function App(){

  const [view, setView] = useState('login')
  const [userID, setUserID] = useState(0)

  return(
    <>
      <h1>App</h1>
      {view == 'login' && <Login setUserID={setUserID} setView={setView}/>}
      {view == 'dashboard' && <UserDashboard setView={setView} userID={userID}/>}
      {view == 'usertasks' && <UserTasks userID={userID} setView={setView}/>}
      {view == 'assigntask' && <AssignTask userID={userID} setView={setView}/>}
    </>
  )
}

export default App