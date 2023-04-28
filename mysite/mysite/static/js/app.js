new Vue ({
    el: '#vuejs',
    data: {
    news: []
    },
    created: function () {
        const vue_app = this;
        axios.get ('/json/')
        .then (function (response) {
        vue_app.news = response.data
        })
    }
}
)