<template>
  <input type="text" class="val-input" id="field-name" name="field-name" v-model="my_value" v-on:change="signalChange">
</template>

<script>
    import axios from 'axios'
    export default {
      name: 'ValueInputField',
      components: {},
      props: ['value', 'value_endpoint_type', 'url', 'id'],
      methods:{
          signalChange: function(evt){
            var send_obj = {};
            send_obj["id"] = this.id;
            send_obj[this.value_endpoint_type] = this.my_value;

            console.log(send_obj)
            axios
              .post('http://localhost:8000'+this.url, send_obj)
              .then(response => {
                  console.log(response);
              })
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