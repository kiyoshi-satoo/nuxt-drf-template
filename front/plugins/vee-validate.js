import Vue from "vue";

import {ValidationProvider, ValidationObserver, extend} from 'vee-validate'
import {required} from 'vee-validate/dist/rules'

Vue.component('ValidationProvider', ValidationProvider)
Vue.component('ValidationObserver', ValidationObserver)

extend("required", {
  ...required,
  message: "Required"
});

