<template>
  <div class="component-header">Hardware Types</div>
  <div id="hardware-type-list">
    <table>
      <tr>
        <td class="t-header">Name</td>
        <td class="t-header">Description</td>
        <td class="t-header">Actions</td>
      </tr>
      <tr v-for="item in activeHardwareTypes" :key="item.id">
        <td><input type="text" class="val-input" v-model="item.name" @change="Update(item)"></td>
        <td><input type="text" class="val-input" v-model="item.description" @change="Update(item)"></td>
        <td>
          <button @click="RemoveHardwareType(item)">Delete</button>
        </td>
      </tr>
      <tr class="spacer">
        <td colspan="3"></td>
      </tr>
      <tr class="new-header">
        <td colspan="3">Add New Hardware Type</td>
      </tr>
      <tr>
        <td class="new">
          <input type="text" placeholder="name" class="val-input" v-model="name">
        </td>
        <td class="new">
          <input type="text" placeholder="description" class="val-input" v-model="description">
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
      description: null
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
    AddNew() {
      this.$store.commit('AddHardwareType', {
        data: {name: this.name, description: this.description},
        success: () => {
          this.name = null;
          this.description = null;
          this.$store.dispatch('InitHardwareTypes');
        },
        onError: (errors) => {
          console.log(errors);
        }
      })
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
