const App = {
  template: `<h1>{{ title }}</h1>`,

  data: function() {
    return {
      title: 'Agencia de Buses',
    };
  },
};

const app = new Vue({
  components: {
    App,
  },
  render: h => h(App),
}).$mount('#app');
