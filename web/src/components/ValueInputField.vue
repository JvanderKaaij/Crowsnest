<template>
  <input type="text" class="val-input" id="field-name" name="field-name" v-model="my_value" v-on:change="signalChange">
</template>

<script>
    import axios from 'axios'
    export default {
      name: 'ValueInputField',
      components: {},
      props: ['value', 'value_endpoint_type', 'mutation', 'id'],
      methods:{
          signalChange: function(evt){
            this.$store.commit(this.mutation, {id:this.id, value_endpoint_type:this.value_endpoint_type, value:this.my_value});
          }
      },
      data () {
        return {
          my_value: null
        }
      },
      mounted(){
        this.my_value = this.value; //I need to set the prop to the data, as props are immutable
      }
    }
</script>

<style scoped>

</style>