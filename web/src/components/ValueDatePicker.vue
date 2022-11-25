<template>
        <datepicker v-model="my_value" @closed="signalChange" format="dd-MM-yyyy"></datepicker>
</template>

<script>
    import axios from 'axios'
    import Datepicker from 'vuejs3-datepicker';

    export default {
      name: 'ValueDatePicker',
      components: {Datepicker},
      props: ['value', 'value_endpoint_type', 'url', 'id'],
      methods:{
          signalChange: function(evt){
            this.datetime = new Date(this.my_value);
            var date = this.datetime.toJSON().split('T')[0]

            var send_obj = {};
            send_obj["id"] = this.id;
            send_obj[this.value_endpoint_type] = date;
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
        this.my_value = new Date(this.value);
      }
    }
</script>

<style scoped>

</style>


