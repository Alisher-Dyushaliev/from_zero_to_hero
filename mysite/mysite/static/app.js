new Vue ({
    el: '#app',
    data: {
    list_app: []
    },
    created: function () {
        const vue_app = this;
        axios.get ('/vue/')
        .then (function (response) {
        console.log(response.data)
        })
    }
})