<template>
    <div id="login-page">
       <div class="form-group">
         <div class="center-group">
            <div class="container">
              <div class="input-container">

                <span class="login-header">Login</span>

                <span class="input-item">
                  <span class="input-label">Username:</span>
                  <span><input v-model="usernameLogin" type="username" class="form-control item-user" placeholder="Username" required></span>
                </span>
                <span class="input-item">
                  <span class="input-label">Password:</span>
                  <span><input v-model="passwordLogin" type="password" class="form-control item-password" placeholder="Password" required></span>
                </span>
              </div>
              <div v-if='validationError' class='error login-error' ref="login-error">username or password not correct</div>
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
             this.$store.commit('Login', {data:{username:this.usernameLogin, password:this.passwordLogin}, success:this.OnSuccess, error:this.OnError});
           }
        },
        OnSuccess(response){
          localStorage.logged_in = true;
          this.$router.push('/app');
        },
        OnError(response){
          this.validationError = true;
          console.log("login error here");
        }
      }
    }
</script>

<style scoped>

  .center-group{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 100vh;
  }

  .login-header{
    margin-bottom: 20px;
  }

  .input-container{
    display: flex;
    flex-direction: column;
  }

  .input-item{
    margin-bottom: 10px;
  }

  .input-label{
    display: inline-block;
    min-width: 110px;
    text-align: right;
    padding-right:10px;
  }

  .btn{
    margin-top:20px;
  }

  .login-error{
    max-width:100%;
  }

</style>