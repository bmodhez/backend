import { createRouter, createWebHistory } from "vue-router";

import Login from "./pages/Login.vue";
import Register from "./pages/Register.vue";
import AdminDash from "./pages/AdminDash.vue";   // 🔥 Dashboard page import

const routes = [
  {
    path: "/",
    redirect: "/login",
  },

  {
    path: "/login",
    name: "Login",
    component: Login,
  },

  {
    path: "/register",
    name: "Register",
    component: Register,
  },

  // 🔥 THIS ROUTE IS REQUIRED FOR REDIRECT
  {
    path: "/admin",
    name: "AdminDash",
    component: AdminDash,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
