const base = {
    get() {
        return {
            url : "http://localhost:8080/djangoqo04n/",
            name: "djangoqo04n",
            // 退出到首页链接
            indexUrl: ''
        };
    },
    getProjectName(){
        return {
            projectName: "Smart city tour guide website "
        } 
    }
}
export default base
