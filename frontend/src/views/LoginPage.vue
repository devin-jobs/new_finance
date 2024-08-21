<template>
  <div>
    <h1>LoginPage</h1>
    <form @submit.prevent="submitForm">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required />

      <label for="password">Password:</label>
      <input type="password" v-model="password" required />

      <button type="submit">LoginPage</button>
    </form>
    <p v-if="message" class="error">{{ message }}</p>
  </div>
</template>


<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';


export default {
  setup() {
    const username = ref('');
    const password = ref('');
    const message = ref('');
    const router = useRouter(); // 获取路由器实例

    function submitForm() {
      axios
        .post('http://localhost:5000/login', {
          username: username.value,
          password: password.value
        })
        .then(response => {
          if (response.status === 200 && response.data.token) {
            localStorage.setItem('sessionToken', response.data.token);
             router.push('/main'); // 使用路由器实例进行页面跳转
          } else {
            message.value = 'Invalid credentials';
          }
        })
        .catch(error => {
          message.value = error.response
            ? error.response.data.error
            : 'An unexpected error occurred.';
        });
    }


    return {
      username,
      password,
      message,
      submitForm
    };
  }
};
</script>

<style>
.error {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  max-width: 600px;
  width: 100%;
  margin: auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}


form label {
  margin-bottom: 10px;
  font-weight: bold;
}

form input {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form button {
  background-color: #007bff;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

form button:hover {
  background-color: #0056b3;
}
</style>