<template>
    <div class="messageVue">
      <el-dialog
        title="心得感悟"
        :visible.sync="dialogVisible"
        width="30%">
        <span class="content-input">请输入您的留言：</span>
        <el-input style="margin-top: 20px" type="textarea" :rows="4" placeholder="留下你的学习心得体会吧" v-model="textAera"></el-input>
        <div class="name-box">
          <span>请输入您的姓名：</span>
          <el-input class="name-input" placeholder="请输入您的姓名" v-model="name"></el-input>
        </div>

        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="Confirm">确 定</el-button>
        </span>
      </el-dialog>
      <div class="background">
        <div class="boy" @click="boy_click"></div>
        <div class="bubble">
          <div class="text-box">
            <p>点我分享属于你的心得！</p>
          </div>
        </div>
        <div class="back-borad">
          <div class="background-title">
            <div class="title-box">
              <div class="title-box-title"></div>
            </div>
          </div>
          <div class="back-content">
            <el-scrollbar style="height: 550px" >
              <transition name="el-fade-in-linear">
                <el-timeline v-show="show">
                  <el-timeline-item v-for="(list, index) in cur_message" :key="index"
                                    :timestamp="list.time" placement="top" size="large" color="#fb1d04">
                    <el-card>
                      <h4>{{list.content}}</h4>
                      <p>{{list.name}}   提交于  {{list.time}}</p>
                    </el-card>
                  </el-timeline-item>
                </el-timeline>
              </transition>
            </el-scrollbar>
            <div class="paginator-box">
              <el-pagination
                :current-page="this.Index"
                :page-sizes="[5, 10]"
                :page-size="this.cur"
                layout="total, sizes, prev, pager, next, jumper"
                :total="this.All_page"
                @current-change="handleCurrentChange"
                @size-change="handleSizeChange">
              </el-pagination>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
    export default {
        name: "message",
        data(){
          return{
            show: true,
            dialogVisible: false,
            textAera:'',  //心得体会
            name:'',      //姓名
            Index: 1,   //当前页数
            All_page: 0,    //总页数
            cur: 0,     //当前条数,
            cur_message:[],   //当前显示总留言条数
          }
        },
      methods:{
          timeFormatter:function() {
              var t = new Date();
              return t.getFullYear() + "-" + (t.getMonth() + 1) + "-" + t.getDate() + " " +
                t.getHours() + ":" + t.getMinutes() + ":" + t.getSeconds();
          },
          Confirm:function(){
            let that = this;
            if (this.textAera === ''){
              this.$message.error('输入内容不能为空')
            }
            else if (this.name === ''){
              this.$message.error('输入姓名不能为空')
            }
            else{
              let content = {};
              content['name']= this.name;
              content['content'] = this.textAera;
              content['time'] = this.timeFormatter();
              this.$axios({
                method: 'post',
                url: 'api/share_think_send',
                data: content,
              }).then(function (res) {
                if (res.data.code === 0){
                    that.$message({
                    message:'分享成功!',
                    type:'success'
                  });
                  that.init_page(0, that.cur)
                }
              });
              this.dialogVisible = false;
              this.textAera = ''
            }
          },
          init_page:function (index, cur) {
            let split = index*cur;
            let that = this;
            that.cur_message = [];
            this.$axios.post('api/share_think').then(function (res) {
              let content = res.data.data;
              that.All_page = content.length;
              while (split < (index+1)*cur){
                if (split === that.All_page)
                  break;
                let dict = {};
                dict['name'] = content[split][0];
                dict['content'] = content[split][1];
                dict['time'] = content[split][2];
                that.cur_message.push(dict);
                split++
              }
            });
          },
          handleCurrentChange:function (val) {
            this.Index = val;
            this.init_page(val-1, this.cur);
          },
          handleSizeChange:function (val) {
            this.cur = val;
            this.init_page(0, this.cur);
            this.Index = 0;
          },
          boy_click:function () {
            this.dialogVisible = true
          }
      },
      mounted() {
      },
      created() {
          this.cur = 5;
          this.init_page(0, this.cur)
      }
    }
</script>

<style scoped>
  .background{
    min-width:  1400px;
    width: 100%;
    min-height: 800px;
    height: 100%;
    position: absolute;
    padding-top: 0;
    background-image: url("/static/picture/message_bg.jpg");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
  }
  .boy{
    position: absolute;
    bottom: 130px;
    left: 40px;
    width: 250px;
    height: 250px;
    background-image: url("/static/picture/boy.png");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
    animation: boy-animate 1s infinite;
    cursor: pointer;
  }
  @keyframes boy-animate {
    0%{bottom: 130px}
    50%{bottom: 150px}
    100%{bottom: 130px}
  }
  @-webkit-keyframes boy-animate {
    0%{bottom: 130px}
    50%{bottom: 150px}
    100%{bottom: 130px}
  }
  .bubble{
    position: absolute;
    width: 150px;
    height: 100px;
    background-image: url("/static/picture/bubble.png");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
    bottom: 400px;
    left: 100px;
  }
  .text-box{
    width: 80px;
    margin-left: 43px;
  }
  .text-box p{
    font-size: 14px;
  }
  .back-borad{
    width: 1200px;
    margin: 0 auto;
  }
  .background-title{
    position: relative;
    z-index: 2;
    height: 200px;
    box-sizing: border-box;
  }
  .title-box{
    margin-left: 430px;
    margin-top: -25px;
    width: 350px;
    height: 200px;
    background-image: url("/static/picture/message_title.png");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
  }
  .title-box-title{
    width: 297px;
    height: 95px;
    position: relative;
    top: 64px;
    margin: auto;
    background-image: url("/static/picture/think_share.png");
    background-size: 100% 100%;
    background-position: center center;
    background-repeat: no-repeat;
  }
  .back-content{
    width: 800px;
    margin: auto;
    position: relative;
    height: 600px;
    box-sizing: border-box;
  }
  .paginator-box{
    margin-top: 10px;
    text-align: center;
  }
  .name-box{
    width: 100%;
    margin-top: 20px;
    display: inline-block;
  }
  .name-box span{
    font-size: 15px;
    color: #333;
    float: left;
  }
  .name-input{
    margin-top: 20px;
    float: left;
  }
  .content-input{
    color: #333;
    font-size: 15px;
  }
</style>
<style>
    .messageVue .el-timeline-item__timestamp{
      color: #fb1d04;
      line-height: 1;
      font-size: 13px;
    }
    .messageVue .el-timeline-item__tail {
      position: absolute;
      left: 4px;
      height: 100%;
      border-left: 2px solid #fb1d04;
    }
    .messageVue .el-card{
      background: #fdeab6;
      cursor: pointer;
    }
    .messageVue .el-card:hover{
      background: #fc692f;
      color:#fff;
    }
    .messageVue .el-pager li{
      transition: all .4s;
    }
    .messageVue .el-pager li.active{
      background: #fb1d04;
      color: #fff;
      cursor: pointer;
    }
    .messageVue .el-pager li:hover{
      color: #fb1d04;
    }
    .messageVue .el-pager li.active:hover{
      color:#fff
    }
</style>
