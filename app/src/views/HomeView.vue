<script setup>
import PageTitle from "@/components/PageTitle.vue";</script>

<template>
  <main class="page-content">
    <PageTitle />
    <div class="mock-stats"></div>
    <div class="mock-table"></div>
  </main>
</template>

<style lang="scss" scoped>
.page-content {
  position: relative;
  z-index: 5;

  .mock-stats{
    width: 100%;
    height: 200px;
    background: var(--surface-color);
    border-radius: 4px;
    margin-top: 24px;
  }

  .mock-table{
    width: 100%;
    height: 800px;
    margin-top: 24px;
    background: var(--surface-color);
    border-radius: 4px;
  }
}
</style>