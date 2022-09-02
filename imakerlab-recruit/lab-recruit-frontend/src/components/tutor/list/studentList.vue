<template>
  <div>
    <el-card class="box-card" style="min-height: 100vh">
      <div slot="header" class="clearfix">
        <h2 v-if="roleType!=='leader'">{{group_name}}组学生列表</h2>
        <h2 v-if="roleType==='leader'">学生列表</h2>
      </div>
      <el-form> <el-row style="margin-top: 20px">
      <el-col>
        <span style="font-size: 15px; margin-right: 10px">姓名</span>
        <el-input style="width: 200px;margin-right: 20px" v-model="listData.username"></el-input>

        <span style="font-size: 15px; margin-right: 10px">年级</span>
        <el-input style="width: 200px;margin-right: 20px" v-model="listData.grade"></el-input>


        <span style="font-size: 15px; margin-right: 10px">学院</span>
        <el-input style="width: 200px;margin-right: 20px" v-model="listData.academy"></el-input>
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
        </div>



        <el-row style="margin-top: 2vh">
          <el-col>
            <span style="font-size: 15px; margin-right: 10px">状态</span>
            <el-select v-model="listData.status" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
              <el-option
                value="">
                不选择
              </el-option>
            </el-select>
            <el-button type="primary" @click="getStudentList()" style="margin-left: 20px">查 询</el-button>
            <el-button type="primary" @click="clearInfo()">重置条件</el-button>
          </el-col>
        </el-row>
      </el-col>
    </el-row>

      </el-form>

      <el-table
        v-loading="loading"
        :data="tableData"
        border
        max-height="450"
        style="width: 100%;margin-top: 50px">
        <el-table-column
          fixed
          prop="uniLearn"
          label="学号"
          width="100">
        </el-table-column>

        <el-table-column
          prop="grade"
          label="年级"
          width="100">
        </el-table-column>
        <el-table-column
          prop="username"
          label="姓名"
          width="120">
        </el-table-column>
        <el-table-column
          prop="username"
          label="组"
          width="120">
          <template slot-scope="scope">
              <span>
                {{scope.row.group.group_name}}
              </span>
          </template>
        </el-table-column>
        <el-table-column
          prop="status"
          label="状态"
          width="150">
        </el-table-column>

        <el-table-column
          prop="tel"
          label="电话号"
          width="150">
        </el-table-column>
        <el-table-column
          prop="email"
          label="邮箱"
          width="150"
        >
        </el-table-column>

        <el-table-column
          prop="email_status"
          label="邮件通知"
          width="120">
        </el-table-column>

        <el-table-column
          prop="major"
          label="专业"
          width="120">
        </el-table-column>
        <el-table-column
          prop="academy"
          label="学院"
          width="120">
        </el-table-column>
        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template slot-scope="scope">
            <el-button type="text" size="small" @click="checkStudentInfo(scope.row)">审核</el-button>
            <el-button type="text" size="small" @click="deleteStudent(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-row type="flex" justify="center" style="margin-top: 50px">

        <el-pagination
          background
          layout="prev, pager, next"
          :total="total"
          :page-size="listData.pre_page"
          @current-change="getStudentList"
        >
        </el-pagination>
      </el-row>
      <!-- Form -->

      <el-dialog title="查看学生信息" :visible.sync="dialogFormVisible">
        <el-form>
          <el-form-item label="学生姓名" :label-width="formLabelWidth">
            <el-row type="flex" justify="center">
              {{currentStudent.username}}
            </el-row>
          </el-form-item>
          <el-form-item label="学号" :label-width="formLabelWidth">
            <el-row type="flex" justify="center">
              {{currentStudent.uniLearn}}
            </el-row>
          </el-form-item>
          <el-form-item label="状态" :label-width="formLabelWidth">
            <el-row type="flex" justify="center">
              {{currentStudent.status}}
            </el-row>
          </el-form-item>
          <el-form-item label="专业" :label-width="formLabelWidth">
            <el-row type="flex" justify="center">
              {{currentStudent.major}}
            </el-row>
          </el-form-item>
          <el-form-item label="学院" :label-width="formLabelWidth">
            <el-row type="flex" justify="center">
              {{currentStudent.academy}}
            </el-row>
          </el-form-item>

          <el-form-item label="自我介绍" :label-width="formLabelWidth">
            <el-row type="flex" justify="center">
              {{currentStudent.introduce}}
            </el-row>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button @click="annotationDialog = true">评 价</el-button>
          <el-button @click="checkStudentStatus(currentStudent)">审 核</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
        </div>
      </el-dialog>


      <el-dialog title="评 价" :visible.sync="annotationDialog">
        <el-form>
          <el-form-item label="评分" :label-width="formLabelWidth">
            <el-row type="flex" justify="start">
              <el-rate
                v-model="currentStudent.rate"
                show-score
                text-color="#ff9900"
                score-template="{value}">
              </el-rate>
            </el-row>
          </el-form-item>
          <el-form-item label="注释" :label-width="formLabelWidth">

            <el-row type="flex" justify="center">
              <el-input
                type="textarea"
                :rows="10"
                placeholder="请输入内容"
                v-model="currentStudent.annotation">
              </el-input>
            </el-row>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="annotationDialog = false">取 消</el-button>
          <el-button type="primary" @click="addAnnotation()">保存</el-button>
        </div>
      </el-dialog>
      <!--    审核状态-->
      <el-dialog title="审核" :visible.sync="checkStudent">
        <el-form ref="form" label-width="150px">
          <el-form-item label="面试状态">
            <el-select v-model="changeStudentInfo.status" placeholder="请选择">
              <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>

          <el-form-item label="是否发送邮件通知">
            <el-select v-model="changeStudentInfo.send_mail" placeholder="请选择">
              <el-option
                v-for="item in send_mail_select"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="checkStudent = false">取 消</el-button>
          <el-button type="primary" @click="submitChange()">确 定</el-button>
        </div>
      </el-dialog>

      <el-dialog title="删除学生" :visible.sync="deleteStudentDialog">
        <el-row>
          <h3>确定要删除学生信息吗? (此操作不可恢复) </h3>
        </el-row>

        <div slot="footer" class="dialog-footer">
          <el-button @click="deleteStudentDialog = false">取 消</el-button>
          <el-button type="primary" @click="submitDelete">确 定</el-button>
        </div>
      </el-dialog>
    </el-card>
  </div>

</template>

<script>
  import {getStudentList, changeStudentInfo, deleteStudent, addAnnotation} from "../../../api/tutor/tutor";
  import {mapState} from "vuex";
  import {Notification} from 'element-ui';
  import {getGroupList} from "../../../api/group/group";

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
        loading: true,
        total: null,
        tableData: [],
        listData: {},
        annotationDialog: false,
        dialogTableVisible: false,
        dialogFormVisible: false,
        deleteStudentDialog: false,
        checkStudent: false,
        formLabelWidth: '120px',
        options: [
          {
            label: "第一轮面试",
            value: "第一轮面试",
          },
          {
            label: "第二轮面试",
            value: "第二轮面试",
          },
          {
            label: "第三轮面试",
            value: "第三轮面试",
          },
          {
            label: "通过",
            value: "通过",
          },
          {
            label: "不通过",
            value: "不通过",
          },
          {
            label: "未审核",
            value: "未审核",
          },
        ],
        send_mail_select: [
          {
            label: "发送",
            value: true,
          },
          {
            label: "不发送",
            value: false,
          },
        ],
        changeStudentInfo: {
          uid: '',
          status: '',
          send_mail: false
        },
        currentStudent: {
          username: '',
          uniLearn: '',
          rate: 0,
        },
        groupList: [],
      };
    },

    methods: {
      init() {
        this.initListData();
        this.getStudentList();
        this.getGroupList();
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

      async getStudentList(page) {
        this.loading = true;
        this.goTopDuration();
        if (page) {
          this.listData.page = page;
        }
        // Vuex 的优先级是低于 data 的
        const res = await getStudentList(this.listData);
        this.tableData = res.student.student_list;
        this.total = res.student.total_elements;
        this.loading = false;
        this.listData.page = '1'
      },

      deleteStudent(student) {
        this.deleteStudentDialog = true;
        this.currentStudent = student;
      },

      async submitDelete() {
        const query = {
          uid: this.currentStudent.uid
        };
        const res = await deleteStudent(query);
        Notification.success(res.message);
        this.deleteStudentDialog = false;
        this.getStudentList();
      },

      async addAnnotation() {
        this.annotationDialog = false;
        const res = await addAnnotation(this.currentStudent);
        Notification.success(res.message);
      },

      submitChange() {
        this.checkStudent = false;
        // if (this.currentStudent.status === this.changeStudentInfo.status) {
        //   return
        // }
        // 调用接口更改信息,
        changeStudentInfo(this.changeStudentInfo).then(res => {
          this.currentStudent.status = this.changeStudentInfo.status;
          Notification.success(res.message);
          this.getStudentList();
        });
      },

      checkStudentInfo(studentInfo) {
        // 设置current对象(深拷贝)
        this.currentStudent = studentInfo;
        // 打开弹窗
        this.dialogFormVisible = true;
      },

      checkStudentStatus(currentStudent) {
        // 深拷贝对象
        let student = JSON.parse(JSON.stringify(currentStudent));
        this.checkStudent = true;
        this.changeStudentInfo = student;
      },

      async getGroupList() {
        const res = await getGroupList();
        this.groupList = res.group.tutor_list;
      },

      clearInfo() {
        this.initListData();
        this.getStudentList();
      },
      initListData() {
        this.listData = {
          page: '1',
          // 返回当前导师的学生列表
          tutor_uid: this.uid, // 这里传入导师的uid, 返回与导师相同校区 and 相同组的学生
          pre_page: 10,
          username: '',
          status: ''
        }
      }
    },
    created() {
      this.init();
    },
    watch: {}
  }
</script>
