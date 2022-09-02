/**
 * reqsuest 网络请求工具
 * 更详细的 api 文档: https://github.com/umijs/umi-request
 */
import { extend } from 'umi-request';
import { notification } from 'antd';

const codeMessage = {
  200: '服务器成功返回请求的数据。',
  201: '新建或修改数据成功。',
  202: '一个请求已经进入后台排队（异步任务）。',
  204: '删除数据成功。',
  400: '发出的请求有错误，服务器没有进行新建或修改数据的操作。',
  401: '用户没有权限（令牌、用户名、密码错误）。',
  403: '用户得到授权，但是访问是被禁止的。',
  404: '发出的请求针对的是不存在的记录，服务器没有进行操作。',
  406: '请求的格式不可得。',
  410: '请求的题目被永久删除，且不会再得到的。',
  422: '当创建一个对象时，发生一个验证错误。',
  500: '服务器发生错误，请检查服务器。',
  502: '网关错误。',
  503: '服务不可用，服务器暂时过载或维护。',
  504: '网关超时。',
};

const errorHandler = (error: { response: Response; data: {} }): void => {
  const { response, data } = error;
  if (response && response.status) {
    const errorText = data['message'] || codeMessage[response.status];
    const { status, url } = response;
    notification.error({
      message: `请求错误 ${status}: ${url}`,
      description: errorText,
    });
  } else if (!response) {
    notification.error({
      description: '您的网络发生异常，无法连接服务器',
      message: '网络异常',
    });
  }
};

/**
 * 不需要token的url
 * */
// const notTokenUrl = ['/api/user/login', "/api/user/register"]

/**
 * 配置request请求时的默认参数
 */
const request = extend({
  errorHandler,
  // credentials: 'include', // 默认请求是否带上cookie
  prefix:
    process.env.NODE_ENV === 'production' ? 'http://www.yedizhang.work' : 'http://127.0.0.1:8024',

  // prefix: 'http://www.yedizhang.work',

  // requestType: 'form',
});

request.interceptors.request.use((url, options): any => {
  console.log(`do request url = ${url}`);
  // 默认携带token
  const cacheToken = !options.notCarryToken ? localStorage.getItem('token') : null;
  // const cacheToken = localStorage.getItem('token') ;
  return {
    url,
    options: {
      ...options,
      headers: {
        token: cacheToken,
      },
    },
  };
});

export default request;
