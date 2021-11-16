import {stringify} from "qs";
import en from './locales/en.json'
import ru from './locales/ru.json'
import az from './locales/az.json'

export default {
  server: {
    host: '0.0.0.0' // default: localhost
  },
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'nuxtjs-template-by-alvin',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      {charset: 'utf-8'},
      {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      {hid: 'description', name: 'description', content: ''}
    ],
    link: [
      {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@/assets/css/main.scss',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    {src: '@/plugins/vue-awesome-swiper'},
    {src: '@/plugins/date-filter'},
    {src: '@/plugins/truncate'},
    {src: '@/plugins/vee-validate.js'},
    {src: '@/plugins/directives.js'}
  ],

  loading: '@/components/custom/LoadingBar.vue',
  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,
  build: {
    transpile: ["vee-validate/dist/rules"],
  },
  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/device',
  ],
  axios: {
    baseURL: process.env.API_BASE_URL, // Used as fallback if no runtime config is provided
    paramsSerializer: params => stringify(params, {arrayFormat: 'repeat'})
  },

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/i18n'
  ],

  auth: {
    redirect: {
      login: '/auth',
      logout: '/',
      callback: '/auth',
      home: '/'
    },
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: 'access',
          global: true,
          required: true,
          type: 'Bearer'
        },
        refreshToken: {
          property: 'refresh',
        },
        user: {
          property: false,
          // autoFetch: true
        },
        endpoints: {
          login: {url: 'account/auth/token/', method: 'post'},
          refresh: {url: 'auth/token/refresh/', method: 'post'},
          logout: {url: 'account/logout/blacklist/', method: 'post'},
          user: {url: 'account/profile/', method: 'get'}
        }
      }
    }
  },
  i18n: {
    lazy: true,
    langDir: 'locales/',
    detectBrowserLanguage: {
      useCookie: true,
      alwaysRedirect: true
    },
    strategy: 'prefix_except_default',
    locales: [
      {code: 'en', name: 'English', file: 'en.json'},
      {code: 'ru', name: 'Russian', file: 'ru.json'},
      {code: 'az', name: 'Azerbaijani', file: 'az.json'},
    ],
    defaultLocale: 'az',

    vueI18n: {
      fallbackLocale: 'en',
    }
  }
}
