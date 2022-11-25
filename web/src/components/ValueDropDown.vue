<template>
  <select v-model="my_value" @change="signalChange">
    <option v-for="s in my_options"></option>


<!--    <option value="0">0</option>-->
<!--    <option value="1" selected>1</option>-->
<!--    <option value="2">2</option>-->
  </select>
</template>

<script>
    import axios from 'axios'
    export default {
      name: 'ValueDropDown',
      components: {},
      props: ['value', 'options', 'value_endpoint_type', 'url', 'id'],
      methods:{
          signalChange: function(evt){
            console.log("Select");
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
          my_value: null,
          my_options: null
        }
      },
      mounted(){
        this.my_value = this.value; //I need to set the prop to the data, as props are immutable. Also need to check against an integer
        this.my_options = this.options;
        console.log("test: ");
        console.log(this.options);
      }
    }
</script>

<style scoped>

</style>