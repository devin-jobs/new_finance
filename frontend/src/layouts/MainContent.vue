<template>
  <div class="main-content">
    <router-view />
     <p>Hello, world! 这里的内容是MainContent组件写的</p>
  </div>
</template>
<script>
</script>

<style scoped>
.main-content {
  margin-left: 200px;
  height: calc(100vh - 64px); /* 减去顶部导航的高度 */
  overflow-y: auto;
}
</style>
