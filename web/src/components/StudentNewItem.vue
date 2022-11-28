<template>
  <td class="new"><input type="text" class="val-input" id="field-name" name="field-name" v-model="name"></td>
  <td class="new"><input type="text" class="val-input" id="field-email" name="field-email" v-model="email"></td>
  <td class="new"><datepicker v-model="start_date" format="dd-MM-yyyy"></datepicker></td>
  <td class="new"><datepicker v-model="end_date" format="dd-MM-yyyy"></datepicker></td>
  <td class="new"><input type="checkbox" id="checkbox" v-model="has_door_access"/></td>
  <td class="new"><input type="checkbox" id="checkbox" v-model="has_git_access"/></td>
  <td class="new"><input type="checkbox" id="checkbox" v-model="has_git_lfs_access"/></td>
  <td class="new"><button @click="AddNew">Add</button></td>
</template>

<script>
    import Datepicker from 'vuejs3-datepicker';

    export default {
      name: 'StudentNewItem',
      components:{Datepicker},
      data () {
        return {
          name:null,
          email:null,
          start_date:null,
          end_date:null,
          has_door_access:false,
          has_git_access:false,
          has_git_lfs_access:false,
        }
      },
      methods:{
        AddNew(){
          this.datetime = new Date(this.start_date);
          var parsed_start_date = this.datetime.toJSON().split('T')[0]

          this.datetime = new Date(this.end_date);
          var parsed_end_date = this.datetime.toJSON().split('T')[0]

          this.$store.commit('AddStudent', {
            name:this.name,
            email:this.email,
            start_date:parsed_start_date,
            end_date:parsed_end_date,
            has_door_access:this.has_door_access? 1:0,
            has_git_access:this.has_git_access? 1:0,
            has_git_lfs_access:this.has_git_lfs_access? 1:0,
          });
        }
      }
    }
</script>

<style scoped>

</style>