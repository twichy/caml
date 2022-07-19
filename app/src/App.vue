<script setup>

import Sidebar from '@/components/Sidebar.vue';</script>

<template>
  <Sidebar />

  <div class="content">
    <RouterView/>
  </div>
</template>

<style lang="scss" scoped>
.content {
  position: relative;
  margin-left: 250px;
  width: calc(100% - 250px);
  height: 100vh;
  z-index: 3;
  overflow-y: scroll;
  background: var(--bg-color);

  main{
    padding: 24px;
  }

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 150px;
    z-index: 1;
    background: var(--primary-color);
  }
}

@media (min-width: 1024px) {

}
</style>
