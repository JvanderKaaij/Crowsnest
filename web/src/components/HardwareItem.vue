<template>
    <td><input type="text" class="val-input" id="field-name" name="field-name" v-model="item.name"    v-on:change="signalChange"></td>
    <td><input type="text" class="val-input" id="field-identity" name="field-identity" v-model="item.identity"    v-on:change="signalChange"></td>
    <datepicker v-model="item.purchase_date" @closed="signalChange" format="dd-MM-yyyy"></datepicker>
    <td><input type="text" class="val-input" id="field-comment" name="field-identity" v-model="item.comment"    v-on:change="signalChange"></td>
    <td><ValueDropDown :id=item.id mutation='EditHardware' :map=students value_endpoint_type="student_id" :value=item.student_id /></td>
    <td><button @click="RemoveHardware(item)">Delete</button></td>
</template>

<script>
    import ValueInputField from './ValueInputField.vue'
    import ValueDatePicker from "./ValueDatePicker.vue";
    import ValueDropDown from "./ValueDropDown.vue";
    import Datepicker from 'vuejs3-datepicker';
    import {mapMutations, mapState} from "vuex";

    export default {
      name: 'HardwareItem',
      components: {ValueDropDown, ValueDatePicker, ValueInputField, Datepicker},
      props:['item'],
      computed: {
          ...mapState(['hardware', 'students'])
      },
      methods:{
        ...mapMutations(['RemoveHardware']),
        signalChange: function(evt){
          this.$store.commit('EditHardware', {data:this.item});
        }
      },
    }
</script>

<style scoped>
</style>