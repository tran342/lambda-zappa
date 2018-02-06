<template>
  <select>
    <option disabled selected>Please select</option>
    <option v-for="f in data" v-bind:key="f.key" v-bind:value="f.key">{{ f.value }}</option>
  </select>
</template>

<script>
export default {
  name: 'SelectComp',
  props: ['data'],
  data () {
    return {}
  }
}
</script>
