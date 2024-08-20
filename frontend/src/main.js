// 引入createApp用于创建应用
import { createApp } from 'vue';
// 引入App根组件
import App from './App.vue';
// 引入路由器
import router from  './router';

// 创建一个应用
const app = createApp(App);
//使用路由器
app.use(router)
//挂载整个应用到app容器中
app.mount('#app');

//main.js是入口文件，负责启动vue应用 它导入了 router 和 App.vue，并将它们注册到 Vue 实例上。
// router 是Vue Router 创建的实例，用于管理应用的路由。
