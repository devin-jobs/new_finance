
//创建一个路由器 并暴露出去

import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import MainPage from '@/views/MainPage.vue';

// 设置默认路由
const routes = [
  { path: '/', component: LoginPage }, // 默认路由设置为登录页面
  { path: '/main', component: MainPage },
];

// 创建路由器
const router = createRouter({
  history: createWebHistory(),
  routes, // 注意：这里不需要重复写 routes: [ ... ]
});

export default router;