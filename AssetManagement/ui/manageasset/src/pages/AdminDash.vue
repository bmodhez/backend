<template>
  <div class="dashboard">

    <!-- SIDEBAR -->
    <aside class="sidebar">
      <h2 class="logo">Dashboard</h2>
      <button class="asset-btn">📦 Assets</button>
    </aside>

    <!-- MAIN AREA -->
    <main class="content">

      <div class="top-bar">
        <h1>Manage Assets</h1>
        <button class="add-btn" @click="startAdd">+ Add Asset</button>
      </div>

      <!-- ✅ TABLE HEADER -->
      <div class="table-header">
        <span>Image</span>
        <span>Name</span>
        <span>Description</span>
        <span>Price</span>
        <span>Stock</span>
        <span>Action</span>
      </div>

      <!-- ✅ ASSET ROWS -->
      <div 
        class="table-row"
        v-for="asset in assets"
        :key="asset.id"
      >
        <img :src="asset.image" class="row-img"/>

        <span>{{ asset.name }}</span>
        <span>{{ asset.description }}</span>
        <span>₹{{ asset.price }}</span>
        <span class="stock">{{ asset.stock }}</span>

        <div class="row-actions">
          <button class="edit" @click="openEdit(asset)">✏️</button>
          <button class="delete" @click="deleteAsset(asset.id)">🗑</button>
        </div>
      </div>

      <!-- ✅ MODAL -->
      <div class="modal" v-if="showModal">
        <div class="modal-box">

          <h2>{{ selectedId ? "Edit Asset" : "Add Asset" }}</h2>

          <input v-model="form.name" placeholder="Name"/>
          <input v-model="form.desc" placeholder="Description"/>
          <input v-model="form.price" type="number" placeholder="Price"/>
          <input v-model="form.stock" type="number" placeholder="Stock"/>
          <input v-model="form.image" placeholder="Image URL (https://...jpg/png)"/>

          <div class="modal-actions">
            <button class="cancel" @click="showModal=false">Cancel</button>

            <button 
              v-if="selectedId" 
              class="save" 
              @click="updateAsset"
            >Update</button>

            <button 
              v-else 
              class="save" 
              @click="addAsset"
            >Add</button>
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
        desc: "",     // ✅ BACKEND KE SATH MATCH
        price: "",
        stock: "",
        image: ""
      }
    };
  },

  mounted() {
    this.fetchAssets();
  },

  methods: {
    async fetchAssets() {
      const res = await api.get("assets/");
      this.assets = res.data;
    },

    startAdd() {
      this.selectedId = null;
      this.form = {
        name: "",
        desc: "",
        price: "",
        stock: "",
        image: ""
      };
      this.showModal = true;
    },

    openEdit(asset) {
      this.selectedId = asset.id;
      this.form = { ...asset };
      this.showModal = true;
    },

    async updateAsset() {
      try {
        await api.put(`assets/${this.selectedId}/`, this.form);
        await this.fetchAssets();
        this.showModal = false;
      } catch (err) {
        alert("Update Failed");
        console.error(err);
      }
    },

    async addAsset() {
  try {
    await api.post("assets/", {
      name: this.form.name,
      desc: this.form.desc,
      price: this.form.price,
      stock: this.form.stock,
      image: this.form.image   // ✅ URL ONLY
    });

    await this.fetchAssets();
    this.showModal = false;

  } catch (err) {
    console.error("ADD ERROR:", err.response?.data || err);
    alert("Add Failed - Check Image URL & Fields");
  }
},

    async deleteAsset(id) {
      await api.delete(`assets/${id}/`);
      this.fetchAssets();
    }
  }
};
</script>



<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.dashboard {
  display: flex;
  width: 100vw;
  height: 100vh;
}

.sidebar {
  width: 260px;
  background: #1d1f27;
  color: white;
  padding: 20px;
}

.logo {
  font-size: 22px;
  margin-bottom: 20px;
}

.asset-btn {
  width: 100%;
  padding: 12px;
  background: #ffc82e;
  border: none;
  border-radius: 6px;
  font-weight: bold;
}

.content {
  flex: 1;
  padding: 25px;
  background: #f4f4f4;
  overflow-y: auto;
}

.top-bar {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.add-btn {
  background: green;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 6px;
}

/* ✅ TABLE HEADER */
.table-header {
  display: grid;
  grid-template-columns: 100px 1fr 2fr 120px 100px 120px;
  background: #333;
  color: white;
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 10px;
  font-weight: bold;
}

/* ✅ TABLE ROW */
.table-row {
  display: grid;
  grid-template-columns: 100px 1fr 2fr 120px 100px 120px;
  align-items: center;
  background: white;
  padding: 10px;
  border-radius: 6px;
  margin-bottom: 8px;
}

.row-img {
  width: 80px;
  height: 60px;
  object-fit: cover;
  border-radius: 6px;
}

.stock {
  color: green;
  font-weight: bold;
}

.row-actions {
  display: flex;
  gap: 8px;
}

.edit {
  background: orange;
  border: none;
  padding: 6px 10px;
}

.delete {
  background: crimson;
  color: white;
  border: none;
  padding: 6px 10px;
}

/* ✅ MODAL */
.modal {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  display: grid;
  place-items: center;
}

.modal-box {
  background: white;
  padding: 25px;
  width: 320px;
  border-radius: 8px;
}

.modal-box input {
  width: 100%;
  margin-bottom: 10px;
  padding: 8px;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.save {
  background: green;
  color: white;
  padding: 8px 14px;
  border: none;
}

.cancel {
  padding: 8px 14px;
}
</style>
