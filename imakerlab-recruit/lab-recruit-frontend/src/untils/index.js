/**
 @Time    : 2021/9/25 13:03
 @Author  : ZhangYd -- Tust
 @Email   : 178320369@qq.com
 @File    : index.js
 */

import Vue from 'vue'
/**
 * 统一工具类
 * */


/**
 *  深拷贝
 */
const deepCloneObj = function (obj) {
  return JSON.parse(JSON.stringify(obj));
};


/**
 * localStore 处理
 * */

export const storeService = {
  setStore(key, value) {
    window.localStorage.setItem(key, value);
  },
  getStore(key) {
    window.localStorage.getItem(key);
  },
  delStore(key) {
    window.localStorage.removeItem(key);
  }
};

/**
 * 递归处理: 非空校验
 * 和深拷贝一样的思路
 * */
export const checkNotNull = function (params, cloneObj) {
  var cloneObj = cloneObj || {}
  for (let i in params) {
    if (typeof params[i] === 'object' && params[i] != null) {
      cloneObj[i] = params[i] instanceof Array ? [] : {};
      handleParams(params[i], cloneObj[i]);
    } else {
      if (obj[i] === null || obj[i] === '') {
        return false
      }
    }
  }
  return cloneObj
};


/**
 * 时间格式转换
 */
export const transformTimestamp = function (timestamp) {
  let a = new Date(timestamp).getTime();
  const date = new Date(a);
  const Y = date.getFullYear() + '-';
  const M = (date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1) + '-';
  const D = (date.getDate() < 10 ? '0' + date.getDate() : date.getDate()) + '  ';
  const h = (date.getHours() < 10 ? '0' + date.getHours() : date.getHours()) + ':';
  const m = (date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes());
  // const s = date.getSeconds(); // 秒
  const dateString = Y + M + D + h + m;
  // console.log('dateString', dateString); // > dateString 2021-07-06 14:23
  return dateString;
}

/**
 * 封装图片地址
 * */
export const buildImgUrl = function (uuid) {
  return baseURLImg + uuid;
};


/**
 * 弹窗相关
 * */
export const showDialog = function (dialog, obj) {
  if (obj) {
    this.currentObj = obj;
  }
  this.$data[dialog] = true;
};

/**
 * 清除信息
 * */
const clearInfo = function (obj) {
  this.$data[obj] = {};
};



Vue.prototype.$clearInfo = clearInfo;
