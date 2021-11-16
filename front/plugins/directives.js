import Vue from 'vue';

Vue.directive('click-outside', {
  bind: function (el, binding, vnode) {
    el.clickOutsideEvent = function (event) {
      // here I check that click was outside the el and his childrens
      if (!(el == event.target || el.contains(event.target))) {
        // and if it did, call method provided in attribute value
        vnode.context[binding.expression](event);
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unbind: function (el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  },
});


Vue.directive('img-lazyload', {
  inserted: function (el) {
    function loadImage() {
      el.classList.add('img-lazy-loading')

      var newImage = new Image()
      newImage.src = el.dataset.src
      // when success
      newImage.onload = function () {
        el.src = el.dataset.src
        el.classList.remove('img-lazy-loading')
      }
    }

    function callback(entries, observer) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          loadImage()
          observer.unobserve(el)
        }
      })
    }

    function createIntersectionObserver() {
      const options = {
        root: null,
        threshold: 0.2,
      }
      const observer = new IntersectionObserver(callback, options)
      observer.observe(el)
    }

    if (!window['IntersectionObserver'])
      loadImage()
    else {
      createIntersectionObserver()
    }
  }

});
