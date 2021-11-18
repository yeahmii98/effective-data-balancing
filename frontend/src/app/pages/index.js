import Detection from './components/Detection';
import Classification from './components/Classification';

const index = ({ info }) => {
  switch (info) {
    case 'detection':
      return <Detection />;
    case 'classification':
      return <Classification />;
  }
};

export default index;
