<template>
  <div>
    <el-card class="box-card" style="min-height: 100vh">
      <el-row style="margin-top: 20px">
        <el-col>
          <div style="display: inline-block" v-if="roleType !== 'tutor'">
            <el-button type="primary" @click="showDialog('newGroupDialog')" style="margin-left: 20px">新建组</el-button>
          </div>
        </el-col>
      </el-row>
      <el-table
        v-loading="loading"
        :data="groupList"
        border
        max-height="450"
        style="width: 100%;margin-top: 50px">
        <el-table-column
          fixed
          prop="group_name"
          label="组名称">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template slot-scope="scope">
            <el-button type="text" size="small" @click="showDialog('deleteGroupDialog',scope.row)">删除</el-button>
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

    <el-dialog title="删除组" :visible.sync="deleteGroupDialog">
      <el-row>
        <h3>确定要删除组信息吗? (此操作不可恢复) </h3>
      </el-row>

      <div slot="footer" class="dialog-footer">
        <el-button @click="deleteGroupDialog = false">取 消</el-button>
        <el-button type="primary" @click="deleteGroup">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog title="新建组" :visible.sync="newGroupDialog">
      <el-row>
        <el-form inline label-width="120px">
          <el-form-item label="组名称: ">
            <el-input v-model="newGroupQuery.group_name"></el-input>
          </el-form-item>
          <div slot="footer" class="dialog-footer">
            <el-button @click="newGroupDialog = false">取 消</el-button>
            <el-button type="primary" @click="deleteGroupDialog">创建</el-button>
          </div>

        </el-form>
      </el-row>

      <div slot="footer" class="dialog-footer">
        <el-button @click="newGroupDialog = false">取 消</el-button>
        <el-button type="primary" @click="newGroup">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</template>

<script>
  import {getStudentList, changeStudentInfo, deleteStudent, addAnnotation, deleteTutor} from "../../../api/tutor/tutor";
  import {mapState} from "vuex";
  import {Notification} from 'element-ui';
  import {deleteGroup, getGroupList, newGroup} from "../../../api/group/group";
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
        newGroupDialog: false,
        deleteGroupDialog: false,
        loading: false,
        total: null,
        tableData: [],
        listData: {},
        formLabelWidth: '120px',
        groupList: [],
        currentObj: {},

        newGroupQuery: {
          group_name: ''
        }
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
      deleteGroup() {
        let query = {id: this.currentObj.id};
        let that = this;

        deleteGroup(query).then(res => {
          that.getGroupList();
          this.deleteGroupDialog = false;
        })
      },

      newGroup() {
        var that = this;
        newGroup(this.newGroupQuery).then(res => {
          that.getGroupList();
          that.newGroupDialog = false;
          that.newGroupQuery = {};
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
        }
      }
    },
    created() {
      this.init();
    },
    watch: {}
  }
</script>
