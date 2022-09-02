import Footer from '@/components/Footer';
import { LockOutlined, QrcodeOutlined, UserOutlined } from '@ant-design/icons';
import { LoginForm, ProFormCheckbox, ProFormText } from '@ant-design/pro-components';
import { Alert, notification, Tabs, message, Row } from 'antd';
import React, { useState } from 'react';
import { FormattedMessage, useIntl } from 'umi';
import styles from './index.less';
import { accountLogin, captchaLogin } from '@/services/user';
import { history, useModel } from 'umi';

const LoginMessage: React.FC<{
  content: string;
}> = ({ content }) => (
  <Alert
    style={{
      marginBottom: 24,
    }}
    message={content}
    type="error"
    showIcon
  />
);

const Login: React.FC = () => {
  const [type, setType] = useState<string>('scan');
  const { initialState, setInitialState } = useModel('@@initialState');
  const intl = useIntl();
  // 根据token拿到用户的详细信息
  const fetchUserInfo = async () => {
    try {
      const { data } = await initialState?.fetchUserInfo?.();
      if (data) {
        await setInitialState((s) => ({ ...s, currentUser: data }));
      }
    } catch (e) {
      const defaultLoginFailureMessage = '登录失败，请重试！';
      message.error(defaultLoginFailureMessage);
    }
  };

  const handleSubmit = async (values: API.LoginParams) => {
    const login = type === 'account' ? accountLogin : captchaLogin;
    const { data }: API.BaseResponse<API.LoginResult> = await login(values);
    if (data) {
      const { token } = data;
      localStorage.setItem('token', token);
      notification.success({
        message: '登录成功🔥',
      });
      await fetchUserInfo();
      if (!history) return;
      const { query } = history.location;
      const { redirect } = query as {
        redirect: string;
      };
      history.push(redirect || '/');
      return;
    }
  };
  return (
    <div className={styles.container}>
      <div className={styles.content}>
        <LoginForm
          logo={<img alt="logo" src={require('@/assets/logo.png')} />}
          title="面试鸭"
          subTitle={intl.formatMessage({ id: 'pages.layouts.userLayout.title' })}
          initialValues={{
            autoLogin: true,
          }}
          onFinish={async (values) => {
            await handleSubmit(values as API.LoginParams);
          }}
        >
          <Tabs activeKey={type} onChange={setType}>
            <Tabs.TabPane
              key="account"
              tab={intl.formatMessage({
                id: 'pages.login.accountLogin.tab',
                defaultMessage: '账户密码登录',
              })}
            />
            <Tabs.TabPane
              key="scan"
              tab={intl.formatMessage({
                id: 'pages.login.scan.tab',
                defaultMessage: '账户密码登录',
              })}
            />
          </Tabs>
          {status === 'error' && (
            <LoginMessage
              content={intl.formatMessage({
                id: 'pages.login.accountLogin.errorMessage',
                defaultMessage: '账户或密码错误(admin/ant.design)',
              })}
            />
          )}
          {type === 'account' && (
            <>
              <ProFormText
                name="userAccount"
                fieldProps={{
                  size: 'large',
                  prefix: <UserOutlined className={styles.prefixIcon} />,
                }}
                placeholder={intl.formatMessage({
                  id: 'pages.login.username.placeholder',
                  defaultMessage: '账户名: admin or user',
                })}
                rules={[
                  {
                    required: true,
                    message: (
                      <FormattedMessage
                        id="pages.login.username.required"
                        defaultMessage="请输入账户名!"
                      />
                    ),
                  },
                ]}
              />
              <ProFormText.Password
                name="userPassword"
                fieldProps={{
                  size: 'large',
                  prefix: <LockOutlined className={styles.prefixIcon} />,
                }}
                placeholder={intl.formatMessage({
                  id: 'pages.login.password.placeholder',
                  defaultMessage: '密码: ant.design',
                })}
                rules={[
                  {
                    required: true,
                    message: (
                      <FormattedMessage
                        id="pages.login.password.required"
                        defaultMessage="请输入密码！"
                      />
                    ),
                  },
                ]}
              />
              <ProFormCheckbox noStyle name="autoLogin">
                <FormattedMessage id="pages.login.rememberMe" defaultMessage="自动登录" />
              </ProFormCheckbox>
              <a
                style={{
                  float: 'right',
                }}
              >
                <FormattedMessage id="pages.login.forgotPassword" defaultMessage="忘记密码" />
              </a>
            </>
          )}

          {type === 'scan' && (
            <>
              <Row justify={'center'} align={'middle'}>
                <img
                  src={require('@/assets/img.png')}
                  style={{
                    width: '260px',
                    height: '260px',
                    marginBottom: '2vh',
                  }}
                  className={styles.qrcode}
                  alt="关注公众号『 面试鸭 』登录"
                />
              </Row>

              <ProFormText
                name="captcha"
                fieldProps={{
                  size: 'large',
                  prefix: <QrcodeOutlined className={styles.prefixIcon} />,
                }}
                placeholder={intl.formatMessage({
                  id: 'pages.login.code.placeholder',
                  defaultMessage: '',
                })}
                rules={[
                  {
                    required: true,
                    message: (
                      <FormattedMessage
                        id="pages.login.username.required"
                        defaultMessage="请输入动态码!"
                      />
                    ),
                  },
                ]}
              />
            </>
          )}

          {status === 'error' && <LoginMessage content="验证码错误" />}
          <div
            style={{
              marginBottom: 24,
            }}
          ></div>
        </LoginForm>
      </div>
      <Footer />
    </div>
  );
};

export default Login;
