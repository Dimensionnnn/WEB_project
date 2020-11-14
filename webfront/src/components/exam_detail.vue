<template>
    <div>
      <el-dialog
        :title="result"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
        <span class="dialog_span">此次测验您的总分为:</span>
        <span class="dialog_score">{{total_score}}</span>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
        </span>
      </el-dialog>
      <div class="exam_detail">
        <div v-for="(item, index) in option_exam" :key="index">
          <div class="exam_section" :id="item.id">
            <div class="exam_title">
              <i>{{item.id}}</i>
              <span>{{item.title}}</span>
            </div>
            <div class="exam_option">
              <ul>
                <el-radio-group v-model="item.select">
                  <li><el-radio label="1">A、{{item.A}}</el-radio></li>
                  <li><el-radio label="2">B、{{item.B}}</el-radio></li>
                  <li><el-radio label="3">C、{{item.C}}</el-radio></li>
                  <li><el-radio label="4">D、{{item.D}}</el-radio></li>
                </el-radio-group>
              </ul>
            </div>
            <div class="button-box">
              <el-button type="primary" @click="Save_test(index)" round style="margin-right: 20px">保存到我的习题集</el-button>
              <el-button type="danger" @click="show_Answer(index)" round v-show="answer_show">保存到我的错题集</el-button>
              <div class="answer-footer" v-show="answer_show">答案：{{answer_list[item.answer-1]}}</div>
            </div>
          </div>
        </div>
        <div class="exam_footer">
          <el-button class="confirm_button" @click="Confrim">确认提交</el-button>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "exam_detail",
        data(){
          return{
            option_exam:[],
            total_score: 0,
            answer_show:false,
            dialogVisible: false,
            result:'',
            answer_list: ['A', 'B', 'C', 'D'],
            answer_visible:[]
          }
        },
      props:{
         parentmsg:{
           type: String,
           required: true
         }
      },
      watch:{
        parentmsg(val){
          if (val === '1'){
            let that = this;
            this.$axios.post('api/get_exam').then(function (res) {
              let content = res.data.data;
              for (let i=0; i<content.length; i++){
                let dict = {};
                dict['id'] = content[i][0];
                dict['title'] = content[i][1];
                dict['A'] = content[i][2];
                dict['B'] = content[i][3];
                dict['C'] = content[i][4];
                dict['D'] = content[i][5];
                dict['answer'] = content[i][6];
                dict['select'] = '';
                that.option_exam.push(dict);
                that.answer_visible.push(false)
              }
            })
          }
          if (val === '2'){
            let that = this;
            this.$axios.post('api/get_else_exam').then(function (res) {
              let content = res.data.data;
              for (let i=0; i<content.length; i++){
                let dict = {};
                dict['id'] = content[i][0];
                dict['title'] = content[i][1];
                dict['A'] = content[i][2];
                dict['B'] = content[i][3];
                dict['C'] = content[i][4];
                dict['D'] = content[i][5];
                dict['answer'] = content[i][6];
                dict['select'] = '';
                that.option_exam.push(dict);
                that.answer_visible.push(false)
              }
            })
          }
        }
      },
      methods:{
          Save_test:function(index){
            this.$message({
              message:'题目'+(index+1).toString()+'成功保存到您的习题集',
              type:'success'
            })
          },
          show_Answer:function(index){
            this.$message({
              message:'题目'+(index+1).toString()+'成功保存到您的习题集',
              type:'success'
            })
          },
          Confrim:function () {
            let flag = true;
            let that = this;
            that.total_score = 0;
            let per_score = 100/(that.option_exam.length);
            for (let i=0; i<that.option_exam.length; i++){
              if (that.option_exam[i]['select'] === ''){
                flag = false;
                $('#'+(i+1).toString()).css('box-shadow', '0 0 10px 0 inset #ff3333');
              }
              else{
                 $('#'+(i+1).toString()).css('box-shadow', '4px 4px 5px 5px #c0c0c0');
                 if (that.option_exam[i]['select'] === that.option_exam[i]['answer'].toString()){
                   that.total_score += per_score;
                   if (that.total_score >= 60){
                     that.result = '恭喜您'
                   }
                   else{
                     that.result = '很遗憾'
                   }
                 }
              }
            }
            if (flag){
              that.dialogVisible = true;
              that.answer_show = true;
            }
            else{
              that.$alert('有题目您尚未答完哦!', '温馨提示', {
                  confirmButtonText:'确定'
              });
            }
          },
          handleClose:function () {
            this.dialogVisible = false;
          }
      },
        created(){
        }
    }
</script>

<style scoped>
  .exam_detail{
    width: 1200px;
    height: auto;
    margin: 60px auto;
    position: relative;
    margin-bottom: 15px;
  }
  .exam_section{
    padding: 10px;
    width: 100%;
    min-height: 60px;
    background: #fff;
    margin-bottom: 40px;
    box-shadow: 4px 4px 5px 5px #c0c0c0;
  }
  .exam_title{
    width: 100%;
    padding: 10px;
  }
  .exam_title i{
    color: #333;
    margin-right: 20px;
  }
  .exam_option{
    width: 100%;
    padding: 5px 20px;
    margin-bottom: 20px;
  }
  .exam_option ul{
    width: 100%;
  }
  .exam_option ul li{
    text-decoration: none;
    display: inline-block;
    float: left;
    margin-right: 20px;
    margin-bottom: 10px;
  }
  .button-box{
    margin-left: 45px;
    margin-bottom: 10px;
  }
  .exam_footer{
    width: 100%;
    min-height: 40px;
    padding-bottom: 20px;
  }
  .confirm_button{
    float: right;
    background: #287960;
    color: #fff;
    transition: all 200ms;
  }
  .confirm_button:hover{
    background: #4C9833;
  }
  .dialog_span{
    float: left;
    display: inline-block;
    margin-right: 20px;
    font-size: 15px;
  }
  .dialog_score{
    font-size: 20px;
    color: #fb1d04;
    font-weight: bold;
  }
  .answer-footer{
    display: inline-block;
    position: relative;
    left: 60px;
    font-size: 20px;
    color: #fb1d04;
  }
</style>

