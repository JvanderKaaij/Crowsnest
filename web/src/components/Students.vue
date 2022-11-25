<template>
  <div class="component-header">Students</div>
    <div id="students-list">
      <table>
        <tr>
          <td class="t-header">Id</td>
          <td class="t-header">Name</td>
          <td class="t-header">Email</td>
          <td class="t-header">Start Date</td>
          <td class="t-header">End Date</td>
          <td class="t-header">Has Door Access</td>
          <td class="t-header">Has Git Access</td>
          <td class="t-header">Has Git LFS Access</td>
        </tr>
        <tr v-for="(item, index) in students">
          <td>{{item.id}}</td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="name"               :value=item.name /></td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="email"              :value=item.email /></td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="start_date"         :value=item.start_date /></td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="estimated_end_date" :value=item.estimated_end_date /></td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="has_door_access"    :value=item.has_door_access /></td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="has_git_access"     :value=item.has_git_access /></td>
          <td><ValueInputField :id=item.id url='/edit_student' value_endpoint_type="has_git_lfs_access" :value=item.has_git_lfs_access /></td>
        </tr>
      </table>
    </div>
</template>

<script>
    import axios from 'axios'
    import ValueInputField from './ValueInputField.vue'
    export default {
        name: 'Students',
        components: {ValueInputField},
        data () {
          return {
            students: null
          }
        },
      mounted(){
          axios
            .get('http://localhost:8000/students')
            .then(response => {
              this.students = response.data
              console.log(response.data)
            })
      }
    }
</script>

<style scoped>

</style>