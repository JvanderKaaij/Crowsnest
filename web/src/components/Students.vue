<template>
  <div class="component-header">Students</div>
    <div id="students-list">
      <table>
        <tr>
          <td class="t-header">Name</td>
          <td class="t-header">Email</td>
          <td class="t-header">Start Date</td>
          <td class="t-header">End Date</td>
          <td v-for="type in attribute_types" class="t-header">{{type.name}}</td>
          <td class="t-header">Actions</td>
        </tr>
        <tr v-for="(item, index) in students">
          <StudentItem v-if=item.active :item="item"/>
        </tr>
          <StudentNewItem :types="attribute_types"/>
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
            ...mapState(['students', 'attribute_types'])
        },
        methods:{
            ...mapActions(["InitAttributeTypes"]),
        },
        mounted() {
          this.$store.dispatch('InitAttributeTypes')
        }
    }
</script>

<style scoped>

</style>