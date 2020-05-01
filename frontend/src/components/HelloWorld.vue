<template>
<el-container>
    <el-header>
        <el-alert
            :title='msg'
            type="success">
        </el-alert>
    </el-header>
    <el-container>
    <el-main>
        <el-input
            type="textarea"
            :autosize="{ minRows: 10, maxRows: 20}"
            placeholder="请输入内容"
            v-model="homwork">
        </el-input>
    </el-main>
    <el-aside>
        <br>
        <el-select v-model="value" placeholder="请选择">
            <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
            </el-option>
        </el-select>
        <br>
        <br>
        <br>
        <br>
        <el-button @click="submit()">提交</el-button>
    </el-aside>
    </el-container>
</el-container>
</template>

<script>
export default {
  name: 'HelloWorld',
  created () {
    this.$axios.get('/api/hwkid').then(res => {
      for (let i = 0; i < res.data['filename'].length; i++) {
        this.options.push({'value': res.data['filename'][i], 'label': res.data['filename'][i]})
      }
    })
  },
  data () {
    return {
      homwork: '',
      msg: '请将作业内容粘贴进文本框，并在右侧下拉菜单中选择对应的作业编号后提交',
      item: [],
      options: [],
      value: ''
    }
  },
  methods: {
    submit () {
      let data = {'hwkContent': this.homwork, 'hwkID': this.value}
      this.$axios.post('/api/upload', data)
        .then(res => {
          console.log(res.data)
          this.msg = res.data['response']
        })
    },
    notice (str) {
      this.$notify({
        title: '提示',
        message: str,
        duration: 0
      })
    }
  }
}
</script>
