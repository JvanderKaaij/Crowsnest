<template>
  <td>
    <input type="text" class="val-input" id="field-name" name="field-name" v-model="item.name" v-on:change="signalChange">
    <div v-if='name_error_msg' class='error' ref="name_error">{{name_error_msg}}</div>
  </td>
  <td>
    <input type="text" class="val-input" id="field-email" name="field-email" v-model="item.email" v-on:change="signalChange">
    <div v-if='email_error_msg' class='error' ref="email_error">{{email_error_msg}}</div>
  </td>
  <td><datepicker v-model="item.start_date" @closed="signalChange" format="dd-MM-yyyy"></datepicker></td>
  <td><datepicker v-model="item.estimated_end_date" @closed="signalChange" format="dd-MM-yyyy"></datepicker></td>

  <td v-for="type in attribute_types">
    <div v-for="attribute in item.attributes">
         <div v-if="attribute.attribute_type_id === type.id "><AttributeItem :item="attribute"/></div>
    </div>
  </td>

  <td><button @click="RemoveStudent(item)">Delete</button></td>

</template>

<script>
    import Datepicker from 'vuejs3-datepicker';
    import {mapState, mapMutations, mapActions} from "vuex"
    import AttributeItem from "./AttributeItem.vue";

    export default {
      name: 'StudentItem',
      components: {Datepicker, AttributeItem},
      props:['item','add'],
      data(){
        return{
            name_error_msg:null,
            email_error_msg:null
        }
      },
      methods:{
        ...mapMutations(['RemoveStudent']),
         signalChange: function(evt){
            this.$store.commit('EditStudent', {data:this.item, success:this.OnSuccess, onError:this.OnErrors});
          },
          OnSuccess(){
            console.log("Success");
            this.name_error_msg=null;
            this.email_error_msg=null;
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
      computed: {
          ...mapState(['students','attribute_types'])
      }
    }
</script>

<style scoped>

</style>