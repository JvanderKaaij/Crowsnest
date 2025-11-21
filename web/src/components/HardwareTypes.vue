<template>
  <div class="component-header">Hardware Types</div>
  <div id="hardware-type-list">
    <table>
      <tr>
        <td class="t-header">Name</td>
        <td class="t-header">Description</td>
        <td class="t-header">Image</td>
        <td class="t-header">Actions</td>
      </tr>
      <tr v-for="item in activeHardwareTypes" :key="item.id">
        <td><input type="text" class="val-input" v-model="item.name" @change="Update(item)"></td>
        <td><input type="text" class="val-input" v-model="item.description" @change="Update(item)"></td>
        <td>
          <img v-if="item.image_url" :src="item.image_url" style="max-width: 100px; max-height: 100px;" />
          <input type="file" @change="UpdateImage(item, $event)" accept="image/*">
        </td>
        <td>
          <button @click="RemoveHardwareType(item)">Delete</button>
        </td>
      </tr>
      <tr class="spacer">
        <td colspan="4"></td>
      </tr>
      <tr class="new-header">
        <td colspan="4">Add New Hardware Type</td>
      </tr>
      <tr>
        <td class="new">
          <input type="text" placeholder="name" class="val-input" v-model="name">
        </td>
        <td class="new">
          <input type="text" placeholder="description" class="val-input" v-model="description">
        </td>
        <td class="new">
          <input type="file" ref="imageInput" @change="HandleImageUpload" accept="image/*">
        </td>
        <td class="new">
          <button @click="AddNew">Add</button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import {mapMutations, mapState} from "vuex";

export default {
  name: 'HardwareTypes',
  data() {
    return {
      name: null,
      description: null,
      imageFile: null
    }
  },
  computed: {
    ...mapState(['hardware_types']),
    activeHardwareTypes() {
      return this.hardware_types.filter(t => t.active);
    }
  },
  methods: {
    ...mapMutations(['RemoveHardwareType']),
    getImageUrl(typeId) {
      return `http://localhost:8047/hardware_type_image/${typeId}`;
    },
    HandleImageUpload(event) {
      this.imageFile = event.target.files[0];
    },
    AddNew() {
      const formData = new FormData();
      formData.append('name', this.name);
      formData.append('description', this.description);
      if (this.imageFile) {
        formData.append('image', this.imageFile);
      }
      
      this.$store.commit('AddHardwareType', {
        data: formData,
        success: () => {
          this.name = null;
          this.description = null;
          this.imageFile = null;
          if (this.$refs.imageInput) {
            this.$refs.imageInput.value = '';
          }
          this.$store.dispatch('InitHardwareTypes');
        },
        onError: (errors) => {
          console.log(errors);
        }
      })
    },
    UpdateImage(item, event) {
      const file = event.target.files[0];
      if (file) {
        const formData = new FormData();
        formData.append('id', item.id);
        formData.append('name', item.name);
        formData.append('description', item.description);
        formData.append('active', item.active);
        formData.append('image', file);
        
        this.$store.commit('EditHardwareType', {
          data: formData,
          success: () => {
            this.$store.dispatch('InitHardwareTypes');
          },
          onError: (errors) => {
            console.log(errors);
          }
        });
      }
    },
    Update(item) {
      this.$store.commit('EditHardwareType', {
        data: item,
        success: () => {
        },
        onError: (errors) => {
          console.log(errors);
        }
      })
    }
  }
}
</script>

<style scoped>
#hardware-type-list {
  margin-bottom: 60px;
}

.spacer {
  background-color: #f9ffff;
}

.new-header {
  background-color: var(--blue-yonder);
  color: var(--ghost-white);
}

.new {
  background-color: var(--blue-yonder);
}

td {
  vertical-align: middle;
}

</style>
