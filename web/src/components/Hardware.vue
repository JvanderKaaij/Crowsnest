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
          <td class="t-header">Actions</td>
        </tr>
        <tr v-for="item in hardware">
          <HardwareItem v-if=item.active :item="item"/>
        </tr>
        <tr><HardwareNewItem/></tr>
      </table>
    </div>
</template>

<script>
    import HardwareItem from "./HardwareItem.vue";
    import HardwareNewItem from "./HardwareNewItem.vue";
    import {mapState} from "vuex";

    export default {
      name: 'Hardware',
      components: {HardwareItem, HardwareNewItem},
      computed: {
          ...mapState(['hardware'])
      }
    }
</script>

<style scoped>
  #hardware-list{

  }
</style>