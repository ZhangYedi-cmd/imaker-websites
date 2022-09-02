const tutorChildren = [
  {
    path: '/tutor/home/studentList',
    component: () => import("../../components/tutor/list/studentList"),
  },
  {
    path: '/tutor/home/tutorInfo',
    component: () => import("../../components/tutor/tutorInfo/tutorInfo"),
  },
  {
    path: '/tutor/home/overView',
    component: () => import("../../components/tutor/overView/overView"),
  },

  {
    path: '/tutor/home/tutorList',
    component: () => import("../../components/tutor/list/tutorList"),
  },
  {
    path: '/tutor/home/groupList',
    component: () => import("../../components/tutor/list/groupList"),
  },
  {
    path: '/tutor/home/batch',
    component: () => import("../../components/tutor/list/batch"),
  },

]

export const tutor = [
  {
    path: '/tutor/login',
    component: () => import("../../components/view/tutor/login")
  },
  {
    path: '/tutor/home',
    redirect: "/tutor/home/studentList",
    component: () => import("../../components/view/tutor/home"),
    // 后台页跳转子路由
    children: [...tutorChildren]
  },
]

