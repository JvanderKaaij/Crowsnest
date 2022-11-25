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
          <td>{{item.name}}</td>
          <td>{{item.identity}}</td>
          <td>{{item.purchase_date}}</td>
          <td>{{item.comment}}</td>
          <td>{{item.lend_to_student.name}}</td>
        </tr>
      </table>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Hardware',
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

<style scoped>
  #hardware-list{

  }
</style>