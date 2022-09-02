/**
 * 用户账号管理(Vuex)
 * 导入已经封装好的api
 * 使用VueX封装 ==> 组件中使用
 * */
import {login, get_base_info} from "../../api/tutor/tutor";
import {tokenService} from "../../untils/token";
import ro from "element-ui/src/locale/lang/ro";

export const user = {
  state: {
    token: tokenService.getToken(),
    group: null,
    username: null,
    uid: null,
    roleType: null,
  },

  mutations: {
    SET_TOKEN(state, token) {
      state.token = token;
      tokenService.setToken(token);
    },
    SET_USERNAME(state, username) {
      state.username = username;
    },
    SET_GROUP(state, groupName) {
      state.group = groupName;
    },
    SET_UID(state, uid) {
      state.uid = uid;
    },
    DEL_TOKEN(state) {
      state.token = null
      tokenService.delToken();
    },
    SET_ROLE_TYPE(state, roleType) {
      console.log(roleType)
      state.roleType = roleType
    }
  },

  actions: {
    /**
     * 登录
     * */
    Login({commit}, userInfo) {
      return new Promise(((resolve, reject) => {
        login(userInfo).then(value => {
          if (value.token) {
            commit('SET_TOKEN', value.token);
            commit('SET_USERNAME', value.user_info.username);
            // commit('SET_UID', value.user_info.uid);
          }
        }).catch(error => {
          reject(error);
        })
      }))
    },
    Logout({commit}) {
      commit('DEL_TOKEN')
    },

    /**
     * 检查用户信息的接口
     * */
    Get_Tutor_Base_Info({commit}) {
      return new Promise((resolve, reject) => {
        get_base_info().then(value => {
          if (value.user_info) {
            let user_info = value.user_info;
            commit("SET_USERNAME", user_info.username);
            commit("SET_UID", user_info.uid);
            commit("SET_GROUP", user_info.group.group_name);
            commit("SET_ROLE_TYPE", user_info.roleType);
            resolve(value)
          }
        }).catch(error => {
          // 如果捕获到异常, 那么就清除token信息
          commit('DEL_TOKEN');
          reject(error);
        })
      })
    },
  }
}
