import { useState } from 'react';
import { Link } from 'react-router-dom';
import BoxData from '../containers/BoxData';

const BoxList = () => {
  const [hide, setHide] = useState(true);

  const Explain = (
    <div
      className="explain-coponent"
      onMouseEnter={() => {
        setHide(false);
      }}
      onMouseLeave={() => {
        setHide(true);
      }}
    >
      <div className="box-content explain">
        <strong className="explain-title">ABOUT</strong>
        <span>kakao Nibs는?</span>
        {!hide && (
          <span>
            (내용 추가)<br/>
            .<br/>
            .<br/>
            .<br/><br/>
            팀장 - 허지현<br/>
            팀원 - 김대건 임대호 조예림
          </span>
        )}
      </div>
    </div>
  );

  return (
    <ul className="list-box">
      {BoxData.map((item, index) => {
        return (
          <li key={index} className={item.cName}>
            {item.cName == 'box-component explain' ? (
              Explain
            ) : (
              <Link to={item.path}>
                <div className="box-content">
                  <span>{item.topic}</span>
                  <strong>{item.title}</strong>
                </div>
              </Link>
            )}
          </li>
        );
      })}
    </ul>
  );
};

export default BoxList;
