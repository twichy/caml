<script setup>
import {computed, ref} from 'vue';
import BrightnessIcon from 'vue-material-design-icons/Brightness4.vue';
import ToggleSwitchOnIcon from 'vue-material-design-icons/ToggleSwitch.vue';
import ToggleSwitchOffIcon from 'vue-material-design-icons/ToggleSwitchOff.vue';

// Data
const themeStorageKey = 'caml-dashboard-theme';
const theme = ref(localStorage.getItem(themeStorageKey) || 'light');

// Computed
const themeLabel = computed(() => theme.value === 'light' ? "Dark Mode" : "Light Mode");
const themeToggle = computed(() => theme.value === 'light' ? ToggleSwitchOffIcon : ToggleSwitchOnIcon);

// Methods
const changeTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light';
  localStorage.setItem(themeStorageKey, theme.value);
  setTheme()
}
const setTheme = () => {
  if(theme.value === 'light'){
    document.body.removeAttribute('data-theme');
  } else {
    document.body.setAttribute('data-theme', 'dark')
  }
}

// On create
setTheme();

</script>

<template>
  <div class="theme-toggle">
    <BrightnessIcon :size="15"/>
    <span class="theme-label"> {{ themeLabel }} </span>

    <component :is="themeToggle" :size="24" class="toggle" @click="changeTheme" />
  </div>
</template>

<style lang="scss" scoped>
.theme-toggle {
  display: flex;
  align-items: center;
  padding: 0 16px;
  height: 50px;
  margin: 4px 0;
  font-size: 15px;
  border-radius: 6px;
  text-align: left;
  letter-spacing: 0.6px;
  color: var(--on-surface-color);
  background: var(--surface-separator-color);

  .theme-label{
    margin-left: 12px;
  }

  .toggle{
    cursor: pointer;
    margin-left: auto;
  }
}

</style>
