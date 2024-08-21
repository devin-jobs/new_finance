<!--侧边栏-->
<template>
  <aside class="sideBar">
    <ul>
      <li><router-link to="/">Login</router-link></li>
      <li><router-link to="/main">Main Page</router-link></li>
    </ul>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { path: '/home', text: '首页' },
        { path: '/settings', text: '设置' }
      ]
    };
  }
};
</script>

<style scoped>
.sideBar {
  position: absolute;
  left: 0;
  top: 64px; /* 顶部导航的高度 */
  bottom: 0;
  width: 200px;
  background-color: lightpink;
}
</style>
