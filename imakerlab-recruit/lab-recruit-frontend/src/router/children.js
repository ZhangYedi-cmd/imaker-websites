import {group} from "./client/group";
import {joinUs} from "./client/joinUs";
import {location} from "./client/location";


export const childrenRouters = [
  {
    path: '/home',
    component: () => import('@/components/view/student/home')
  },
  {
    path: "/group",
    redirect: "/group/c",
    component: () => import("@/components/view/student/group"),
    children: [
      // 组的子路由
      ...group
    ]
  },
  {
    path: "/joinUs",
    redirect: "/joinUs/form",
    component: () => import("@/components/view/student/joinUs"),
    children: [
      ...joinUs
    ]
  },
  {
    path: "/location",
    redirect: "/location/taida",
    component: () => import("@/components/view/student/location"),
    children: [
      ...location
    ]
  },

]
