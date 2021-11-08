import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navigation from './app/navigation/index';
import Home from './app/home/Home';
import './styles/sass/main.css';

function App() {
  return (
    <Router>
      <Navigation />
      <Routes>
        <Route path="/" exact component={Home} />
        {/* <Route path="/ToGithub" component={ToGithub} /> */}
        {/* <Route path="/About" component={About} /> */}
        {/* <Route path="/Contact" component={Contact} /> */}
      </Routes>
    </Router>
  );
}

export default App;
