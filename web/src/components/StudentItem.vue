<template>
  <td><ValueInputField :id=item.id mutation='EditStudents' value_endpoint_type="name" :value=item.name /></td>
  <td><ValueInputField :id=item.id mutation='EditStudents' value_endpoint_type="email" :value=item.email /></td>
  <td><ValueDatePicker :id=item.id mutation='EditStudents' value_endpoint_type="start_date" :value=item.start_date /></td>
  <td><ValueDatePicker :id=item.id mutation='EditStudents' value_endpoint_type="estimated_end_date" :value=item.estimated_end_date /></td>
  <td><ValueCheckBox   :id=item.id mutation='EditStudents' value_endpoint_type="has_door_access" :value=item.has_door_access /></td>
  <td><ValueCheckBox   :id=item.id mutation='EditStudents' value_endpoint_type="has_git_access" :value=item.has_git_access /></td>
  <td><ValueCheckBox   :id=item.id mutation='EditStudents' value_endpoint_type="has_git_lfs_access" :value=item.has_git_lfs_access /></td>
  <td><button @click="DeleteMe">Delete</button></td>
</template>

<script>
    import ValueInputField from './ValueInputField.vue'
    import ValueCheckBox from "./ValueCheckBox.vue";
    import ValueDatePicker from "./ValueDatePicker.vue";
    import {mapState, mapMutations} from "vuex"

    export default {
      name: 'StudentItem',
      components: {ValueCheckBox, ValueInputField, ValueDatePicker},
      props:['item','add'],
      computed: {
          ...mapState(['students'])
      },
      methods:{
        DeleteMe(){
          console.log("Delete me");
        }
      },
      mounted(){
        console.log(this.add);
      }
    }
</script>

<style scoped>

</style>