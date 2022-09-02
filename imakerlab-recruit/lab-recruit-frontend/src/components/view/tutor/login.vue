<template>
  <section>

    <!-- 登录 -->

    <div class="container">
      <div class="user singinBx">
        <div class="imgBx"><img src="../../../assets/images/2.jpg" alt=""></div>
        <div class="formBx">
          <form>
            <h2>创新实验室纳新管理系统</h2>
            <h2> 登录</h2>
            <input type="text" name="" placeholder="用户名" v-model="formData.username">
            <input type="password" name="" placeholder="密码" v-model="formData.password">
            <input type="button" name="" value="登录" @click="handleSubmit()">
            <p class="signup">没有账号？<a @click="topggleForm()">注册</a></p>
          </form>
        </div>
      </div>

      <!-- 注册 -->

      <div class="user singupBx">
        <div class="formBx">
          <form>
            <h2> 注册</h2>
            <input type="text" name="" placeholder="用户名" v-model="registerData.username">
            <input type="email" name="" placeholder="邮箱地址"  v-model="registerData.email">
            <input type="password" name="" placeholder="密码" v-model="registerData.password">
            <input type="password" name="" placeholder="qq号码" v-model="registerData.qq">
            <el-select v-model="registerData.campus" placeholder="选择校区" style="width: 100%;">
              <el-option
                v-for="item in campusList"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
            <el-select v-model="registerData.group" placeholder="选择组名" style="width: 100%;">
              <el-option
                v-for="item in groupList"
                :key="item.group_name"
                :label="item.group_name"
                :value="item.group_name">
              </el-option>
            </el-select>
            <br>

            <input type="button" name="" value="注册" @click="tutorRegister()">
            <p class="signup">已有账号？<a @click="topggleForm()">登录</a></p>
          </form>
        </div>
        <div class="imgBx"><img src="../../../assets/images/3.jpg" alt=""></div>
      </div>

    </div>
  </section>

</template>
<script>

  import $ from "jquery"
  import {login} from "../../../api/tutor/tutor";
  import {mapState, mapActions} from 'vuex'
  import {Notification} from "element-ui";
  import {getGroupList} from "../../../api/group/group";
  import {register} from "../../../api/tutor/tutor";
  export default {
    name: "login",
    data() {
      return {
        registerData: {
          username: '',
          password: '',
          email: '',
          campus: '',
          group : '',
          qq:''
        },
        formData: {
          username: '',
          password: '',

        },
        campusList: [
          {
            label: '河西校区',
            value: '河西校区',
          }, {
            label: '泰达校区',
            value: '泰达校区',
          }
        ],
        groupList: []
      }
    },
    computed: {
      ...mapState({
        token: status => status.user.token,
        username: status => status.user.username,
        uid: status => status.user.uid,
      })
    },

    methods: {
      ...mapActions([
        'Login'
      ]),
      async getGroupList() {
        const res = await getGroupList();
        this.groupList = res.group.tutor_list;
      },
       handleSubmit() {
        this.Login(this.formData).then(res => {});
      },
      async tutorRegister () {
        const res = await register(this.registerData);
        Notification.success("注册成功!")
      },
      checkToken() {
        if (this.token) {
          this.$router.push('/tutor/home');
          return false
        } else {
          return true
        }
      },
      init() {
        var res = this.checkToken()
        if (res) {
        }
        this.getGroupList();
      },
      topggleForm() {
        var container = document.querySelector('.container');
        container.classList.toggle('active');
      },

    },
    mounted() {
      this.init();
    }
  }


</script>
<style>
  @import "../../../styles/style.css";
</style>
