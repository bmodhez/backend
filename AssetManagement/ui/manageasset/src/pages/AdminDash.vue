<template>
  <div class="dashboard">

    <!-- SIDEBAR -->
    <aside class="sidebar">
      <h2 class="logo">Dashboard</h2>

      <button class="asset-btn">📦 Assets</button>

      <!-- LOGOUT BUTTON -->
      <button class="logout-btn" @click="logout">🚪 Logout</button>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="content">

      <div class="top-bar">
        <h1>Manage Assets</h1>
        <button class="add-btn" @click="startAdd">+ Add Asset</button>
      </div>

      <div class="table-header">
        <span>Image</span>
        <span>Name</span>
        <span>Description</span>
        <span>Price</span>
        <span>Stock</span>
        <span>Action</span>
      </div>

      <div class="table-row" v-for="asset in assets" :key="asset.id">
        <img :src="asset.image" class="row-img" />
        <span>{{ asset.name }}</span>
        <span>{{ asset.description }}</span>
        <span>₹{{ asset.price }}</span>
        <span class="stock">{{ asset.stock }}</span>

        <div class="row-actions">
          <button class="edit" @click="openEdit(asset)">✏️</button>
          <button class="delete" @click="deleteAsset(asset.id)">🗑</button>
        </div>
      </div>

      <!-- MODAL -->
      <div class="modal" v-if="showModal">
        <div class="modal-box">

          <h2>{{ selectedId ? "Edit Asset" : "Add Asset" }}</h2>

          <input v-model="form.name" placeholder="Name" />
          <input v-model="form.description" placeholder="Description" />
          <input v-model="form.price" type="number" placeholder="Price" />
          <input v-model="form.stock" type="number" placeholder="Stock" />

          <!-- FILE UPLOAD -->
          <input type="file" @change="handleImageUpload" />

          <div class="modal-actions">
            <button class="cancel" @click="showModal = false">Cancel</button>

            <button v-if="selectedId" class="save" @click="updateAsset">Update</button>
            <button v-else class="save" @click="addAsset">Add</button>
          </div>

        </div>
      </div>

    </main>
  </div>
</template>


<script>
import { api } from "../api";

export default {
  data() {
    return {
      assets: [],
      showModal: false,
      selectedId: null,

      form: {
        name: "",
        description: "",
        price: "",
        stock: "",
        image: null
      }
    };
  },

  mounted() {
    this.fetchAssets();
  },

  methods: {

    logout() {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      this.$router.push("/login");
    },

    handleImageUpload(event) {
      this.form.image = event.target.files[0];
    },

    async fetchAssets() {
      const res = await api.get("assets/");
      this.assets = res.data;
    },

    startAdd() {
      this.selectedId = null;
      this.form = {
        name: "",
        description: "",
        price: "",
        stock: "",
        image: null
      };
      this.showModal = true;
    },

    openEdit(asset) {
      this.selectedId = asset.id;
      this.form = { ...asset, image: null };
      this.showModal = true;
    },

    async addAsset() {
      const fd = new FormData();
      fd.append("name", this.form.name);
      fd.append("description", this.form.description);
      fd.append("price", this.form.price);
      fd.append("stock", this.form.stock);
      fd.append("image", this.form.image);
      console.log(fd,"Hello")

      await api.post("assets/", fd, {
        headers: { "Content-Type": "multipart/form-data" }
      });

      this.fetchAssets();
      this.showModal = false;
    },

    async updateAsset() {
      const fd = new FormData();
      fd.append("name", this.form.name);
      fd.append("description", this.form.description);
      fd.append("price", this.form.price);
      fd.append("stock", this.form.stock);

      if (this.form.image instanceof File) {
        fd.append("image", this.form.image);
      }

      await api.put(`assets/${this.selectedId}/`, fd, {
        headers: { "Content-Type": "multipart/form-data" }
      });

      this.fetchAssets();
      this.showModal = false;
    },

    async deleteAsset(id) {
      await api.delete(`assets/${id}/`);
      this.fetchAssets();
    }
  }
};
</script>

<style scoped>

html, body { margin: 0; padding: 0; height: 100%; width: 100%; overflow: hidden; background: #f4f4f4; }
* { margin: 0; padding: 0; box-sizing: border-box; }

.dashboard { display: flex; height: 100vh; width: 100vw; }

.sidebar { width: 260px; background: #1d1f27; color: white; padding: 20px; }

.logo { font-size: 22px; margin-bottom: 20px; }

.asset-btn { width: 100%; padding: 12px; background: #ffc82e; border: none; border-radius: 6px; font-weight: bold; }

.logout-btn {
  width: 100%;
  margin-top: 20px;
  padding: 12px;
  background: #e63946;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
}

.logout-btn:hover { background: #d62828; }

.content { flex: 1; margin-left: 260px; padding: 30px; background: #f4f4f4; overflow-y: auto; }

.top-bar { display: flex; justify-content: space-between; align-items: center; width: 100%; }

.add-btn { background: green; color: white; padding: 10px 15px; border-radius: 6px; border: none; }

.table-header, .table-row {
  width: 100%; display: grid; grid-template-columns: 120px 1fr 2fr 120px 100px 120px;
  padding: 12px; border-radius: 6px; margin-bottom: 10px;
}

.table-header { background: #333; color: white; font-weight: bold; }
.table-row { background: white; }

.row-img { width: 90px; height: 70px; object-fit: cover; border-radius: 6px; }
.stock { color: green; font-weight: bold; }

.row-actions { display: flex; gap: 10px; }
.edit { background: orange; padding: 6px 10px; border: none; border-radius: 4px; }
.delete { background: crimson; color: white; padding: 6px 10px; border: none; border-radius: 4px; }

.modal { position: fixed; inset: 0; background: rgba(0,0,0,0.5); display: grid; place-items: center; }

.modal-box { width: 300px; background: white; padding: 20px; border-radius: 8px; }
.modal-box input { width: 100%; padding: 10px; margin-bottom: 10px; }

.modal-actions { display: flex; justify-content: flex-end; gap: 10px; }
.save { background: green; color: white; padding: 8px 14px; border: none; }
.cancel { padding: 8px 14px; }
</style>
