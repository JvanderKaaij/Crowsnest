<template>
    <td>
      <input type="text" class="val-input" id="field-name" name="field-name" v-model="item.name"    v-on:change="signalChange">
      <div v-if='name_error_msg' class='error' ref="email_error">{{name_error_msg}}</div>
    </td>
    <td><input type="text" class="val-input" id="field-identity" name="field-identity" v-model="item.identity"    v-on:change="signalChange"></td>
    <td><datepicker v-model="item.purchase_date" @closed="signalChange" format="dd-MM-yyyy"></datepicker></td>
    <td><input type="text" class="val-input" id="field-comment" name="field-identity" v-model="item.comment"    v-on:change="signalChange"></td>
    <td>
      <select v-model="item.student_id" @change="signalChange">
        <option value="remove">{Remove User}</option>
        <option v-for="(stud, index) in GetActive" :value=stud.id >{{stud.name}}</option>
      </select>
    </td>
    <td><button @click="RemoveHardware(item)">Delete</button></td>
</template>

<script>
    import Datepicker from 'vuejs3-datepicker';
    import {mapMutations, mapState} from "vuex";

    export default {
      name: 'HardwareItem',
      components: {Datepicker},
      props:['item'],
      data(){
        return{
          name_error_msg:null
        }
      },
      computed: {
        ...mapState(['hardware', 'students']),
        GetActive() {
          return this.students.filter(x => x['active']);
        }
      },
      methods:{
        ...mapMutations(['RemoveHardware']),
        signalChange: function(evt){
          if(this.item.student_id === 'remove'){
            this.item.student_id = null;
          }
          this.$store.commit('EditHardware', {data:this.item, success:this.OnSuccess, onError:this.OnErrors});
        },
        OnSuccess(){
          console.log("Success");
          this.name_error_msg=null;
        },
        OnErrors(errors){
          console.log("Error");
          Object.entries(errors).forEach((e)=>{
            const [key, value] = e;
            const select = key+'_error_msg';
            this[select] = value[0];
          });
        }
      },
    }
</script>

<style scoped>
</style>