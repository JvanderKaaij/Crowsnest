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
    <div><AttributeItem :type="type" :attribute="GetPossibleAttribute(type.id)" :student="item"/></div>
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
            isMounted: false,
            name_error_msg:null,
            email_error_msg:null
        }
      },
      methods:{
        ...mapMutations(['RemoveStudent']),
         signalChange: function(evt){
            if(this.isMounted){
              this.$store.commit('EditStudent', {data:this.item, success:this.OnSuccess, onError:this.OnErrors});
            }
          },
          OnSuccess(){
            this.name_error_msg=null;
            this.email_error_msg=null;
          },
          OnErrors(errors) {
            Object.entries(errors).forEach((e) => {
              const [key, value] = e;
              const select = key + '_error_msg';
              this[select] = value[0];
            });
          },
          GetPossibleAttribute(type_id){
            return this.item?.attributes?.find(x => x.attribute_type_id === type_id);
          }
      },
      computed: {
          ...mapState(['students','attribute_types'])
      },
      created(){
      },
      mounted(){
        this.isMounted = true;
      }
    }
</script>

<style scoped>
  td {
    vertical-align: middle;
  }
</style>