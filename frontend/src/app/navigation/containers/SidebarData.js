import * as BsIcons from 'react-icons/bs';

const SidebarData = [
  {
    title: 'Home',
    path: '/',
    icon: <BsIcons.BsFillHouseDoorFill />,
    cName: 'nav-text',
  },
  {
    title: 'Github',
    path: '/ToGithub',
    icon: <BsIcons.BsPersonBoundingBox />,
    cName: 'nav-text',
  },
  {
    title: 'About',
    path: '/About',
    icon: <BsIcons.BsFillInfoCircleFill />,
    cName: 'nav-text',
  },
  {
    title: 'Contact Us',
    path: '/Contact',
    icon: <BsIcons.BsEnvelopeFill />,
    cName: 'nav-text',
  },
];

export default SidebarData;
