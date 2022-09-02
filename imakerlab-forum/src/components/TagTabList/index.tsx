import { Tabs } from 'antd';
import React from 'react';
import { EXTRA_TAG_LIST } from '@/constant/tabs';

const { TabPane } = Tabs;

interface tabsProps {
  activeKey: string;
  handleClick?: (key: string) => void;
}

const App: React.FC<tabsProps> = (props) => {
  const { activeKey, handleClick } = props;
  const allList = [...EXTRA_TAG_LIST];

  return (
    <>
      <Tabs defaultActiveKey={activeKey} onTabClick={handleClick} type="card">
        {allList.map((item, index) => {
          return <TabPane tab={item} key={index} />;
        })}
      </Tabs>
    </>
  );
};

export default App;
