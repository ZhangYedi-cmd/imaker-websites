<template>
  <el-row type="flex" style="min-height: 100vh" v-if="!loading">
    <el-col :span="4" v-bind:class="{show: sideClassList.show,hide: sideClassList.hide}" class="side_bar">
      <el-menu
        :default-active="$route.path"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
        @select="goPage"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b">
        <el-row type="flex" justify="center">
          <img style="height: 100px; width:100px; border-radius: 50% " src="../../../assets/images/bilibili.png"/>
        </el-row>
        <el-row>
          <el-row type="flex" justify="center" style="margin-top: 25px;margin-bottom: 25px">
            <el-row>
              <h4 style="font-size: 17px;color:#ffff;" v-if="roleType==='tutor'">{{group_name}}组</h4>
            </el-row>
            <el-row  v-if="roleType==='leader'">
              <h4 style="font-size: 17px;color:#ffff;"  >TUST创新实验室  <br>
                {{campus}}分部</h4>
            </el-row>
          </el-row>
          <el-row type="flex" justify="center" style="margin-top: 25px;margin-bottom: 25px">
            <span style="font-size: 18px;color:#ffff; font-weight: 600">你好~{{username}}</span>
          </el-row>
        </el-row>
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>纳新管理</span>
          </template>
          <el-menu-item-group>
            <template slot="title">纳新</template>
            <el-menu-item :index="item.url" v-for="item in menu[roleType]">
              {{item.title}}
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>

        <el-menu-item @click="showDialog('logoutDialog')">
          <i class="el-icon-s-fold"></i>
          <span slot="title">退出登录</span>
        </el-menu-item>
      </el-menu>
    </el-col>
    <el-col :span="20" style="height: 100%">
      <el-card style='height: 100%'>
        <!--        这里需要先拿到导师的uid, 然后再去请求列表页面! -->
        <transition name="slide-fade">
          <router-view v-if="uid"/>
        </transition>
      </el-card>
    </el-col>

    <el-dialog
      title="提示"
      :visible.sync="logoutDialog"
      width="30%"
    >
      <span>确定要退出登录吗? </span>
      <span slot="footer" class="dialog-footer">
    <el-button @click="logoutDialog = false">取 消</el-button>
    <el-button type="primary" @click="logout">确 定</el-button>
  </span>
    </el-dialog>
    <batch ref="batch" v-if="roleType === 'leader'"/>
    <el-row>
    </el-row>
  </el-row>
</template>

<script>
  import batch from "../../tutor/list/batch";
  import {mapActions, mapState} from 'vuex'
  import {Notification} from "element-ui";
  import {showDialog} from "../../../untils";

  export default {
    name: "home",
    components: {batch},
    data() {
      return {
        campus: '',
        logoutDialog: false,
        dialogVisible: false,
        sideClassList: {
          show: false,
          hide: true
        },
        loading: true,

        menu: {
          ['tutor']: [
            {
              url: '/tutor/home/overView',
              title: '概览'
            },
            {
              url: '/tutor/home/studentList',
              title: '学生列表'
            },

          ],
          ['leader']: [
            {
              url: '/tutor/home/studentList',
              title: '学生列表'
            },
            {
              url: '/tutor/home/tutorList',
              title: '导师列表'
            },
            {
              url: '/tutor/home/groupList',
              title: '组列表'
            },
            // {
            //   url: '',
            //   title: '信息导出',
            //   fn: () => this.$refs['batch'].show()
            // },
          ]
        }
      }
    },
    computed: {
      ...mapState({
        token: status => status.user.token,
        username: status => status.user.username,
        uid: status => status.user.uid,
        group_name: status => status.user.group,
        roleType: status => status.user.roleType,
      })
    },
    methods: {
      showDialog(dialog) {
        showDialog.call(this, dialog)
      },
      ...mapActions(['Get_Tutor_Base_Info', 'Logout']),
      logout() {
        this.Logout();
      },

      goPage(path) {
        if (!path) {
          return
        }
        this.$router.push(path);
      },

      checkToken() {
        if (!this.token) {
          this.$router.push('/tutor/login');
          Notification.info("请先登录哦!");
          return false
        }
        return true;
      },

      init() {
        const res = this.checkToken();
        // 先确保有token
        if (!res) {
          return
        }
        //  验证token信息
        this.getUserInfo();
      },
      // 考虑到页面刷新Vuex会清空信息/ 关闭浏览器后 ,
      // 所以后端会出一个接口, 专门验证token信息, 然后返回用户信息
      // 根据本地的token去后端拿到用户信息
      getUserInfo() {
        this.Get_Tutor_Base_Info().then(res => {
          this.campus = res.user_info.campus;
          this.loading = false;
        })
      },
      handleOpen(key, keyPath) {

      },
      handleClose(key, keyPath) {
      }
    },
    created() {
      this.init();
    },
    mounted() {
      this.sideClassList.show = true;
      this.sideClassList.hide = false;
    }
  }
</script>

<style scoped>

  @import "../../../assets/css/tutor-sidebar.css";

  .side_bar {
    transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }

  .hide {
    transform: translateX(-300px);

  }

  .show {
    transform: translateX(0px);
  }

  ul {
    height: 100%;
  }

  .slide-fade-enter-active {
    transition: all .05s ease;
  }

  .slide-fade-leave-active {
    transition: all .05s cubic-bezier(1.0, 0.5, 0.8, 1.0);
  }

  .slide-fade-enter, .slide-fade-leave-to
    /* .slide-fade-leave-active for below version 2.1.8 */
  {
    transform: translateX(10px);
    opacity: 0;
  }


</style>
