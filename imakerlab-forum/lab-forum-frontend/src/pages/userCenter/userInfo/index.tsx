import React, { useState } from 'react';
import { Avatar, Button, Row, Space, Tag, Typography } from 'antd';
import { Card } from 'antd';
import { AVATAR_DEFAULT_URL, DEFAULT_USER_NAME } from '@/constant';
import { EditOutlined } from '@ant-design/icons';
import styles from './index.less';
import { useModel } from '@@/plugin-model/useModel';
import UserInfoModal from '@/components/UserInfoModal';

const { Title } = Typography;

const UserInfo: React.FC = () => {
  const { initialState } = useModel('@@initialState');
  const { currentUser } = initialState;
  const [isModalVisible, setIsModalVisible] = useState(false);

  return (
    <>
      <div>
        <UserInfoModal
          activeKey={isModalVisible}
          userInfo={currentUser}
          setActiveKey={setIsModalVisible}
        />
        <Card>
          <Card.Meta
            title={
              <Space align="center">
                <Title level={4} style={{ marginBottom: 0 }}>
                  {currentUser.username ? currentUser.username : DEFAULT_USER_NAME}
                </Title>
                <Tag style={{ marginRight: 0, marginBottom: 3 }}>LV1</Tag>
              </Space>
            }
            avatar={
              <Avatar
                src={currentUser.avatarUrl ? currentUser.avatarUrl : AVATAR_DEFAULT_URL}
                size={96}
                // @ts-ignore
                onClick={() => {
                  // if (user._id === currentUser._id) {
                  //   setModalVisible(true);
                  // }
                  setIsModalVisible(!isModalVisible);
                }}
              />
            }
            description={'暂无描述'}
          ></Card.Meta>
        </Card>

        <Card
          style={{ marginTop: 17 }}
          className={styles.card}
          extra={
            <>
              <Button
                type="link"
                icon={<EditOutlined />}
                onClick={() => {
                  // if (user._id === currentUser._id) {
                  //   setModalVisible(true);
                  // }
                  setIsModalVisible(!isModalVisible);
                }}
              >
                编辑
              </Button>
            </>
          }
          title={<>个人信息</>}
        >
          <Row>年龄 ： 18</Row>
          <Row className={styles.info}>
            简介 ： {currentUser.introduction ? currentUser.introduction : '暂无'}
          </Row>
          <Row className={styles.info}>邮箱 : {currentUser.email ? currentUser.email : '暂无'}</Row>
          <Row className={styles.info}>
            兴趣方向 ： {currentUser.direction ? currentUser.direction : '暂无'}
          </Row>
          <Row className={styles.info}>注册时间 ： {currentUser.createTime.slice(0, 10)}</Row>
        </Card>
      </div>
    </>
  );
};

export default UserInfo;
