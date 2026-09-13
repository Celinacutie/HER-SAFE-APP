     import { BrowserRouter, Routes, Route } from 'react-router-dom'
     import TrackingLoad from './TrackingLoad.jsx'

 function App() {
  return (
    <BrowserRouter>
      <div className="App">
       <h1>HER SAFE!</h1>
       <Routes>
                <Route path="/Tracking" element={<TrackingLoad />} />
                <Route path="/tracking.html" element={<TrackingLoad />} />
        {/* add your other pages here */}
      </Routes>
      </div>
    </BrowserRouter>
  )

    
      
   
  
}

export default App;