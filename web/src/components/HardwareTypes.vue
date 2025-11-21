<template>
    <div class="component-header">Hardware Types</div>
    <div id="hardware-type-list">
      <table>
        <tr>
          <td class="t-header">Name</td>
        </tr>
        <tr v-for="item in hardware_types">
          <td>{{item.name}}</td>
        </tr>
        <tr class="spacer"><td colspan="1"></td></tr>
        <tr class="new-header"><td colspan="1">Add New Hardware Type</td></tr>
        <tr>
            <td class="new">
                <input type="text" placeholder="name" class="val-input" v-model="name">
                <button @click="AddNew">Add</button>
            </td>
        </tr>
      </table>
    </div>
</template>

<script>
    import {mapState} from "vuex";

    export default {
      name: 'HardwareTypes',
      data () {
        return {
          name: null
        }
      },
      computed: {
          ...mapState(['hardware_types'])
      },
      methods: {
          AddNew(){
              this.$store.commit('AddHardwareType', {
                  data: {name: this.name},
                  success: () => {
                      this.name = null;
                      this.$store.dispatch('InitHardwareTypes');
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
  #hardware-type-list{
    margin-bottom: 60px;
  }
  .spacer{
    background-color: #f9ffff;
  }
  .new-header{
    background-color: var(--blue-yonder);
    color: var(--ghost-white);
  }
  .new{
    background-color: var(--blue-yonder);
    display: flex;
    gap: 10px;
  }
</style>
