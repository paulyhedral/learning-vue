<template>
  <div id="app">
    <app-header/>
    <router-view/>
  </div>
</template>

<script>
import AppHeader from '@/components/Header'
export default {
  name: 'App',
  components: {
    'app-header': AppHeader,
  }
}
</script>

<style lang="scss">
@import '~bulma/bulma'
</style>
