//创建一个路由器 并暴露出去

import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import MainPage from '@/views/MainPage.vue';


const routes = [
  { path: '/', redirect: '/login' }, // 添加这一行来重定向根路径到 /login
  { path: '/login', component: LoginPage },
  { path: '/main', component: MainPage },
];


// 创建路由器
const router = createRouter({
  history: createWebHistory(),
  routes, // 注意：这里不需要重复写 routes: [ ... ]
});

// 添加全局前置守卫
router.beforeEach((to, from, next) => {
  const sessionToken = localStorage.getItem('sessionToken');

  // 只有在用户尝试从其他页面重新进入 /login 时才检查登录状态
  if (to.path === '/login' && from.path !== '/' && sessionToken) {
    next('/main'); // 已登录，重定向到 /main
  } else {
    next(); // 允许正常导航
  }
});

export default router;