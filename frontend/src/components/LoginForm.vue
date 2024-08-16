<template>
  <div class="login-container">
    <form @submit.prevent="handleSubmit">
      <h1>Login</h1>
      <div class="input-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="input-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async handleSubmit() {
      const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `username=${encodeURIComponent(this.username)}&password=${encodeURIComponent(this.password)}`
      });

      const result = await response.json();
      if (result.success) {
        alert(result.message);
        // 这里可以添加跳转到主界面的逻辑
      } else {
        alert(result.message);
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

form {
  border: 1px solid #ccc;
  padding: 20px;
  width: 300px;
}

.input-group {
  margin-bottom: 10px;
}
</style>