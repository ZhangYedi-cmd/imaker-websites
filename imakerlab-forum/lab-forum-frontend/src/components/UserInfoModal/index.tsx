import { Button, Form, Input, Modal, Radio, Image, Row, Col, notification } from 'antd';
import React, { useEffect } from 'react';
import { useModel } from '@@/plugin-model/useModel';
import { AVATAR_DEFAULT_URL } from '@/constant';
import { updateUserInfo } from '@/services/user';

interface userInfoModalProps {
  activeKey: boolean;
  setActiveKey: () => void;
  userInfo: API.CurrentUser;
}

const formItemLayout = {
  labelCol: {
    xs: {
      span: 4,
    },
  },
  wrapperCol: { span: 16 },
};

const UserInfoModal: React.FC<userInfoModalProps> = (props) => {
  const { activeKey, setActiveKey } = props;
  const { initialState } = useModel('@@initialState');
  const { currentUser } = initialState;
  const [form] = Form.useForm();

  const doUpdateUserInfo = async (values: API.CurrentUser) => {
    Object.keys(values).map((key) => {
      currentUser[key] = values[key];
    });
    const res = await updateUserInfo(currentUser);
    if (res) {
      notification.success({
        description: '您的用户信息已更新',
        message: '操作成功',
      });
      setActiveKey(!activeKey);
    }
    // console.log(2 ** 53 > currentUser.id)
    // console.log(currentUser);
  };

  useEffect(() => {
    if (activeKey) {
      if (!currentUser.id) {
        return;
      }
      form.setFieldsValue(currentUser);
    }
  }, [currentUser, activeKey]);

  return (
    <>
      <Modal
        title="修改信息"
        footer={null}
        visible={activeKey}
        destroyOnClose
        onCancel={() => setActiveKey(!activeKey)}
      >
        <Form
          style={{
            marginTop: 8,
          }}
          form={form}
          requiredMark={false}
          name="user"
          labelAlign="left"
          {...formItemLayout}
          scrollToFirstError
          onFinish={doUpdateUserInfo}
        >
          <Form.Item
            label="用户名"
            name="username"
            rules={[
              {
                required: true,
                message: '请输入昵称',
              },
            ]}
          >
            <Input maxLength={12} allowClear />
          </Form.Item>

          <Form.Item label="兴趣方向" name="direction">
            <Input maxLength={12} allowClear />
          </Form.Item>

          <Form.Item label="邮箱" name="email">
            <Input maxLength={20} allowClear />
          </Form.Item>

          <Form.Item label="简介" name="introduction">
            <Input placeholder="请填写个人简介" maxLength={40} allowClear />
          </Form.Item>

          <Form.Item label="性别" name="gender">
            <Radio.Group>
              <Radio value={1}>男</Radio>
              <Radio value={0}>女</Radio>
            </Radio.Group>
          </Form.Item>

          <Form.Item label="头像">
            <Image.PreviewGroup>
              <Image
                width={100}
                src={currentUser.avatarUrl ? currentUser.avatarUrl : AVATAR_DEFAULT_URL}
              />
            </Image.PreviewGroup>
          </Form.Item>

          <Form.Item
            style={{
              marginTop: 32,
            }}
          >
            <Row gutter={24} justify="end">
              <Col>
                <Button htmlType="reset" block onClick={() => setActiveKey(false)}>
                  取消
                </Button>
              </Col>
              <Col span={12}>
                <Button
                  type="primary"
                  htmlType="submit"
                  block
                  // loading={submitting}
                  // disabled={submitting}
                >
                  {/*{submitting ? '提交中' : '提交'}*/}
                  提交
                </Button>
              </Col>
            </Row>
          </Form.Item>
        </Form>
      </Modal>
    </>
  );
};

export default UserInfoModal;
