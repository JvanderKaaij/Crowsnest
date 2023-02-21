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
        <tr class="spacer"><td colspan="6"></td></tr>
        <tr class="new-header"><td colspan="6">Add New Hardware</td></tr>
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
    margin-bottom: 60px;
  }
  .spacer{
    background-color: #f9ffff;
  }
  .new-header{
    background-color: var(--blue-yonder);
    color: var(--ghost-white);
  }
</style>