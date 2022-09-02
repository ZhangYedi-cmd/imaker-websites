import React, { useEffect, useState } from 'react';
import TagTabList from '@/components/TagTabList';
import { Avatar, Button, Card, Col, Divider, List, Row, Space, Tag, Typography } from 'antd';
import { RECOMMEND_TAG } from '@/constant/tabs';
import { QuestionType } from '@/models/question';
import { Link } from 'umi';
import QuestionItem from '@/components/Questions';

const { Title, Paragraph } = Typography;

/**
 * 排序方式
 */
const ORDERS = {
  RECOMMEND: '0',
  NEWEST: '1',
  GOOD: '2',
};

const QuestionsList: QuestionType[] = [
  {
    _id: '123123',
    name: 'Java为啥这么难呢？',
    detail: 'java 其实就不是人去学的',
    tags: ['java', 'Java之父', '八股文'],
  },
  {
    _id: '1112',
    name: '前端工程化？？',
    detail: 'java 其实就不是人去学的',
    tags: ['java'],
  },
  {
    _id: '1112',
    name: '前端工程化？？',
    detail: 'java 其实就不是人去学的',
    tags: ['java'],
  },
  {
    _id: '1112',
    name: '前端工程化？？',
    detail: 'java 其实就不是人去学的',
    tags: ['java'],
  },
  {
    _id: '1112',
    name: '前端工程化？？',
    detail: 'java 其实就不是人去学的',
    tags: ['java'],
  },
  {
    _id: '1112',
    name: '前端工程化？？',
    detail: 'java 其实就不是人去学的',
    tags: ['java'],
  },
];

const Index: React.FC = () => {
  const [activeTab, setActiveTab] = useState<string>(RECOMMEND_TAG);
  const [order, setOrder] = useState<string>(ORDERS.RECOMMEND);
  const [list, setList] = useState(QuestionsList);

  const loadData = () => {
    console.log('loadData!');
  };

  useEffect(() => {
    loadData();
  }, [activeTab, order]);

  const CardTabList = [
    {
      key: ORDERS.RECOMMEND,
      tab: '最热',
    },
    {
      key: ORDERS.NEWEST,
      tab: '最新',
    },
    {
      key: ORDERS.GOOD,
      tab: '精选',
    },
  ];

  const handleClickTab = (key: string): void => {
    setActiveTab(key);
  };

  return (
    <>
      <Col>
        <Row>
          <Col>
            <TagTabList activeKey={activeTab} handleClick={handleClickTab} />
          </Col>
        </Row>

        <Row gutter={[24, 24]}>
          <Col lg={18} style={{ width: '100%' }}>
            <Card
              tabList={CardTabList}
              onTabChange={(key: string): void => {
                setOrder(key);
              }}
              activeTabKey={order}
            >
              <List<QuestionType>
                rowKey="_id"
                itemLayout="vertical"
                dataSource={list} // 绑定list
                // 自定义渲染
                renderItem={(item) => {
                  return <QuestionItem question={item} />;
                }}
              ></List>
              <div
                style={{
                  textAlign: 'center',
                  margin: '20px 0',
                  columnSpan: 'all',
                }}
              >
                <Button type="primary">
                  <Link to="/" target="_blank">
                    <Space size={8}>查看更多</Space>
                  </Link>
                </Button>
              </div>
            </Card>
          </Col>

          <Col lg={6}>
            <Card title="关于本站" style={{ marginBottom: 16 }}>
              <Card.Meta
                avatar={<Avatar src="https://avatars.githubusercontent.com/u/79396379?v=4" />}
                description={
                  <div>
                    致力于收集面试题目与题解，提供一站式面试备战交流服务，助你成为面试达人！
                    <a href="https://t.1yb.co/yO1G" target="_blank" rel="noreferrer">
                      站长Yedi，全栈开发者。
                    </a>
                  </div>
                }
              ></Card.Meta>
            </Card>

            <Card title="公告栏" style={{ marginBottom: 16 }}>
              <Card.Meta description={<div>本站禁止一切测试行为！否则小黑屋处理</div>}></Card.Meta>
            </Card>

            <Card title="本月用户排行" style={{ marginBottom: 16 }}></Card>

            <Card style={{ marginBottom: 16 }}>业頔的知识库</Card>
          </Col>
        </Row>
      </Col>
    </>
  );
};

export default Index;
