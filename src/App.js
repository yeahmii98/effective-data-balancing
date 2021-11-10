import { Routes, Route } from 'react-router-dom'; /* version 6 변경사항 유의 */
import Navigation from './app/navigation/index';
import Home from './app/home/index';
import './styles/sass/main.css';

function App() {
  return (
    <div className="main-layout">
      <Navigation />
      <div className="content">
        <Routes>
          <Route path="/" element={<Home />} exact />
          {/* <Route path="/Page" element={<Page />} /> */}
          {/* <Route path="/ToGithub" component={ToGithub} /> */}
          {/* <Route path="/About" component={About} /> */}
          {/* <Route path="/Contact" component={Contact} /> */}
        </Routes>
      </div>
    </div>
  );
}

export default App;
