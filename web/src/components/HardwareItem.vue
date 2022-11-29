<template>
    <td><ValueInputField :id=item.id mutation='EditHardware' value_endpoint_type="name"               :value=item.name /></td>
    <td><ValueInputField :id=item.id mutation='EditHardware' value_endpoint_type="identity"           :value=item.identity /></td>
    <td><ValueDatePicker :id=item.id mutation='EditHardware' value_endpoint_type="purchase_date"      :value=item.purchase_date /></td>
    <td><ValueInputField :id=item.id mutation='EditHardware' value_endpoint_type="comment"            :value=item.comment /></td>
    <td><ValueDropDown :id=item.id mutation='EditHardware' :map=students value_endpoint_type="student_id" :value=item.student_id /></td>
    <td><button @click="RemoveHardware(item)">Delete</button></td>
</template>

<script>
    import ValueInputField from './ValueInputField.vue'
    import ValueDatePicker from "./ValueDatePicker.vue";
    import ValueDropDown from "./ValueDropDown.vue";
    import {mapMutations, mapState} from "vuex";

    export default {
      name: 'HardwareItem',
      components: {ValueDropDown, ValueDatePicker, ValueInputField},
      props:['item'],
      computed: {
          ...mapState(['hardware', 'students'])
      },
      methods:{
        ...mapMutations(['RemoveHardware'])
      },
    }
</script>

<style scoped>
</style>