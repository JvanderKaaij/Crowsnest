<template>
    <div id="app">
      <table>
        <tr>
          <td>Name</td>
          <td>Identity</td>
          <td>Comment</td>
        </tr>
        <tr v-for="(item, index) in hardware">
          <td>{{item.name}}</td>
          <td>{{item.identity}}</td>
          <td>{{item.comment}}</td>
        </tr>
      </table>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'App',
        components: {},
        data () {
          return {
            hardware: null
          }
        },
      mounted(){
          axios
            .get('http://localhost:8000/hardware')
            .then(response => {
              this.hardware = response.data
            })
      }
    }
</script>