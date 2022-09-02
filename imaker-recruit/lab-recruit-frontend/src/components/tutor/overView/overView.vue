<template>
  <el-col>
    <topBilibili></topBilibili>
    <el-row style="margin-top: 3vh">
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <h3>概览</h3>
        </div>
        <div>
          <el-row type="flex" justify="center">
            <el-col class="data-card">
              <el-card class="card success">

                <span class="card-text"> 面试通过人数</span>
                <br>
                <br>
                <span class="card-text" style="margin-top: 10px">
                  <span style="font-size: 30px">
                           {{passed_count}}人
                  </span>

                </span>
              </el-card>
            </el-col>
            <el-col class="data-card">
              <el-card class="card not-pass">
                <span class="card-text"> 面试不通过人数</span>
                <br>
                <br>
                <span class="card-text" style="margin-top: 10px">
                  <span style="font-size: 30px">
                           {{not_passed_count}}人
                  </span>
                </span>
              </el-card>
            </el-col>
            <el-col class="data-card">
              <el-card class="card all-num">
                <span class="card-text"> 面试总人数</span>
                <br>
                <br>
                <span class="card-text" style="margin-top: 10px">
                  <span style="font-size: 30px">
                           {{all_count}}人
                  </span>
                </span>
              </el-card>
            </el-col>
          </el-row>

        </div>
      </el-card>

    </el-row>
  </el-col>

</template>

<script>
  import {getStudentSummary} from "../../../api/tutor/tutor";
  import topBilibili from "../tutorInfo/topBilibili";
  import {mapState} from "vuex";

  export default {
    components: {
      topBilibili
    },
    computed: {
      ...mapState({
        token: status => status.user.token,
        username: status => status.user.username,
        uid: status => status.user.uid,
        group_name: status => status.user.group,
      })
    },
    data() {
      return {
        all_count: null,
        ing_count: null,
        not_passed_count: null,
        passed_count: null
      }
    },

    methods: {
      format(percentage) {
        return percentage;
      },

      async getStudentSummary() {
        const query = {
          uid: this.uid
        };
        const res = await getStudentSummary(query);
        this.all_count = res.data.all_student_count;
        this.ing_count = res.data.on_going_student_count;
        this.not_passed_count = res.data.not_pass_student_count;
        this.passed_count = res.data.pass_student_count;
      },

      init() {
        this.getStudentSummary();
      }
    },

    created() {
      this.init();
    }
  }
</script>

<style scoped>
  .card {
    height: 200px;
    width: 300px;
    border-radius: 30px;
  }

  .card:hover {
    transform: scale(1.1);
  }

  .card-text {
    color: #fff;
    font-size: 20px;
  }

  .card-text span {
    margin-top: 20px;
  }

  .success {
    background-color: #67C23A;
  }

  .all-num {
    background-color: #409EFF;
  }

  .not-pass {
    background-color: #F56C6C;

  }


  .data-card {
    display: flex;
    flex-direction: column;
    align-items: center
  }

  body {
    margin: 0;
    padding: 0;

  }

  header {
    height: 160px;
    position: relative;
    overflow: hidden;
    /*这里定义一个变量,可以通过Var()函数访问到*/
    --percentage: 0.5;
  }

  /*主轴交叉轴居中显示*/
  /*把几张图片摆到一行*/
  header .media,
  header .tree {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  header img,
  header video {
    position: absolute;
    display: block;
    width: 120%;
    height: 100%;
    object-fit: cover;
    /*    自适应*/
  }

  /*先从早上到晚上*/
  header .morning {
    z-index: 20;
    /*根据js传参自动计算透明度*/
    opacity: calc(1 - (var(--percentage) - 0.25) / 0.25);
  }

  header .afternoon {
    z-index: 10;
    opacity: calc(1 - (var(--percentage) - 0.5) / 0.5);
  }

  header .media {
    transform: translateX(calc(var(--percentage) * 100px));
  }

  /*树动起来*/
  header .tree {
    transform: translateX(calc(var(--percentage) * 50px));
    filter: blur(3px);
    /*    filter属性设置高斯模糊*/
  }

  header .morning .media,
  header .morning .tree,
  header .morning .morning,
  header .morning .afternoon {
    transition: none;
  }

  header .window-cover {
    opacity: calc((var(--percentage) - 0.9) / 0.1);
  }

</style>
