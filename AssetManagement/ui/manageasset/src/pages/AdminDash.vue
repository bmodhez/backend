<template>
  <div class="dashboard">

    <!-- SIDEBAR -->
    <aside class="sidebar">
      <h2 class="logo">Dashboard</h2>

      <nav class="menu">
        <a class="menu-item" :class="{ active: activeMenu === 'assets' }" @click="setActive('assets')">
          📦 Assets
        </a>
      </nav>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="content-area">
      <h1 class="page-title">
        {{ activeMenu === 'assets' ? "Manage Assets" : "" }}
      </h1>

      <!-- PAGE CONTENT CHANGES BASED ON MENU -->
      <div v-if="activeMenu === 'assets'" class="page-section">
        <p>Welcome to the Assets section. Asset tables and forms will come here.</p>
      </div>
    </main>

  </div>
</template>

<script>
export default {
  data() {
    return {
      activeMenu: "assets",
    };
  },
  methods: {
    setActive(menu) {
      this.activeMenu = menu;
    }
  }
};
</script>

<style scoped>

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}


/* Main layout */
.dashboard {
  display: flex;
  min-height: 100vh;     /* Full dynamic page height */
  height: auto;          /* expands according to content */
  background: #f4f4f4;
}

/* Sidebar */
.sidebar {
  width: 240px;
  background: #1d1f27;
  color: white;
  padding: 25px 20px;
  display: flex;
  flex-direction: column;
}

.logo {
  margin-bottom: 25px;
  font-size: 22px;
  font-weight: bold;
}

/* Sidebar Menu */
.menu {
  display: flex;
  flex-direction: column;
}

.menu-item {
  padding: 12px 14px;
  margin-bottom: 10px;
  background: #2a2d36;
  border-radius: 6px;
  cursor: pointer;
  color: #ddd;
  text-decoration: none;
  transition: 0.2s;
}

.menu-item:hover {
  background: #383c47;
}

.menu-item.active {
  background: #ffc82e;
  color: black;
  font-weight: 600;
}

/* Main Content */
.content-area {
  flex: 1;
  padding: 30px;
}

.page-title {
  font-size: 26px;
  font-weight: bold;
  margin-bottom: 25px;
}

.page-section {
  background: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
}
</style>
