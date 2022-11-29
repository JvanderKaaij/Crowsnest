<template>
    <td class="new">
      <input type="text" class="val-input" id="field-name" name="field-name" v-model="name">
      <div v-if='name_error_msg' class='error' ref="email_error">{{name_error_msg}}</div>
    </td>
    <td class="new"><input type="text" class="val-input" id="field-identity" name="field-name" v-model="identity"></td>
    <td class="new"><datepicker v-model="purchase_date" format="dd-MM-yyyy" @closed="PurchaseDateChanged"></datepicker></td>
    <td class="new"><input type="text" class="val-input" id="field-comment" name="field-comment" v-model="comment"></td>
    <td class="new">
      <select v-model="student_id">
        <option v-for="(item, key) in students" :value=item.id>{{item.name}}</option>
      </select>
    </td>
    <td class="new"><button @click="AddNew">Add</button></td>
</template>

<script>
    import {mapState} from "vuex";
    import Datepicker from 'vuejs3-datepicker';

    export default {
      name: 'HardwareNewItem',
      components: {Datepicker},
      props:['item'],
      data () {
        return {
          name:null,
          identity:null,
          purchase_date:"2020-1-1",
          comment:null,
          student_id:null,
          name_error_msg:null
        }
      },
      computed: {
          ...mapState(['hardware', 'students'])
      },
      methods:{
        PurchaseDateChanged(){
          this.purchase_date = this.purchase_date.toJSON().split('T')[0]
        },
        AddNew(){
          this.$store.commit('AddHardware', {data:{
            name:this.name,
            identity:this.identity,
            purchase_date:this.purchase_date,
            comment:this.comment,
            active:1
          },
            success:this.OnSuccess,
            onError:this.OnErrors
          });
          if(this.student_id != null) data["student_id"] = this.student_id;
        },
        OnSuccess(){
          this.name = null;
          this.identity = null;
          this.purchase_date = "2020-1-1";
          this.comment = null;
          this.student_id = null;
          this.name_error_msg=null;
        },
        OnErrors(errors){
          console.log(errors);
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
  #hardware-list{

  }
</style>