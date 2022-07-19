<script setup>
import MarkIcon from 'vue-material-design-icons/MapMarkerDistance.vue';</script>

<template>
  <section class="page-title">
    <h1> Welcome! </h1>
    <div class="actions">
      <MarkIcon :size="20" />
      <MarkIcon :size="20" />
      <MarkIcon :size="20" />
    </div>
  </section>
</template>

<style lang="scss" scoped>
.page-title {
  padding: 12px 0;
  display: flex;
  letter-spacing: 0.6px;
  background: var(--primary-color);

  color: var(--on-primary-color);

  h1{
    font-size: 20px;
    color: var(--on-primary-color);
    letter-spacing: 0.6px;
  }

  .actions{
    margin-left: auto;

    span{
      margin-left: 10px;
    }
  }
}

</style>