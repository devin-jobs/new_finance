<!--顶部导航-->
<template>
  <nav class="top-nav">
    <div class="logo">个人理财</div>
    <ul class="nav-links">
      <li><router-link to="/main">Main Page</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/contact">Contact</router-link></li>
    </ul>
  </nav>
</template>

<script>
// export default {
//   data() {
//   }
// };
</script>

<style scoped>
.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: white;
  padding: 10px;
}

.logo {
  font-size: 1.5em;
  font-weight: bold;
}

.nav-links {
  display: flex;
  list-style-type: none;
  margin: 0;
  padding: 0;
  justify-content: center; /* 让子元素居中对齐 */

}

.nav-links li {
  margin: 0 10px; /* 添加左右边距来增加链接之间的间隔 */
}

.nav-links a {
  text-decoration: none;
  color: inherit;
}
</style>