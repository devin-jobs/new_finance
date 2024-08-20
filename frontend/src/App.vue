<template>
  <div id="app">
    <header>
      <router-link to="/">Login</router-link>
      <router-link to="/main">Main Page</router-link>
    </header>
    <router-view></router-view>
  </div>
</template>

<script>
import {ref, onMounted} from 'vue';

export default {
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