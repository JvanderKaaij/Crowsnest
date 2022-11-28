<template>
        <datepicker v-model="my_value" @closed="signalChange" format="dd-MM-yyyy"></datepicker>
</template>

<script>
    import axios from 'axios'
    import Datepicker from 'vuejs3-datepicker';

    export default {
      name: 'ValueDatePicker',
      components: {Datepicker},
      props: ['value', 'mutation', 'value_endpoint_type', 'url', 'id'],
      methods:{
          signalChange: function(evt){
            this.datetime = new Date(this.my_value);
            var date = this.datetime.toJSON().split('T')[0]
            this.$store.commit(this.mutation, {id:this.id, value_endpoint_type:this.value_endpoint_type, value:date});
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


