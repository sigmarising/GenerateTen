<template>
  <div class="block">
    {{ dataNum }}
  </div>
</template>

<script>
export default {
  props: {
    dataNum: {
      type: Number,
      default: ""
    }
  }
};
</script>

<style scoped>
.block {
  border-radius: 7px;
  height: 100px;
  line-height: 100px;
  min-width: 60px;
  background: #d3dce6;
  text-align: center;
  font-size: 60px;
  font-weight: bolder;
  margin: 20px;
}
</style>
