<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="submitForm">
            <label for="username">Username:</label>
            <input type="text" v-model="username" required />
            <br/>
            <label for="password">Password:</label>
            <input type="password" v-model="password" required />
            <br/>
            <button type="submit">Login</button>
        </form>
        <p>{{ message }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            username: '',
            password: '',
            message: ''
        }
    },
    methods: {
        async submitForm() {
            try {
                const response = await axios.post('http://localhost:5000/login', {
                    username: this.username,
                    password: this.password
                });

                if (response.status === 200) {
                    this.message = response.data.message;
                } else {
                    this.message = 'An unexpected error occurred.';
                }
            } catch (error) {
                if (error.response) {
                    this.message = error.response.data.error;
                } else if (error.request) {
                    this.message = 'No response received.';
                } else {
                    this.message = 'Error preparing the request.';
                }
                console.error('Error:', error);
            }
        }
    }
};
</script>