import { AUTH_SERVER_HOST_URL } from "@/settings";
import axios from 'axios'

const AuthModule = {
  state: {
    user: null
  },
  mutations: {
    setUser (state, payload) {
      state.user = payload

    //   const userListRef = firebase.database().ref('presence')
    //   const myUserRef = userListRef.push()

    //   firebase.database().ref('.info/connected')
    //     .on(
    //       'value', function (snap) {
    //         if (snap.val()) {
    //           // if we lose network then remove this user from the list
    //           myUserRef.onDisconnect()
    //             .remove()
    //           // set user's online status
    //           let presenceObject = {user: payload, status: 'online'}
    //           myUserRef.set(presenceObject)
    //         } else {
    //           // client has lost network
    //           let presenceObject = {user: payload, status: 'offline'}
    //           myUserRef.set(presenceObject)
    //         }
    //       }
    //     )
    }
  },
  actions: {
    signUserUp ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')

      axios.post(`${AUTH_SERVER_HOST_URL}/rest-auth/registration/`, {
        username: payload.username,
        password1: payload.password1,
        password2: payload.password2,
      }).then(res => {
          commit('setLoading', false)
          console.log('xxxxxx: ', res)
          localStorage.setItem("token", res.data.token);
          const newUser = {
            username: payload.username
          }
          commit('setUser', newUser)
      }).catch((ex)=>{
        console.log(ex)
        commit('setLoading', false)
        commit('setError', ex)
      })

    },
    signUserIn ({commit}, payload) {
      commit('setLoading', true)
      commit('clearError')

      
      axios.post(`${AUTH_SERVER_HOST_URL}/rest-auth/login/`, {
        username: payload.username,
        password: payload.password
      }).then(res => {
          commit('setLoading', false)
          console.log('xxxxxx: ', res)
          localStorage.setItem("token", res.data.token);
          const newUser = {
            username: payload.username
          }
          commit('setUser', newUser)
      }).catch((ex)=>{
        console.log(ex)
        commit('setLoading', false)
        commit('setError', ex)
      })
    }
  },
  getters: {
    user (state) {
      return state.user
    }
  }
}

export default AuthModule