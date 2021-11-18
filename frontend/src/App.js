import { Routes, Route } from 'react-router-dom'; /* version 6 변경사항 유의 */
import Navigation from './app/navigation/index';
import Home from './app/home/index';
import ImgDetetion from './app/pages/index';
import ImgClassification from './app/pages/index';
import './styles/sass/main.css';

function App() {
  return (
    <div className="main-layout">
      <Navigation />
      <div className="content">
        <Routes>
          <Route path="/" element={<Home />} exact />
          <Route path="/imgDetection" element={<ImgDetetion info="detection"/>} />
          <Route path="/imgClassification" element={<ImgClassification info="classification"/>} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
