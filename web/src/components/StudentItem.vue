<template>
  <td><input type="text" class="val-input" id="field-name" name="field-name" v-model="item.name" v-on:change="signalChange"></td>
  <td><input type="text" class="val-input" id="field-email" name="field-email" v-model="item.email" v-on:change="signalChange"></td>
  <td><datepicker v-model="item.start_date" @closed="signalChange" format="dd-MM-yyyy"></datepicker></td>
  <td><datepicker v-model="item.estimated_end_date" @closed="signalChange" format="dd-MM-yyyy"></datepicker></td>
  <td><input type="checkbox" id="checkbox" v-model="item.has_door_access" true-value="1" false-value="0" v-on:change="signalChange"/></td>
  <td><input type="checkbox" id="checkbox" v-model="item.has_git_access" true-value="1" false-value="0" v-on:change="signalChange"/></td>
  <td><input type="checkbox" id="checkbox" v-model="item.has_git_lfs_access" true-value="1" false-value="0" v-on:change="signalChange"/></td>
  <td><button @click="RemoveStudent(item)">Delete</button></td>
</template>

<script>
    import ValueInputField from './ValueInputField.vue'
    import ValueCheckBox from "./ValueCheckBox.vue";
    import ValueDatePicker from "./ValueDatePicker.vue";
    import Datepicker from 'vuejs3-datepicker';
    import {mapState, mapMutations} from "vuex"

    export default {
      name: 'StudentItem',
      components: {ValueCheckBox, ValueInputField, ValueDatePicker, Datepicker},
      props:['item','add'],
      methods:{
        ...mapMutations(['RemoveStudent']),
         signalChange: function(evt){
            this.$store.commit('EditStudent', {data:this.item});
          }
      },
      computed: {
          ...mapState(['students'])
      }
    }
</script>

<style scoped>

</style>