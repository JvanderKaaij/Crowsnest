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
          <tr class="spacer"><td :colspan="getAttributeAmount()"></td></tr>
          <tr class="new-header" id="one"><td :colspan="getAttributeAmount()">Add New Student</td></tr>
          <tr><StudentNewItem :types="attribute_types"/></tr>
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
          getAttributeAmount() {
            return 6 + this.attribute_types?.length ?? 0;
          }
        },
        mounted() {
          this.$store.dispatch('InitAttributeTypes')
        }
    }
</script>

<style scoped>
  .new-header{
    background-color: var(--blue-yonder);
    color: var(--ghost-white);
  }
    .spacer{
    background-color: #f9ffff;
  }
</style>