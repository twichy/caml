<script setup></script>

<template>
  <div class="sidebar">
    <h1>Title of the website</h1>
    <nav>
      <h1>Main navigation</h1>
      <ul>
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
      </ul>
    </nav>
    <!-- aside inside sidebar -->
    <aside>
      <h1>My last tweets</h1>
      <ul>
        <li><a href="#">quoque... </a></li>
        <li><a href="#">inleceb... </a></li>
        <li><a href="#">locaaer... </a></li>
      </ul>
    </aside>
  </div>

  <div class="content">
    <RouterView/>
  </div>
</template>

<style lang="scss" scoped>
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  width: 250px;
  padding: 20px;
  background: var(--surface-color);
}

.content {
	margin-left: 250px;
	width: 100%;
  overflow: hidden;


	position: relative;
  background: var(--bg-color);
}

@media (min-width: 1024px) {

}
</style>
