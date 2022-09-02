<template>
  <div>
    <el-card class="box-card" style="min-height: 100vh">
      <el-row style="margin-top: 20px">
        <el-col>
          <span style="font-size: 15px; margin-right: 10px">用户名</span>
          <el-input style="width: 200px;margin-right: 20px" v-model="listData.username"></el-input>
          <div style="display: inline-block" v-if="roleType !== 'tutor'">
            <span style="font-size: 15px; margin-right: 10px">组</span>
            <el-select v-model="listData.group_name" placeholder="选择组名">
              <el-option
                v-for="item in groupList"
                :key="item.group_name"
                :label="item.group_name"
                :value="item.group_name">
              </el-option>
            </el-select>
            <el-button type="primary" @click="getTutorList()" style="margin-left: 20px">查 询</el-button>
            <el-button type="primary" @click="clearInfo()">重置条件</el-button>
          </div>
        </el-col>
      </el-row>


      <el-table
        v-loading="loading"
        :data="tableData"
        border
        max-height="450"
        style="width: 100%;margin-top: 50px">
        <el-table-column
          fixed
          prop="username"
          label="用户名">
        </el-table-column>
        <el-table-column
          fixed
          prop="roleType"
          label="身份">
        </el-table-column>

        <el-table-column
          prop="username"
          label="组"
        >
          <template slot-scope="scope">
              <span>
                {{scope.row.group.group_name}}
              </span>
          </template>
        </el-table-column>

        <el-table-column
          prop="email"
          label="邮箱"
        >
        </el-table-column>

        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template slot-scope="scope">
            <el-button type="text" size="small" @click="showDialog('deleteTutorDialog',scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-row type="flex" justify="center" style="margin-top: 50px">

        <el-pagination
          background
          layout="prev, pager, next"
          :total="total"
          :page-size="listData.pre_page"
          @current-change="getTutorList"
        >
        </el-pagination>
      </el-row>
      <!-- Form -->
    </el-card>

    <el-dialog title="删除学生" :visible.sync="deleteTutorDialog">
      <el-row>
        <h3>确定要删除导师信息吗? (此操作不可恢复) </h3>
      </el-row>

      <div slot="footer" class="dialog-footer">
        <el-button @click="deleteTutorDialog = false">取 消</el-button>
        <el-button type="primary" @click="deleteTutor">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</template>

<script>
  import {getStudentList, changeStudentInfo, deleteStudent, addAnnotation, deleteTutor} from "../../../api/tutor/tutor";
  import {mapState} from "vuex";
  import {Notification} from 'element-ui';
  import {getGroupList} from "../../../api/group/group";
  import {getTutorList} from "../../../api/tutor/tutor";
  import {showDialog} from "../../../untils";

  export default {
    computed: {
      ...mapState({
        token: status => status.user.token,
        username: status => status.user.username,
        uid: status => status.user.uid,
        group_name: status => status.user.group,
        roleType: status => status.user.roleType,
      })
    },
    data() {
      return {
        /**
         * 删除导师弹出框
         * */
        deleteTutorDialog: false,
        loading: false,
        total: null,
        tableData: [],
        listData: {},
        formLabelWidth: '120px',
        groupList: [],
        currentObj: {}
      };
    },

    methods: {
      init() {
        this.initListData();
        this.getTutorList();
        this.getGroupList();
      },

      showDialog(dialog, row) {
        showDialog.call(this, dialog, row)
      },
      /**
       * 获取导师列表
       * */
      async getTutorList(page) {
        this.loading = true;
        this.goTopDuration();
        if (page) {
          this.listData.page = page;
        }
        // Vuex 的优先级是低于 data 的
        const res = await getTutorList(this.listData);
        this.tableData = res.tutor.tutor_list;
        this.total = res.tutor.total_elements;
        this.loading = false;
      },
      goTopDuration() {
        var timer = setInterval(function () {
          //获取滚动条距离顶部高度
          var osTop = document.documentElement.scrollTop || document.body.scrollTop;
          var ispeed = Math.floor(-osTop / 7);
          document.documentElement.scrollTop = document.body.scrollTop = osTop + ispeed;
          //到达顶部，清除定时器
          if (osTop == 0) {
            clearInterval(timer);
          }
        }, 30);
      },
      deleteTutor() {
        let query = {uid: this.currentObj.uid};
        let that = this;
        if (query.uid === this.uid) {
          this.$message.warning("你不能删除自己哦!");
          return
        }
        deleteTutor(query).then(res => {
          that.getTutorList();
          this.deleteTutorDialog = false;
        })
      },

      async getGroupList() {
        const res = await getGroupList();
        this.groupList = res.group.tutor_list;
      },

      clearInfo() {
        this.initListData();
        this.getTutorList();
      },
      initListData() {
        this.listData = {
          page: '1',
          pre_page: 10,
          username: '',
          group_name: ''
        }
      }
    },
    created() {
      this.init();
    },
    watch: {}
  }
</script>
