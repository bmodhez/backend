<template>
  <div class="login-wrapper">

    <!-- TOP GRADIENT HEADER -->
    <div class="login-header">
      <h1>Member LOGIN</h1>
      <p>
        Login to your portal
        <br>
        Not a Member?
        <a class="signup-link" href="/register">Sign up today!</a>
      </p>
    </div>

    <!-- LOGIN BOX -->
    <div class="login-box">

      <label>Email Address</label>
      <input v-model="email" type="email" placeholder="Enter your email">

      <label>Password</label>
      <input v-model="password" type="password" placeholder="Enter password">

      <div class="remember">
        <input type="checkbox" v-model="remember">
        <span>Remember me on this computer</span>
      </div>

      <button @click="login">
        <span class="lock-icon">🔒</span> CONFIRM
      </button>

      <p class="error" v-if="error">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import { api } from "../api";

export default {
  data() {
    return {
      email: "",
      password: "",
      remember: false,
      error: "",
    };
  },
  methods: {
    async login() {
      this.error = "";
      
      
      if (!this.email || !this.password) {
        this.error = "Please fill in all fields";
        return;
      }

      try {
        const response = await api.post("/users/login/", {
          email: this.email,
          password: this.password
        });

        // Store tokens if needed
        if (response.data.access) {
          localStorage.setItem('access_token', response.data.access);
          if (response.data.refresh) {
            localStorage.setItem('refresh_token', response.data.refresh);
          }
        }

        // Redirect to dashboard
        this.$router.push({ name: "AdminDash" });

      } catch (err) {
  console.error("Login error:", err);

  if (err.code === 'ERR_NETWORK' || !err.response) {
    this.error = "Network Error: Backend server is not reachable";
    return;
  }

  this.error = "Invalid email or password";
}

    }
  },
};
</script>

<style scoped>


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

.login-header h1 {
  font-size: 36px;
  font-weight: 800;
  margin: 0;
}

.signup-link {
  color: #ffdf5e;
  font-weight: bold;
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
  font-size: 14px;
  color: #333;
}

input[type="email"],
input[type="password"] {
  margin-top: 5px;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 15px;
}

.remember {
  margin: 15px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* confirm button */
button {
  background: #ffc82e;
  border: none;
  padding: 12px;
  font-size: 18px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
}

button:hover {
  background: #ffb900;
}

.lock-icon {
  margin-right: 6px;
}

.error {
  margin-top: 10px;
  color: red;
}
</style>
