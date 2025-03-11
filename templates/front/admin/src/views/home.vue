<template>
<div class="content" :style='{"minHeight":"100vh","padding":"30px","background":"url(http://codegen.caihongy.cn/20230228/47752d6be3a94e8892a83ec2a70c8443.png) no-repeat center top /100% 100%"}'>
	<div class="text" :style='{"margin":"50px auto","fontSize":"34px","color":"#012c7a","textAlign":"center","fontWeight":"bold"}'>Welcome {{this.$project.projectName}}</div>
    <div class="cardView">
        <div class="cards" :style='{"margin":"0 0 20px 0","alignItems":"center","justifyContent":"center","display":"flex"}'>
			<div :style='{"border":"0px solid #ccc","boxShadow":"0 0px 0px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('menpiaoxinxi','首页总数')">
				<div :style='{"width":"160px","borderRadius":"5px 0px 0px 5px","background":"#1b5a90","height":"120px"}'></div>
				<div :style='{"alignItems":"center","borderRadius":"0 5px 5px 0","flexDirection":"column","background":"#fff","display":"flex","width":"180px","justifyContent":"center"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"30px","color":"#333","fontWeight":"bold","height":"24px"}'>{{menpiaoxinxiCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>ticket information numbers</div>
				</div>
			</div>
			<div :style='{"border":"0px solid #ccc","boxShadow":"0 0px 0px rgba(0,0,0,.3)","margin":"0 10px","borderRadius":"4px","display":"flex"}' v-if="isAuth('mingsuxinxi','首页总数')">
				<div :style='{"width":"160px","borderRadius":"5px 0px 0px 5px","background":"#1b5a90","height":"120px"}'></div>
				<div :style='{"alignItems":"center","borderRadius":"0 5px 5px 0","flexDirection":"column","background":"#fff","display":"flex","width":"180px","justifyContent":"center"}'>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"30px","color":"#333","fontWeight":"bold","height":"24px"}'>{{mingsuxinxiCount}}</div>
					<div :style='{"margin":"5px 0","lineHeight":"24px","fontSize":"16px","color":"#666","height":"24px"}'>hotel information numbers</div>
				</div>
			</div>
        </div>
    </div>
</div>
</template>
<script>
//0
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
            menpiaoxinxiCount: 0,
            mingsuxinxiCount: 0,
		};
	},
  mounted(){
    this.init();
    this.getmenpiaoxinxiCount();
    this.getmingsuxinxiCount();
  },
  methods:{
    init(){
        if(this.$storage.get('Token')){
        this.$http({
            url: `${this.$storage.get('sessionTable')}/session`,
            method: "get"
        }).then(({ data }) => {
            if (data && data.code != 0) {
            router.push({ name: 'login' })
            }
        });
        }else{
            router.push({ name: 'login' })
        }
    },
    getmenpiaoxinxiCount() {
        this.$http({
            url: `menpiaoxinxi/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.menpiaoxinxiCount = data.data
            }
        })
    },
    getmingsuxinxiCount() {
        this.$http({
            url: `mingsuxinxi/count`,
            method: "get"
        }).then(({
            data
        }) => {
            if (data && data.code == 0) {
                this.mingsuxinxiCount = data.data
            }
        })
    },
  }
};
</script>
<style lang="scss" scoped>
    .cardView {
        display: flex;
        flex-wrap: wrap;
        width: 100%;

        .cards {
            display: flex;
            align-items: center;
            width: 100%;
            margin-bottom: 10px;
            justify-content: center;
            .card {
                width: calc(25% - 20px);
                margin: 0 10px;
                /deep/.el-card__body{
                    padding: 0;
                }
            }
        }
    }
</style>
