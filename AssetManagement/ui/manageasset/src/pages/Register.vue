<template>
  <div class="login-wrapper">

    <!-- TOP HEADER -->
    <div class="login-header">
      <h1>Member Sign in</h1>
      <p>Create your account</p>
    </div>

    <div class="login-box">

      <label>Name</label>
      <input v-model="name" type="text" placeholder="Your full name">

      <label>Email Address</label>
      <input v-model="email" type="email" placeholder="Enter email">

      <label>Password</label>
      <input v-model="password" type="password" placeholder="Enter password">

      <button @click="register">
        Create Account
      </button>

      <p class="error" v-if="error">{{ error }}</p>

      <p class="switch">
        Already have an account?
        <a href="/login">Login</a>
      </p>
    </div>
  </div>
</template>

<script>
import { api } from "../api";

export default {
  data() {
    return {
      name: "",
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async register() {
      this.error = "";

      // Validation
      if (!this.name || !this.email || !this.password) {
        this.error = "Please fill in all fields";
        return;
      }

      try {
        // API call
        await api.post("/users/register/", {
          name: this.name,
          email: this.email,
          password: this.password
        });

        // 🔥 SUCCESS → Redirect to Admin Dashboard
        this.$router.push({ name: "AdminDash" });

      } catch (err) {
        this.error = err.response?.data?.detail || "Registration failed.";
      }
    }
  }
};
</script>

<style scoped>
/* SAME styling as login */
.login-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-header {
  width: 100%;
  padding: 50px 0;
  text-align: center;
  color: white;
  background: linear-gradient(90deg, #8a0f9a, #b81fb6);
}

.login-box {
  margin-top: -40px;
  width: 450px;
  background: white;
  padding: 35px;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 15px;
  color: #333;
}

input {
  margin-top: 5px;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

button {
  margin-top: 20px;
  background: #ffc82e;
  border: none;
  padding: 12px;
  font-size: 18px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

button:hover { background: #ffb900; }

.error { color: red; margin-top: 10px; }

.switch {
  margin-top: 15px;
  font-size: 14px;
}
</style>
