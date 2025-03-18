// var webpack = require('webpack');
//vue2
const path = require('path')
function resolve(dir) {
return path.join(__dirname, dir)
}
function publicPath(){
if (process.env.NODE_ENV == 'production') {
return "././";
} else {
return "/";
}
}
//vue.config.js
module.exports = {
// publicPath:"././",
publicPath: publicPath(),
// The international configuration uses other languages, and by default the Chinese language package is introduced by old
configureWebpack: {
// plugins: [
//     new webpack.NormalModuleReplacementPlugin(/element-ui[\/\\]lib[\/\\]locale[\/\\]lang[\/\\]zh-CN/, 'element-ui/lib/locale/lang/en')
// ]
resolve: {
alias: {
'@': resolve('src')
}
}
},
lintOnSave: false,
devServer: {
Host: "0.0.0.0", / / specifies to use a host. The default is localhost, but here is the default value
Port: 8081, / / specified port
Hot: true, / / open hot more new
The https: false, / / whether to open the https mode
Proxy: {/ / Request proxy server
'/ djangoqo04n': {/ / with an api prefix
target: 'http://localhost:8080/djangoqo04n/', //address
changeOrigin: true,
secure: false,
pathRewrite: {/ / Replace / api with '' null value after making the request, which does not affect the interface request
'^/djangoqo04n': ''
}
}
}
},
chainWebpack(config) {
config.module
.rule('svg')
.exclude.add(resolve('src/icons'))
.end()
config.module
.rule('icons')
.test(/\.svg$/)
.include.add(resolve('src/icons'))
.end()
.use('svg-sprite-loader')
. loader ('svg-sprite-loader ')
.options({
symbolId: 'icon-[name]'
})
.end()
}
}
