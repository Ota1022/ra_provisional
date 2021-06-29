var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        visual: false,
        results: [],
        info: {
            エピソード: '',
        }
    },
    methods: {
        submit: function() {
            axios.post('/data/json-get', this.info)
            
            .then(response => {
                this.results = response.data;
                this.visual = true;
            })
            
            .catch(error => {
                console.log(error);
            })
        }
    }

});