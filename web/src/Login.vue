<template>
    <div id="login-page">
      Login:
       <div class="form-group">
         <div class="center-group">
            <div class="container">
              <div class="grid-container">
                <div>Username</div>
                <div><input v-model="usernameLogin" type="username" class="form-control item-user" placeholder="Username" required></div>
                <div>Password</div>
                <div><input v-model="passwordLogin" type="password" class="form-control item-password" placeholder="Password" required></div>
              </div>
              <input type="submit" class="btn btn-primary" @click="doLogin">
            </div>
         </div>
       </div>
    </div>
</template>

<script>
    export default {
        name: 'Login',
        components: {},
        data () {
          return {
            usernameLogin: "",
            passwordLogin: "",
            emptyFields: false,
            validationError: false
          }
        },
      methods: {
        doLogin() {
           if (this.usernameLogin === "" || this.passwordLogin === "") {
              this.emptyFields = true;
           } else {
             this.$store.commit('Login', {data:{username:this.usernameLogin, password:this.passwordLogin}, success:this.OnSuccess});
           }
        },
        OnSuccess(response){
            localStorage.logged_in = true;
            this.$router.push('/app');
        },
      }
    }
</script>


<style scoped>

  .center-group{
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 100vh;
  }

  .grid-container{
     display: grid;
      grid-template-columns: [first] 50% [second] 50%;
      grid-template-rows: [row1] 50% [row2] 50%;
  }

  .btn{
    margin-top:20px;
  }

</style>