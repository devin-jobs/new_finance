<!--<template>-->
<!--  <div id="app">-->
<!--    <header>-->
<!--      <router-link to="/login">Login</router-link>-->
<!--      <router-link to="/main">Main Page</router-link>-->
<!--    </header>-->
<!--    <router-view></router-view>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div id="app">
    <TopNavbar />
    <div class="container">
      <SideBar />
      <MainContent />
    </div>
  </div>
</template>


<script>
import {ref, onMounted} from 'vue';
import TopNavbar from '@/layouts/TopNavbar.vue';
import SideBar from '@/layouts/SideBar.vue';
import MainContent from '@/layouts/MainContent.vue';

export default {
  components: {
    TopNavbar,
    SideBar,
    MainContent
  },
  name: 'App',
  setup() {
    const isLoggedIn = ref(false);
    onMounted(() => {
      if (localStorage.getItem('sessionToken')) {
        isLoggedIn.value = true;
      }
    });
    return {
      isLoggedIn
    };
  }
};
</script>

<style scoped>
#app {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}
</style>