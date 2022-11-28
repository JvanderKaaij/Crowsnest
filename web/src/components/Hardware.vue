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
          <td><ValueInputField :id=item.id mutation='EditHardware' value_endpoint_type="name"               :value=item.name /></td>
          <td><ValueInputField :id=item.id mutation='EditHardware' value_endpoint_type="identity"           :value=item.identity /></td>
          <td><ValueDatePicker :id=item.id mutation='EditHardware' value_endpoint_type="purchase_date"      :value=item.purchase_date /></td>
          <td><ValueInputField :id=item.id mutation='EditHardware' value_endpoint_type="comment"            :value=item.comment /></td>
          <td><ValueDropDown :id=item.id mutation='EditHardware' :map=students value_endpoint_type="student_id" :value=item.student_id /></td>
        </tr>
      </table>
    </div>
</template>

<script>
    import axios from 'axios'
    import ValueInputField from './ValueInputField.vue'
    import ValueDatePicker from "./ValueDatePicker.vue";
    import ValueDropDown from "./ValueDropDown.vue";
    import {mapState} from "vuex";

    export default {
      name: 'Hardware',
      components: {ValueDropDown, ValueDatePicker, ValueInputField},
      computed: {
          ...mapState(['hardware', 'students'])
      }
    }
</script>

<style scoped>
  #hardware-list{

  }
</style>