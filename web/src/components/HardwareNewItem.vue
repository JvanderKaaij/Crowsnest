<template>
    <td class="new"><input type="text" class="val-input" id="field-name" name="field-name" v-model="name"></td>
    <td class="new"><input type="text" class="val-input" id="field-identity" name="field-name" v-model="identity"></td>
    <td class="new"><datepicker v-model="purchase_date" format="dd-MM-yyyy"></datepicker></td>
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
          purchase_date:null,
          comment:null,
          student_id:false
        }
      },
      computed: {
          ...mapState(['hardware', 'students'])
      },
      methods:{
        AddNew(){
          this.datetime = new Date(this.purchase_date);
          var parsed_purchase_date = this.datetime.toJSON().split('T')[0]

          this.$store.commit('AddHardware', {
            name:this.name,
            identity:this.identity,
            purchase_date:parsed_purchase_date,
            comment:this.comment,
            student_id:this.student_id,
          });
        }
      }
    }
</script>

<style scoped>
  #hardware-list{

  }
</style>