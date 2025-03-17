import Vue from 'vue'
import App from '@/App.vue'
// element ui Completely introduced
import ElementUI from 'element-ui'
import '@/assets/css/element-variables.scss'
import '@/assets/css/style.scss'
// Load the routing
// import router from '@/router/router-static.js';
import router from '@/router/router-static.js';
// Breadcrumb navigation, registered as a global component
import BreadCrumbs from '@/components/common/BreadCrumbs'
// Introducing the echart
import * as echarts from 'echarts'
import 'echarts-wordcloud'
// Introduce the echart motif
// import  '@/assets/js/echarts-theme-macarons.js'
import 'echarts/theme/macarons.js'
// ajax
import http from '@/utils/http.js'
// Basic configuration
import base from '@/utils/base'
// utility class
import { isAuth, getCurDate, getCurDateTime } from '@/utils/utils'
// storage Package
import storage from "@/utils/storage";
// Upload the component
import FileUpload from "@/components/common/FileUpload";
import ExcelFileUpload from "@/components/common/ExcelFileUpload";
// Rich text editing component
import Editor from "@/components/common/Editor";
The // api interface
import api from '@/utils/api'
// Data calibration tool class
import * as validate from '@/utils/validate.js'
// Background map
import VueAMap from 'vue-amap'
import '@/icons'
/ / Export export
import JsonExcel from 'vue-json-excel'
// put a seal on
import printJS from 'print-js'
//MD5
import md5 from 'js-md5';
// Background map
Vue.use (VueAMap)
VueAMap.initAMapApiLoader ({
//key: 'ca04cee7ac952691aa67a131e6f0cee0',
key: '001d42eaa139dc53fd655e7c23c0187e',
plugin: ['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor', 'AMap.Geocoder'],
// Default gold sdk, version 1.4.4
v: '1.4.4'
})
Vue.prototype.$validate = validate
Vue.prototype.$http = http / / ajax request method
Vue.prototype. $echarts = echarts
Vue.prototype.$base = base.get()
Vue.prototype.$project = base.getProjectName()
Vue.prototype.$storage = storage
Vue.prototype. $api = api
// Judgment authority method
Vue.prototype.isAuth = isAuth
Vue.prototype.getCurDateTime = getCurDateTime
Vue.prototype.getCurDate = getCurDate
//Vue.prototype. $base = base
Vue.use(ElementUI, { size: 'medium', zIndex: 3000 });
Vue.config.productionTip = false
// Component Global components
Vue.component('bread-crumbs', BreadCrumbs)
Vue.component('file-upload', FileUpload)
Vue.component('excel-file-upload', ExcelFileUpload)
Vue.component('editor', Editor)
/ / Export export
Vue.component ('downloadExcel', JsonExcel)
//MD5
Vue.prototype. $md5 = md5;
New view ({
render: h => h(App),
router
}).$mount('#app')
