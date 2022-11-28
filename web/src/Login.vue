<template>
    <div id="login-page">
      Login:
       <div class="form-group">
         <input v-model="usernameLogin" type="username" class="form-control" placeholder="Username" required>
         <input v-model="passwordLogin" type="password" class="form-control" placeholder="Password" required>
         <input type="submit" class="btn btn-primary" @click="doLogin">
       </div>
    </div>
</template>

<script>
    import axios from 'axios'
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
              axios
                .post('http://localhost:8000/login', {
                  username: this.usernameLogin,
                  password: this.passwordLogin
                })
                .then(response => {
                  if(response.data == true){
                    console.log(response.data);
                    localStorage.logged_in = true;
                    this.$router.push('/')
                  }
                })
           }
        }
      }
    }
</script>