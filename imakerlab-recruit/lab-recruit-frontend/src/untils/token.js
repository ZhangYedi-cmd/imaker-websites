// 使用window.localStorage 缓存token 信息
export const tokenService = {
  setToken(token) {
    window.localStorage.setItem('token', token);
  },
  getToken() {
    let token = window.localStorage.getItem('token');
    return token;
  },
  delToken() {
    window.localStorage.removeItem('token')
  }
}


