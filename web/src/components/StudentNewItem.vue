<template>
  <tr class="new-item">
    <td class="new">
      <input type="text" class="val-input" id="name" name="field-name" v-model="name">
      <div v-if='name_error_msg' class='error' ref="name_error">{{name_error_msg}}</div>
    </td>
    <td class="new">
      <input type="text" class="val-input" id="email" name="field-email" v-model="email">
      <div v-if='email_error_msg' class='error' ref="email_error">{{email_error_msg}}</div>
    </td>
    <td class="new"><datepicker v-model="start_date" format="dd-MM-yyyy" @closed="StartDateChanged"></datepicker></td>
    <td class="new"><datepicker v-model="estimated_end_date" format="dd-MM-yyyy" @closed="EndDateChanged"></datepicker></td>
    <td class="new"><input type="checkbox" id="has_door_access" v-model="has_door_access"/></td>
    <td class="new"><input type="checkbox" id="has_git_access" v-model="has_git_access"/></td>
    <td class="new"><input type="checkbox" id="has_git_lfs_access" v-model="has_git_lfs_access"/></td>
    <td class="new"><button @click="AddNew">Add</button></td>
  </tr>
</template>

<script>
    import Datepicker from 'vuejs3-datepicker';
    import { ref } from 'vue';

    export default {
      name: 'StudentNewItem',
      components:{Datepicker},

      data () {
        return {
          inputRef:ref(null),
          name:null,
          email:null,
          start_date:"2020-1-1",
          estimated_end_date:"2020-1-1",
          has_door_access:false,
          has_git_access:false,
          has_git_lfs_access:false,
          name_error_msg:null,
          email_error_msg:null,
        }
      },
      methods:{
        StartDateChanged(){
          this.start_date = this.start_date.toJSON().split('T')[0]
        },
        EndDateChanged(){
          this.estimated_end_date = this.estimated_end_date.toJSON().split('T')[0]
        },
        AddNew(){
          this.$store.commit('AddStudent', {
            data:{
              name:this.name,
              email:this.email,
              start_date:this.start_date,
              estimated_end_date:this.estimated_end_date,
              has_door_access:this.has_door_access? 1:0,
              has_git_access:this.has_git_access? 1:0,
              has_git_lfs_access:this.has_git_lfs_access? 1:0,
              active:1
            },
            success:this.OnSuccess,
            onError:this.OnErrors
          });
        },
        OnSuccess(){
          this.name=null;
          this.email=null;
          this.start_date="2020-1-1";
          this.estimated_end_date="2020-1-1";
          this.has_door_access=false;
          this.has_git_access=false;
          this.has_git_lfs_access=false;
        },
        OnErrors(errors){
          Object.entries(errors).forEach((e)=>{
            const [key, value] = e;
            const select = key+'_error_msg';
            this[select] = value[0];
          });
        }
      }
    }
</script>

<style scoped>
  .error{
    color:white;
    max-width:150px;
    font-size:9pt;
    margin-top:2px;
    padding:2px;
    background-color: var(--orange-red-crayola);
  }
</style>