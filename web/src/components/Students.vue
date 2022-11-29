<template>
  <div class="component-header">Students</div>
    <div id="students-list">
      <table>
        <tr>
          <td class="t-header">Name</td>
          <td class="t-header">Email</td>
          <td class="t-header">Start Date</td>
          <td class="t-header">End Date</td>
          <td class="t-header">Door</td>
          <td class="t-header">Git</td>
          <td class="t-header">Git LFS</td>
          <td class="t-header">Actions</td>
        </tr>
        <tr v-for="(item, index) in students">
          <StudentItem v-if=item.active :item="item"/>
        </tr>
          <StudentNewItem/>
      </table>
    </div>
</template>

<script>
    import { mapMutations, mapState, mapActions } from "vuex"
    import StudentItem from "./StudentItem.vue";
    import StudentNewItem from "./StudentNewItem.vue";
    export default {
        name: 'Students',
        components: {StudentItem, StudentNewItem},
        data () {
          return {
            show_new:false
          }
        },
        computed: {
            ...mapState(['students'])
        }
    }
</script>

<style scoped>

</style>