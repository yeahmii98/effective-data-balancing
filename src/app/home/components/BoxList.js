import { useState } from 'react';
import { Link } from 'react-router-dom';
import BoxData from '../containers/BoxData';

const BoxList = () => {
  const [hide, setHide] = useState(false);

  return (
    <ul className="list-box">
      {BoxData.map((item, index) => {
        return (
          <li key={index} className={item.cName}>
            <Link to={item.path}>
              <div className="box-content">
                <span>{item.topic}</span>
                <strong>{item.title}</strong>
              </div>
            </Link>
          </li>
        );
      })}
    </ul>
  );
};

export default BoxList;
