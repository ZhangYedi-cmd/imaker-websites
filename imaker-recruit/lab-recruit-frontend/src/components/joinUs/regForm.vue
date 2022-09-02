<template>
  <!-- <el-main style="height: calc(100vh - 80px);margin-top:10vh"> -->
  <el-main class="box">
    <el-row type="flex" justify="center" align="middle" :gutter="4" style="height: 100% ">
      <el-col :span="12" :xs="{span:10}">
        <el-row type="flex" justify="center" align="middle">
          <!--          pc端30 移动端50-->
          <!--          img src="../../../assets/images/2.jpg" alt="">-->
          <img src="../../assets/images/2.jpg" alt="" style="width: 30vw;height: auto">
        </el-row>
      </el-col>
      <el-col :span="12" :xs="24">
        <el-row type="flex" justify="start" align="middle" style="height: 100%">
          <el-form ref="form" :model="form" label-width="80px">
            <el-row>
              <el-col :span="12">
                <el-form-item label="姓名">
                  <el-input v-model="form.username" aria-required="true"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="学号">
                  <el-input v-model="form.uniLearn"></el-input>
                </el-form-item>
              </el-col>
            </el-row>

            <el-row>
              <el-col :span="12">
                <el-form-item label="兴趣方向">
                  <el-select v-model="form.group" placeholder="选择组名" style="width: 100%;">
                    <el-option
                      v-for="item in groupList"
                      :key="item.group_name"
                      :label="item.group_name"
                      :value="item.group_name">
                    </el-option>
                  </el-select>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="校区">
                  <el-select v-model="form.campus" placeholder="选择你所在的校区">
                    <el-option label="河西校区" value="河西校区"></el-option>
                    <el-option label="泰达校区" value="泰达校区"></el-option>
                  </el-select>
                </el-form-item>
              </el-col>
            </el-row>

            <el-row>
              <el-col :span="12">
                <el-form-item label="学院">
                  <el-input v-model="form.academy"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="专业">
                  <el-input v-model="form.major"></el-input>
                </el-form-item>
              </el-col>

            </el-row>

            <el-row>

              <!--              <el-col :span="12">-->
              <!--                <el-form-item label=" 面试时间">-->
              <!--                  <el-date-picker-->
              <!--                    format=" MM 月 dd 日"-->
              <!--                    v-model="form.interview_time"-->
              <!--                    type="datetime"-->
              <!--                    placeholder="选择日期时间">-->
              <!--                  </el-date-picker>-->
              <!--                </el-form-item>-->
              <!--              </el-col>-->
              <el-col :span="12">
                <el-form-item label="电话">
                  <el-input v-model="form.tel"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="邮箱">
                  <el-input v-model="form.email"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-row>

            </el-row>
            <el-form-item label="自我介绍">
              <el-input
                type="textarea"
                placeholder="请输入内容"
                maxlength="200"
                show-word-limit
                rows="10"
                v-model="form.introduce"
              >
              </el-input>

            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">立即创建</el-button>

            </el-form-item>
          </el-form>
        </el-row>
      </el-col>
    </el-row>
  </el-main>
</template>

<script>
  import {submitRegForm} from "../../api/student/joinUs-form";
  import {Notification} from "element-ui";
  import {getGroupList} from "../../api/group/group";

  export default {
    data() {
      return {
        code: '',
        form: {
          uniLearn: '',
          username: '',
          // interview_time: '',
          campus: '',
          group: '',
          email: '',
          introduce: '',
          tel: '',
          major: '',
          academy: ''
        },
        groupList: [],
      }
    },

    methods: {
      onSubmit() {
        submitRegForm(this.form).then(res => {
        });
        Notification.success("报名成功!");
      },

      async getGroupList() {
        const res = await getGroupList();
        this.groupList = res.group.tutor_list;
      },

      init() {
        this.getGroupList();
      }
    },

    created() {
      this.init()
    }
  }
</script>

<style scoped lang="less">
  .box {
    background: url(../../assets/images/mainbg.png) no-repeat center/cover;
    height: 100vh;
    padding-top: 200px;
  }

  @media screen and (max-width: 768px ) {
    .el-col-xs-10 {
      display: none !important;
    }
  }

  /*屏幕宽度 大于700px 且 小于900px 时*/
  @media screen and (min-width: 768px) and (max-width: 992px ) {

  }

  /*屏幕宽度 大于900px 且 小于1200px 时*/
  @media screen and (min-width: 992px) and (max-width: 1200px ) {

  }

  /*屏幕宽度 大于1200px 时*/
  @media screen and (min-width: 1200px ) {

  }
</style>
