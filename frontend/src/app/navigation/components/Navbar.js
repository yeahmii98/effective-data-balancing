import { useState } from 'react';
import * as AiIcons from 'react-icons/ai';
import { BsGridFill } from 'react-icons/bs';
import { IconContext } from 'react-icons'; /* 아이콘 컬러 전체 변경 기능 */
import { Link } from 'react-router-dom';
import SidebarData from '../containers/SidebarData';
import mainLogo from '../../../styles/images/main-logo.png';
import github from '../../../styles/images/github.png';

function Navbar() {
  const [sidebar, setSidebar] = useState(false);
  const showSidebar = () => setSidebar(!sidebar);

  return (
    <>
      {/* 아이콘 컬러 전체 변경 기능 */}
      <IconContext.Provider value={{ color: '#333' }}>
        {/* 네비게이션 토글 코드*/}
        <div className="navbar">
          <Link to="#" className="menu-bars">
            <BsGridFill onClick={showSidebar} />
          </Link>
          <img id="main-logo" src={mainLogo}></img>
          <img id="github" src={github}></img>
        </div>
      </IconContext.Provider>
      <IconContext.Provider value={{ color: '#FFF' }}>
        <nav className={sidebar ? 'nav-menu active' : 'nav-menu'}>
          <ul className="nav-menu-items" onClick={showSidebar}>
            <li className="navbar-toggle">
              <Link to="#" className="menu-bars">
                <AiIcons.AiOutlineClose />
              </Link>
            </li>
            {/* SidebarData를 순서대로 담기*/}
            {SidebarData.map((item, index) => {
              return (
                <li key={index} className={item.cName}>
                  <Link to={item.path}>
                    {item.icon}
                    <span style={{ marginLeft: '20px' }}>{item.title}</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Navbar;
