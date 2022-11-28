<template>
  <div class="component-header">Students</div>
    <div id="students-list">
      <table>
        <tr>
          <td class="t-header">Name</td>
          <td class="t-header">Email</td>
          <td class="t-header">Start Date</td>
          <td class="t-header">End Date</td>
          <td class="t-header">Has Door Access</td>
          <td class="t-header">Has Git Access</td>
          <td class="t-header">Has Git LFS Access</td>
        </tr>
        <tr v-for="(item, index) in students">
          <StudentItem :item="item"/>
        </tr>
        <button @click="AddNew">Add New</button>
      </table>

    </div>
</template>

<script>
    import { mapMutations, mapState, mapActions } from "vuex"
    import StudentItem from "./StudentItem.vue";
    export default {
        name: 'Students',
        components: {StudentItem},
        data () {
          return {

          }
        },
        computed: {
            ...mapState(['students'])
        },
        methods:{
          AddNew(){
            console.log("Add Student")
          }
        }
    }
</script>

<style scoped>

</style>