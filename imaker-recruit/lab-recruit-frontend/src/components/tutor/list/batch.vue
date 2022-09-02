<!-- 批量导出信息-->
<template>
  <div>
    <el-dialog :visible.sync="batchDialog" title="信息导出">
      <el-form label-width="100px">
        <el-form-item label="选择组: ">
          <el-select v-model="formData.group_name" placeholder="选择组名">
            <el-option
              v-for="item in groupList"
              :key="item.group_name"
              :label="item.group_name"
              :value="item.group_name">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
    <el-button @click="batchDialog = false">取 消</el-button>
    <el-button type="primary" @click="batchDialog = false">导 出</el-button>
  </span>
    </el-dialog>
  </div>
</template>

<script>
  import {getGroupList} from "../../../api/group/group";

  export default {
    name: "batch",
    data() {
      return {
        batchDialog: false,
        /**
         * 传参
         * */
        formData: {
          group_name: ''
        },
        /**
         * 获取的组列表
         * */
        groupList: [],

      }
    },
    methods: {
      init() {
        this.getGroupList();
      },
      show() {
        this.batchDialog = true;
      },
      async getGroupList() {
        const res = await getGroupList();
        this.groupList = res.group.tutor_list;
      },
    },
    created() {
      this.init();
    }
  }
</script>

<style scoped>

</style>
