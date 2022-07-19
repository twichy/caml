<script setup>

import HomeIcon from 'vue-material-design-icons/Home.vue';
import CogIcon from 'vue-material-design-icons/Cog.vue';
import UserIcon from 'vue-material-design-icons/Account.vue';
import LogoutIcon from 'vue-material-design-icons/Logout.vue';
import ThemeToggle from '@/components/ThemeToggle.vue';
import FileCodeIcon from 'vue-material-design-icons/FileCode.vue';
import ViewDashboardIcon from 'vue-material-design-icons/ViewDashboard.vue';
import ToyBrickIcon from 'vue-material-design-icons/ToyBrick.vue';
import PlayCircleIcon from 'vue-material-design-icons/PlayCircle.vue';
import AccountMultipleIcon from 'vue-material-design-icons/AccountMultiple.vue';</script>

<template>
  <div class="sidebar">

<!--    <div class="logo">-->
<!--      <FlaskIcon :size="50" fill-color="#F79F1F" class="logo-icon" />-->
<!--      <div class="info">-->
<!--        <h1> CAML </h1>-->
<!--        <span> Version 0.0.1 </span>-->
<!--      </div>-->
<!--    </div>-->

    <div class="user-info">
      <div class="image"> <UserIcon /> </div>
      <div class="info">
        <span class="name"> David Robert </span>
        <span class="role"> Administrator </span>
      </div>
    </div>

    <nav class="main-nav">
      <RouterLink to="/"><HomeIcon :size="15" /> Overview</RouterLink>
      <RouterLink to="/about"><PlayCircleIcon :size="15" /> Jobs</RouterLink>
      <RouterLink to="/about"><FileCodeIcon :size="15" /> Workspaces</RouterLink>
      <RouterLink to="/about"><FileCodeIcon :size="15" /> Endpoints</RouterLink>
    </nav>

    <nav class="admin-nav">
      <h2>MANAGE</h2>

      <RouterLink to="/about"><AccountMultipleIcon :size="15" /> Access</RouterLink>
      <RouterLink to="/about"><ToyBrickIcon :size="15" /> Plugins</RouterLink>
      <RouterLink to="/about"><CogIcon :size="15" /> Settings</RouterLink>
      <RouterLink to="/dashboard"><ViewDashboardIcon :size="15" /> Dashboard</RouterLink>
    </nav>


    <div class="user-actions">
      <RouterLink to="/about"><LogoutIcon :size="15" /> Logout</RouterLink>
      <ThemeToggle />
    </div>

  </div>
</template>

<style lang="scss" scoped>
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  z-index: 5;
  display: flex;
  flex-direction: column;
  width: 250px;
  padding: 20px;
  background: var(--surface-color);
  transition: all 0.3s;
  box-shadow: 1px 0 20px rgba(0, 0, 0, 0.07);


  .logo {
    display: flex;
    padding-top: 8px;
    padding-bottom: 4px;

    .logo-icon{
      margin-right: 12px;
    }

    .info{
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 2px 0 7px 0;

      h1 {
        font-size: 26px;
        font-weight: 600;
        color: var(--on-surface-color);
        font-family: 'Cairo', Arial, Tahoma, sans-serif;
      }

      span {
        font-size: 12px;
        font-family: 'Open Sans', Arial, Tahoma, sans-serif;
      }
    }

  }

  .main-nav, .admin-nav, .user-actions {
    margin-top: 20px;

    a {
      display: flex;
      padding: 12px 16px;
      margin: 4px 0;
      font-size: 15px;
      text-align: left;
      border-radius: 6px;
      transition: all 0.3s;
      letter-spacing: 0.6px;
      color: var(--on-surface-color);

      &:hover {
        background: var(--surface-separator-color);
      }

      &.router-link-active {
        background: var(--primary-color);
        color: var(--on-primary-color);
      }

      span {
        margin-right: 12px;
        vertical-align: middle;
      }
    }

    h2 {
      font-size: 13px;
      letter-spacing: 0.6px;
      color: var(--on-surface-color);
      margin-bottom: 12px;
    }
  }

  .user-actions{
    margin-top: auto;
    border-top: 1px solid var(--surface-separator-color);
  }

  .user-info{
    display: flex;
    border-bottom: 1px solid var(--surface-separator-color);
    padding-bottom: 22px;

    .image {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      border: 2px solid var(--primary-color);
      background: var(--primary-color);
      color: var(--on-primary-color);
      width: 45px;
      height: 45px;
      border-radius: 6px;
    }

    .info {
      display: flex;
      flex-direction: column;
      margin-left: 12px;
      padding: 3px 0;

      .name {
        font-size: 16px;
        font-weight: 500;
        color: var(--on-surface-color);
      }

      .role {
        margin-top: auto;
        font-size: 13px;
        font-weight: 400;
        color: var(--on-surface-color);
      }
    }

    .logout {
      display: flex;
      align-items: center;
      justify-content: center;
      margin-left: auto;
    }
  }
}
</style>