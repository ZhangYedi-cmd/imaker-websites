import request from '@/utils/request';

/**
 * 当前登陆的用户
 * */
export const getCurrentUser = async () => {
  return request<API.BaseResponse<API.LoginResult>>('/api/user/current', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
};

/**
 * 账户密码登陆
 */
export const accountLogin = async (options?: { [key: string]: any }) => {
  return request<API.BaseResponse<API.LoginResult>>('/api/user/login', {
    method: 'POST',
    data: options,
    notCarryToken: true,
  });
};

/**
 * 微信用户登陆
 * */
export const captchaLogin = async (options?: { [key: string]: any }) => {
  return request<API.BaseResponse<API.LoginResult>>('/api/user/captchaLogin', {
    method: 'GET',
    params: options,
    notCarryToken: true,
  });
};

/**
 * 微信用户登陆
 * */
export const updateUserInfo = async (options?: { [key: string]: any }) => {
  return request<API.BaseResponse<API.LoginResult>>('/api/user/update', {
    method: 'POST',
    data: options,
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
};

export const logout = async () => {
  localStorage.removeItem('token');
};
