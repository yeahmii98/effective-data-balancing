import useState from 'react';
import { Link } from 'react-router-dom';
import BoxData from '../containers/BoxData';

const BoxList = () => {
  // const [ex, setEx] = useState(false);
  // const

  return (
    <ul className="list-box">
      {BoxData.map((item, index) => {
        return (
          <li key={index} className={item.cName}>
            <Link to={item.path}>
              <div className="box-content">
                <strong style={{ fontSize: '2.5rem', color: '#B4B4B4' }}>{item.topic}</strong>
                <strong style={{ fontSize: '7.5rem' }}>{item.title}</strong>
              </div>
            </Link>
          </li>
        );
      })}
    </ul>
  );
};

export default BoxList;
