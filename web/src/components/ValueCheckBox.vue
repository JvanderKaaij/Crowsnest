<template>
  <input type="checkbox" id="checkbox" v-model="my_value" v-on:change="signalChange"/>
</template>

<script>
    import axios from 'axios'
    export default {
      name: 'ValueCheckBox',
      components: {},
      props: ['value', 'value_endpoint_type', 'url', 'id'],
      methods:{
          signalChange: function(evt){
            var send_obj = {};
            send_obj["id"] = this.id;
            send_obj[this.value_endpoint_type] = this.my_value;
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
        this.my_value = this.value === 1; //I need to set the prop to the data, as props are immutable. Also need to check against an integer
      }
    }
</script>

<style scoped>

</style>