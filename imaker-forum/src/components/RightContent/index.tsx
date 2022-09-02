import { Button, Col, Dropdown, Menu, Row } from 'antd';
import { Link, useModel } from 'umi';
import HeaderSearch from '../HeaderSearch';
import AvatarDropdown from './AvatarDropdown';
import React from 'react';
import styles from './index.less';
const GlobalHeaderRight: React.FC = () => {
  const { initialState } = useModel('@@initialState');

  if (!initialState || !initialState.settings) {
    return null;
  }

  const menu = (
    <Menu>
      <Menu.Item key="1">
        <Link to="/addQuestion" target="_blank">
          上传题目
        </Link>
      </Menu.Item>
      <Menu.Item key="2">
        <Link to="/addPaper" target="_blank">
          创建试卷
        </Link>
      </Menu.Item>
    </Menu>
  );

  return (
    <>
      <div
        style={{ display: 'flex' }}
      >
        <Row
          className={styles.row}
          gutter={
            {
              xs: 0,
              md: 30
            }
          }
          align={'middle'}
          justify={"center"}
        >
          <Col
            span={13}
            xs={
              {
                span: 10
              }
            }
          >
            <HeaderSearch placeholder={'全站搜索面试题目'} />
          </Col>

          <Col>
            <Dropdown overlay={menu} placement="bottomCenter">
              <Link to="/addQuestion" target="_blank">
                <Button
                  type="primary"
                  className="uploadDropdown"
                  style={{ marginLeft: 24, marginRight: 8 }}
                >
                  上传
                </Button>
              </Link>
            </Dropdown>
          </Col>

          <Col>
            <AvatarDropdown />
          </Col>
        </Row>
      </div>
    </>
  );
};
export default GlobalHeaderRight;
