export default [
  {
    path: '/user',
    layout: false,
    routes: [
      {
        name: 'login',
        path: '/user/login',
        component: './user/Login',
      },
    ],
  },
  {
    path: '/',
    component: '../layouts/BasicLayout',
    routes: [
      {
        path: '/',
        component: '../pages/index/index',
      },
      {
        path: '/account',
        redirect: '/account/info',
      },
      {
        path: '/account/info',
        component: '../pages/userCenter/userInfo/index',
      },
      // {
      //   path: '/account',
      //   routes: [
      //     {
      //       path: '/account/info',
      //       component: '../pages/userCenter/userInfo/index'
      //     },
      //   ]
      // }
    ],
  },
];
