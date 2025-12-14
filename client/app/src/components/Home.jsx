import { useNavigate } from 'react-router-dom';


function Home(){
    const navigate = useNavigate()

    return <div>
        <h1>React-Django Learning app</h1>
        <button style={{marginRight: "20px"}} onClick={() => navigate('/login')}>LogIn</button>
          <button onClick={() => navigate('/register')}>Register</button>
    </div>
}

export default Home;