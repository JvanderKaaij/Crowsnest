<template>
    <div class="component-header">Hardware</div>
    <div id="hardware-list">
      <table>
        <tr>
          <td class="t-header">Name</td>
          <td class="t-header">Identity</td>
          <td class="t-header">Purchase date</td>
          <td class="t-header">Comment</td>
          <td class="t-header">Lend out to</td>
        </tr>
        <tr v-for="(item, index) in hardware">
          <HardwareItem :item="item"/>
        </tr>
        <button @click="AddNew">Add New</button>
      </table>
    </div>
</template>

<script>
    import HardwareItem from "./HardwareItem.vue";
    import {mapState} from "vuex";

    export default {
      name: 'Hardware',
      components: {HardwareItem},
      computed: {
          ...mapState(['hardware', 'students'])
      },
        methods:{
          AddNew(){
            console.log("Add Hardware")
          }
        }
    }
</script>

<style scoped>
  #hardware-list{

  }
</style>