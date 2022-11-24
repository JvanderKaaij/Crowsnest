<template>
  <div>STUDENTS</div>
    <div id="students-list">
      <table>
        <tr>
          <td>Name</td>
          <td>Email</td>
        </tr>
        <tr v-for="(item, index) in students">
          <td>{{item.name}}</td>
          <td>{{item.email}}</td>
          <td>{{item.comment}}</td>
        </tr>
      </table>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Students',
        components: {},
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
            })
      }
    }
</script>