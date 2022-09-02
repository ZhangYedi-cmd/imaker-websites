import axios from "axios";
import {baseUrl} from "./config";
import {Notification} from 'element-ui';
import {tokenService} from "./token";
import {ignore_token_urls} from "./config";

function makeMap() {
  let list = {};
  ignore_token_urls.forEach(item => list[item] = true);
  return function (path) {
    return !!list[path] // 转换为布尔值
  }
}

let isIgnorePath = makeMap(); // 返回内置函数的内存地址

const services = axios.create({
  baseURL: baseUrl,
  responseType: "json",
  timeout: 5000,
  // 请求头
  headers: {},
})


services.interceptors.request.use(config => {
  let path = config.url;
  // 如果不是忽略请求的地址, 就将token放入请求头中
  if (!isIgnorePath(path)) {
    config.headers = {
      Authorization: tokenService.getToken()
    }
  }
  return config;
}, (error => {
  return Promise.reject(error);
}))


services.interceptors.response.use(res => {
  return new Promise((resolve, reject) => {
    if (res.data.code === '200') {
      // Notification.success(res.data.message);
    }
    if (res.data.code !== '200') {
      Notification.error(res.data.error_detail.message + "\n");
      // 抛错
      reject("后台报错" + res.data.error_detail.error);
    }
    resolve(res.data);
  })

}, error => {
  if (error && error.response) {
    console.log("报错了!!");
  }
  return Promise.reject(error);
})

export default services;
