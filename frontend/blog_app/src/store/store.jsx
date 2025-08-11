import { configureStore } from '@reduxjs/toolkit';
// Corrected import to match actual filename themeslicer.jsx
import themeReducer from './themeslicer.jsx';

const store = configureStore({
  reducer: {
    theme: themeReducer,
    // other reducers here...
  },
});

export default store;
