<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
  import {mapState} from 'vuex'

  export default {
    name: "index",
    computed: {
      ...mapState({
        token: status => status.user.token,
        username: status => status.user.username,
        uid: status => status.user.uid,
      })
    },
    methods: {
      // 初始化方法, 先看一下有没有token信息
      init() {
        if (this.token) {
          this.$router.push('/tutor/home');
        }
        this.$router.push('/tutor/login');
      }
    },
    watch: {
      token(val) {
        if (val === null) {
          this.$router.push('/tutor/login')
          return
        }
        this.$router.push('/tutor/home');
      }
    },
    created() {
      this.init();
    },
  }
</script>

<style >

</style>
