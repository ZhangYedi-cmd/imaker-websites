import Vue from "vue"
import Router from 'vue-router'
import {childrenRouters} from "./children";
import {tutor} from "./client/tutor";

Vue.use(Router)

const pubRouters = [
  {
    path: "*",
    redirect: "/home"
  },
  //导师纳新后台专用
  {
    path: '/tutor',

    redirect: "/tutor/index",
    component: () => import("../components/view/tutor/index"),
    children: [
      ...tutor
    ]
  },
  //首页
  {
    path: '/',
    component: () => import("../components/index"),
    redirect: "/home",
    children: [
      ...childrenRouters
    ]
  },
]

export default new Router({
  mode: "hash",
  routes: [
    ...pubRouters
  ]
})


// 重复跳转路由报错问题
const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
