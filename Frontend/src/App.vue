<template>
  <v-app style="background-color:#eee">
    <v-toolbar color="#FF9436" style="position:fixed; z-index:10000000" height="50px">
      <v-toolbar-title style="margin-left: 137px;">
        <router-link to="/" tag="span" style="cursor: pointer">
          <img style="padding:10px 0px 0px 0px;" src="./assets/sig_logo.png" width="100" height="80">
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items v-for="item in menuItems">
        <v-btn flat :key="item.title" :to="item.route">
          <v-icon left>{{ item.icon }}</v-icon>
          <div class="hidden-xs-only">{{ item.title }}</div>
        </v-btn>
      </v-toolbar-items>
        <v-btn flat style="margin-right: 30px;" disabled>
        </v-btn>
      <!--<v-toolbar-side-icon @click.native.stop="drawerToggle = !drawerToggle"></v-toolbar-side-icon>-->
    </v-toolbar> 
    <main style="margin-top:55px;">
      <router-view></router-view>
    </main>
  </v-app>

</template>

<script>
  export default {
    data () {
      return {
        drawerToggle: false
      }
    },
    computed: {
      menuItems () {
        let items = [
          { icon: 'face', title: 'Register', route: '/signup' },
          { icon: 'lock_open', title: 'Login', route: '/signin' }
        ]
        if (this.userIsAuthenticated) {
          items = [
            {icon: 'notifications', title: 'Alarm', route: '/alarm'},
            {icon: 'chat', title: 'Chat', route: '/chat'},
            {icon: 'account_circle', title: 'MyPage', route: '/mypage'}
            //{icon: 'chat', title: 'Logout', route: '/'},

          ]
        }
        return items
      },
      userIsAuthenticated () {
        // return "token" in localStorage
        return this.$store.getters.user !== null && this.$store.getters.user !== undefined || "token" in localStorage
      },
      onlineUsers () {
        console.log(this.$store.getters.onlineUsers)
        return this.$store.getters.onlineUsers
      }
    }
  }
</script>

