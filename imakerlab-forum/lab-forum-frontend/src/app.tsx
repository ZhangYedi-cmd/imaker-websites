import type { Settings as LayoutSettings } from '@ant-design/pro-components';
import { PageLoading } from '@ant-design/pro-components';
import defaultSettings from '../config/defaultSettings';
import { RunTimeLayoutConfig } from '@@/plugin-layout/layoutExports';
import { getCurrentUser } from '@/services/user';
import { history } from 'umi';

/** 获取用户信息比较慢的时候会展示一个 loading */
export const initialStateConfig = {
  loading: <PageLoading />,
};

const loginPath = '/user/login';

const NO_NEED_LOGIN_WHITE_LIST = [loginPath];

/**
 * @see  https://umijs.org/zh-CN/plugins/plugin-initial-state
 * */
export async function getInitialState(): Promise<{
  settings?: Partial<LayoutSettings>;
  currentUser?: API.CurrentUser;
  loading?: boolean;
  fetchUserInfo?: () => Promise<API.CurrentUser | undefined>;
}> {
  // 获取当前用户信息
  const fetchUserInfo = async () => {
    try {
      return await getCurrentUser();
    } catch (e) {
      // 如果发生异常，则直接退回登录页面
      history.push(loginPath);
    }
    return undefined;
  };

  // 判断是否为要登陆的页面,如果不是，则直接返回
  if (NO_NEED_LOGIN_WHITE_LIST.includes(history.location.pathname)) {
    return {
      //@ts-ignore
      fetchUserInfo,
      settings: defaultSettings,
    };
  }
  // 如果是，调用借口获取信息，一并返回
  const currentUser = await fetchUserInfo();
  return {
    //@ts-ignore
    fetchUserInfo,
    currentUser,
    settings: defaultSettings,
  };
}

// ProLayout 支持的api https://procomponents.ant.design/components/layout
export const layout: RunTimeLayoutConfig = ({ initialState, setInitialState }) => {
  return {
    menuHeaderRender: undefined,
    headerRender: false,
    onPageChange: async () => {
      const { location } = history;
      if (NO_NEED_LOGIN_WHITE_LIST.includes(location.pathname)) {
        return;
      }
      // 如果没有登录，重定向到 login
      if (!initialState?.currentUser) {
        history.push(loginPath);
        return;
      }
      const { data } = await initialState?.fetchUserInfo?.();
      if (data) {
        await setInitialState((s) => ({ ...s, currentUser: data }));
      }
    },
  };
};
